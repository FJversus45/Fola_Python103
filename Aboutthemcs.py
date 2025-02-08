
import tkinter as tk
from tkinter import*

myGlossary = {
    "OnePiece": "Luffy want to be the King of the Pirates",
    "Naruto": "Naruto want to become the Hokage",
    "DragonBall": "Goku wants to be the strongest in the universe",
    "JJK": "Yuji wants to collect all 20 of sukuna's fingers",
    "MHA": "Deku wants to become the symbol of peace"
}

window = Tk()
window.title("Fola's Anime Application")
window.geometry("500x500")
window.config(bg= "black")




def Submit():
    try:
        enteredtext = myentry.get()
        myOutput.delete(0.0, END)
        output= myGlossary[enteredtext]
        myOutput.insert(END, output)
    except:
        myOutput.delete(0.0, END)
        myOutput.insert(END, "Word not found in the dictionary")

mylabel = Label(window, text = "Enter the anime you want to learn about:", )
mylabel.pack()
myentry = Entry(window, width = 25, bg = "DeepSkyBlue4")
myentry.pack()
mybutton = Button(window, width=7, text="Submit", bg="DeepSkyBlue4", command=Submit)
mybutton.pack()
mySecondLabel = Label(window, text="Definition:",)
mySecondLabel.pack()
myOutput = Text(window, width=50, height=15, bg="DeepSkyBlue4")
myOutput.pack()


window.mainloop()
