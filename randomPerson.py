
from tkinter import*
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

class People:
    def __init__(self):
        self.window = Tk()
        self.window.title("People App")
        self.window.geometry("500x500")
        

        self.myLabel = Label(self.window, text = "Welcome to My App about People" )
        self.myLabel.pack()


        self.NAMELabel = Label(self.window, bg = "Azure", text = "")
        self.NAMELabel.pack()
        
        self.fromLabel= Label(self.window, bg = "Azure", text ="")
        self.fromLabel.pack()

        self.emailLabel = Label(self.window)
        self.emailLabel.pack()

        self.pictureLbl = Label(self.window)
        self.pictureLbl.pack()

        self.loadBTN = Button(self.window, bg = 'Light Pink', width = 40, text = "Load Random", command = self.updateUI)
        self.loadBTN.pack()

        self.window.mainloop()


    def updateUI(self):
        
        NAME = data["results"][0]["name"]["first"]
        countryFrom = data["results"][0]["location"]["country"]
        Email = data["results"][0]["email"]
        iconURL = data["results"][0]["picture"]["medium"]

        self.NAMELabel.config(text= f"{NAME}\n {countryFrom} \n {Email}")

        
        iconResponse = requests.get(iconURL)
        myIcon = Image.open(io.BytesIO(iconResponse.content))
        myIcon = myIcon.resize((100,100), Image.LANCZOS)
        self.pfp = ImageTk.PhotoImage(myIcon)
        self.pictureLbl.config(image = self.pfp)
        
apiCalls = "https://randomuser.me/api"
data = requests.get(apiCalls).json()


Fola = People()

