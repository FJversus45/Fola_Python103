from tkinter import *
from tkinter import ttk
import sqlite3 as sq
from datetime import datetime
from tkinter import messagebox

# connection = sq.connect("example.db")
# cursor = connection.cursor()
# cursor.execute(
#     """
# CREATE TABLE IF NOT EXISTS folaUser(
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# age INTEGER NOT NULL)
# """
# )
# Users = [
#     ("Fola Aduwo", 12),
#     ("Bola Tinubu", 12),
#     ("Samuel", 27)
# ]
# cursor.executemany("INSERT INTO folaUser(name, age) VALUES(?,?)", Users)
# cursor.execute("SELECT * FROM folaUser")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# connection.commit()
# connection.close()


class ExpenseTracker():
    def __init__(self,window):
        
        self.window = window
        self.window.title("Expense Tracker")
        self.window.geometry("500x500")
        self.createDb()
        self.createWidget()
        self.populateExpenses()
        self.addAmount()
        self.window.mainloop()
        window.protocol("WM_DELETE_WINDOW", self.close())

    def createWidget(self):
        myFrame = Frame(self.window)
        myFrame.pack()
        
        myLabel = Label(myFrame, text = "Date(YYYY- MM - DD)")
        myLabel.grid(sticky = "E",row = 0, column = 0)
        self.date = StringVar(value = datetime.now().strftime("%Y-%m-%d"))
        dateEntry = Entry(myFrame, width = 15, textvariable = self.date)
        dateEntry.grid(row=0, column = 1)
    

        DescriptionLabel = Label(myFrame, text = "Description")
        DescriptionLabel.grid(sticky = "E",row = 1, column = 0)
        self.description = StringVar()
        DescriptionEntry = Entry(myFrame, width = 40, textvariable = self.description)
        DescriptionEntry.grid(row =1, column = 1)

        AmountLbl = Label(myFrame, text = "Amount")
        AmountLbl.grid(row =2, column = 0, sticky = "E")
        self.amount = StringVar()
        AmountEntry = Entry(myFrame, width = 15, textvariable = self.amount)
        AmountEntry.grid(row =2, column = 1)

        AddBtn = Button(myFrame, text = "Add Expense", bg ="azure", command = self.addExpense)
        AddBtn.grid(row =3, column = 0)
        self.MyTree = ttk.Treeview(self.window, columns = ("ID","Date", "Description", "Amount"), show = "headings")
        self.MyTree.heading("ID",text = "ID")
        self.MyTree.column("ID", width = 30)
        self.MyTree.heading("Date", text = "Date")
        self.MyTree.column("Date", width = 100)
        self.MyTree.heading("Description",text = "Description")
        self.MyTree.column("Description", width = 200)
        self.MyTree.heading("Amount", text = "Amount")
        self.MyTree.column("Amount", width = 100, anchor= "e")
        self.MyTree.pack()
    
    

    def addExpense(self):
        date = self.date.get().strip()
        description = self.description.get().strip()
        amount = self.amount.get().strip()
        if not date or not description or not amount:
            messagebox.showwarning("Input Error", "All fields are required")
            return
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Input Error", "Date must be in YYYY-MM-DD format")


        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number")

        self.cursor.execute(
            """
            INSERT INTO expenses(date,description,amount) VALUES(?,?,?)
            """, (date, description,amount)
        )
        self.conn.commit()
        # clear input
        self.description.set("")
        self.amount.set("")

        self.populateExpenses()

    def addAmount(self):
        self.cursor.execute("""
            SELECT amount FROM expenses ORDER BY id DESC
            """)
        total = self.cursor.fetchall()
        amount = 0
        for num in total:
            print(num[0])

 
    def populateExpenses(self):
        for item in self.MyTree.get_children():
            self.MyTree.delete(item)
        self.cursor.execute("""
            SELECT id,date, description, amount FROM expenses ORDER BY id DESC
            """)
        rows = self.cursor.fetchall()

        for row in rows:
            self.MyTree.insert("", "end", values = row)

    def close(self):
        self.conn.close()

    def createDb(self):
        self.conn = sq.connect("esxpense.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date TEXT NOT NULL,
                            description TEXT NOT NULL,
                            amount REAL NOT NULL
                            )
""")



Fola = ExpenseTracker(Tk())


#    def AddExpense():    
# Database - A database is a collection of organized data that can be accessed managed and updated.
# Think of a database as a filing cabinet. 
# Types of Datbases - Relational Database,and  Non-Relational Database
# Examples of Relational Datbase - MySQL, PostgreSQL, ...
# Examples of Non-Relational Database - MongoDB,  ...
# Create New Database, Read from a Database, Update a Database and, Delete from a Database
# SQL - Structured Query Language
# SQl is the language we use to query a database
# Commands in SQL - SELECT is used to select data from the database, INSERT is used to insert new dat into the database
#   Update is used to modify data iin the database, DELETE is used to delete data from the database
# Tables 
# (--)