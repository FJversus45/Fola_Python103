
import tkinter as Tk
from tkinter import*
from tkinter import messagebox

class MainEntry():
    def __init__(self, manager):
        self.manager = manager
        self.window = Tk()
        self.window.title("Contact Manager")
        self.window.geometry("500x500")

        self.MyLabel = Label(self.window, text = "Welcome to Contact Manager", font=28)
        self.MyLabel.pack()
        self.BlankSpace = Label(self.window, text = "")
        self.BlankSpace.pack()

        self.NameLabel = Label(self.window, text = "Enter Name")
        self.NameLabel.pack()
        self.NameEntry = Entry(self.window, width = 60, bg = "azure")
        self.NameEntry.pack()

        self.PhoneLabel = Label(self.window, text = "Enter Phone Number")
        self.PhoneLabel.pack()
        self.PhoneEntry = Entry(self.window, width = 60, bg = "azure")
        self.PhoneEntry.pack()

        self.EmailLabel = Label(self.window, text = "Enter Email")
        self.EmailLabel.pack()
        self.EmailEntry = Entry(self.window, width = 60, bg = "azure")
        self.EmailEntry.pack()

        self.AddbTN = Button(self.window, text = "Add Contact",bg = "white", width = 40, command = self.addContact)
        self.AddbTN.pack(pady=10)


        self.Searchbtn = Button(self.window, text = "Search Contact",bg = "white", width = 40, command = self.searchContacts)
        self.Searchbtn.pack(pady=5)



        self.window.mainloop()

    def addContact(self):
        name = self.NameEntry.get()
        phone = self.PhoneEntry.get()
        email = self.EmailEntry.get()

        if name and phone and email:
            self.manager.addContact(name, phone, email)
            messagebox.showinfo("Sucess",f"Contact {name} added Successfully!")
            self.clearEntries()
        else:
            messagebox.showwarning("Input Error ", "Please fill out all fields")


    def searchContacts(self):
        name = self.NameEntry.get()
        self.NameEntry.delete(0, END)
        self.PhoneEntry.delete(0, END)
        self.EmailEntry.delete(0, END)
        if name:
            contact = self.manager.findContact(name)
            if contact:
                messagebox.showinfo("Contact found", f"{name} has been found")
                self.NameEntry.insert(END, contact["name"])
                self.PhoneEntry.insert(END, contact["phone"])
                self.EmailEntry.insert(END, contact["email"])
            else:
                messagebox.showerror("Not Found", f"No constact found with name {name}")
        else:
            messagebox.showwarning("Input Error", "Please Enter a name to search")

    def clearEntries(self):
        self.NameEntry.delete(0, END)
        self.PhoneEntry.delete(0, END)
        self.EmailEntry.delete(0, END)





