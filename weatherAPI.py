#API - Application Programming Interface
# API is a set of defined rules that enables applications and systems to talk to each other.
from tkinter import*
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

class WeatherApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("WeatherApp")
        self.window.geometry("500x500")
        

        self.myLabel = Label(self.window, text = "Welcome to My Weather App" )
        self.myLabel.pack()

        self.myCity = StringVar()
        self.cityLabel = Label(self.window, text ="Enter City:")
        self.cityLabel.pack()
        self.cityEntry = Entry(self.window, bg ="Azure", textvariable = self.myCity )
        self.cityEntry.pack()
        self.myButton = Button(self.window, bg = "Light Pink", text ="Get Weather", command = self.getWeather)
        self.myButton.pack()
        
        self.WeatherLabel = Label(self.window, bg = "Azure", text = "")
        self.WeatherLabel.pack()
        
        self.TempLabel= Label(self.window, bg = "Azure", text ="")
        self.TempLabel.pack()

        self.iconLabel = Label(self.window)
        self.iconLabel.pack()

        self.window.mainloop()

    def getWeather(self):
        city = self.myCity.get().strip()
        if not city:
            messagebox.showwarning("INPUT ERROR", "PLEASE ENTER A CITY")
            return 
        try:
            apiCalls = "https://api.weatherapi.com/v1/current.json?key=0dcae0d334a1406ea59144357242103&"
            apiCalls +=  f"q={city}"
            response = requests.get(apiCalls).json()
            self.updateUI(response)
        except KeyError:
            messagebox.showerror("INVALID KEY","INVALID CITY NAME OR API ISSUE")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("ERROR",f"FAILED TO FETCH WEATHER DATA :{e}")

    def updateUI(self, data):
        cityName = data["location"]["name"]
        countryName = data["location"]["country"]
        weatherDescription = data["current"]["condition"]["text"]
        tempDescription = data["current"]["temp_c"]
        iconURL = data["current"]["condition"]["icon"]

        self.WeatherLabel.config(text= f"{cityName}, {countryName} \n {weatherDescription}")
        self.TempLabel.config(text= f"{tempDescription}°C")

        fixedIconURL = f"https:{iconURL}"
        iconResponse = requests.get(fixedIconURL)
        myIcon = Image.open(io.BytesIO(iconResponse.content))
        myIcon = myIcon.resize((100,100), Image.LANCZOS)
        self.weatherIcon = ImageTk.PhotoImage(myIcon)
        self.iconLabel.config(image = self.weatherIcon)
        
apiCalls = "https://api.weatherapi.com/v1/current.json?key=0dcae0d334a1406ea59144357242103&q=wassenaar"
data = requests.get(apiCalls).json()
print(data)

Fola = WeatherApp()

# EXPLAIN API
