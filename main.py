number = 1234 #integer
words = "1234" + "123" # string

items=[1234,"1234","fola","sam"] #list

myitems = {
    "fola":"sam",
    12:1234,
    "pawn":"rook"} #dictionary

# dictionary is what we call a key-value pair


# tuple
myOtherItems = (
    1234, "1234", "fola", "sam"
)




import tkinter as tk
from tkinter import*

myGlossary = {
    "algorithm": "Step by Step Instruction to perform a task that a somputer understand",
    "bug": "A piece of code that is causing a program to fail or run properly",
    "binary number": "A number representes in base 2"
}

window = Tk()
window.title("Fola Glossary Application")
window.geometry("500x500")


#try -  catch statement

def onClick():
    try:
        enteredtext = myentry.get()
        myOutput.delete(0.0, END)
        output= myGlossary[enteredtext]
        myOutput.insert(END, output)
    except:
        myOutput.delete(0-0, END)
        myOutput.insert(END, "Word not found in the dictionary")

mylabel = Label(window, text = "Enter the word you want defining:")
mylabel.pack()
myentry = Entry(window, width = 25, bg = "light green")
myentry.pack()
mybutton = Button(window, width=7, text="Submit", bg="red", command=onClick)
mybutton.pack()
mySecondLabel = Label(window, text="Definition:")
mySecondLabel.pack()
myOutput = Text(window, width=50, height=15, bg="red")
myOutput.pack()


window.mainloop()


# assignment

# create a dictionary of anime the key will be the name of the anime and the value shld be a brief story of the main character

#create a tkinter window where the user can input the name of the anime and learn about the main actor
