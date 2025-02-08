from tkinter import *
from tkinter import ttk
import sqlite3 as sq


connection = sq.connect("example.db")
cursor = connection.cursor()
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS folaUser(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER NOT NULL)
"""
)
Users = [
    ("Fola Aduwo", 12),
    ("Bola Tinubu", 12),
    ("Samuel", 27)
]
cursor.executemany("INSERT INTO folaUser(name, age) VALUES(?,?)", Users)
cursor.execute("SELECT * FROM folaUser")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()


class ExpenseTracker():
    def __init__(self,window):
        
        self.window = window
        self.window.title("Expense Tracker")
        self.window.geometry("500x500")
        self.createWidget()
        self.window.mainloop()

    def createWidget(self):
        myFrame = Frame(self.window)
        myFrame.pack()
        
        myLabel = Label(myFrame, text = "Date(YYYY- MM - DD)")
        myLabel.grid(sticky = "E",row = 0, column = 0)
        dateEntry = Entry(myFrame, width = 15)
        dateEntry.grid(row=0, column = 1)

        DescriptionLabel = Label(myFrame, text = "Description")
        DescriptionLabel.grid(sticky = "E",row = 1, column = 0)
        DescriptionEntry = Entry(myFrame, width = 40)
        DescriptionEntry.grid(row =1, column = 1)

        AmountLbl = Label(myFrame, text = "Amount")
        AmountLbl.grid(row =2, column = 0, sticky = "E")
        AmountEntry = Entry(myFrame, width = 15)
        AmountEntry.grid(row =2, column = 1)

        AddBtn = Button(myFrame, text = "Add Expense", bg ="azure")
        AddBtn.grid(row =3, column = 0)
        MyTree = ttk.Treeview(self.window, columns = ("ID","Date", "Description", "Amount"), show = "headings")
        MyTree.heading("ID",text = "ID")
        MyTree.column("ID", width = 30)
        MyTree.heading("Date", text = "Date")
        MyTree.column("Date", width = 100)
        MyTree.heading("Description",text = "Description")
        MyTree.column("Description", width = 200)
        MyTree.heading("Amount", text = "Amount")
        MyTree.column("Amount", width = 100, anchor= "e")
        MyTree.pack()



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
