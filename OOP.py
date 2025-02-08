# OOP means object oriented programming

# class
# object

# Abstraction
# Inheritance
# Encapsulation
# Polymerphism


# Every class must have a constructor, even if you don't pass a parameters to it

# functions are functions that are outside a class
# methods are functions that are inside my class

# f means string formatting, and it actually allows us to use variables inside a string

# Global variable is a variable that can be accessed anywhere in the file
# Local variable is a variable that can only be accessed where it is defined

class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model
        isEngineRunning = False

    def start(self):
        self.isEngineRunning = True
        print(f"The {self.color}, {self.brand}, {self.model} is starting")
        
    def drive(self):
        if self.isEngineRunning:
            print(f"The {self.color}, {self.brand}, {self.model} zooms off")
        else:
            print(f"The {self.color}, {self.brand}, {self.model} You need to start your engine first")
    
    def stop(self):
        print(f"The {self.color}, {self.brand}, {self.model} is shutting down")



myNissan = Car("nissan", "grey", "nissan ferrari")
myNissan.start()
myNissan.drive()
myNissan.stop()


myToyota = Car("Toyota", "green", "Venza")
myToyota.start()
myToyota.drive()
myToyota.stop()

#Inheritance

# inheritance simply means a class can inherit the properties and the methods of another class
#the class that is being inherited is called the parent class
#the class that is inheirting is called the child class

#polymorphism means a child class can have a method with the same name a s the parent class
#but the child class method will override the parent class method
# this is called method overriding


class ElectricCar(Car):
    def __init__(self, brand, color, model, batterySize):
        super().__init__(brand, color, model)
        self.batterySize = batterySize
        self.chargeLevel = 100
        
    def charge(self):
        self.chargeLevel = 100
        print(f"The {self.color}, {self.brand}, {self.model} is charging")
        
    def drive(self):
        if self.chargeLevel > 0:
            self.chargeLevel -= 10
            print(f"The {self.color}, {self.brand}, {self.model}")
    def drive(self):
        if self.chargeLevel > 0:
            self.chargeLevel -= 10
            print(f"The {self.color}, {self.brand}, {self.model} Zooms Off")
        else:
            print(f"The {self.color}, {self.brand}, {self.model} Needs to charge first")
            
    def checkBatteryLevel(self):
        print(f"The {self.color}, {self.brand}, {self.model} has {self.chargeLevel}% battery left")


myTesla = ElectricCar("Tesla", "Red","Model S", 100)
myTesla.start()
myTesla.drive()
myTesla.stop()
myTesla.charge()
myTesla.checkBatteryLevel()

# Assignment
# Create a facebook userr class, thank about the parameter it can accept
# Create a method to welcom the user to facebook
# Create a method to tell the user things about themselves e.g age 
# think of 2 more methods you can create to make it more interactive