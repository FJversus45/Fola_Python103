class Profile:
    def __init__(self, Name, Age, Interests, Status):
        self.name = Name
        self.age = Age
        self.Interests = Interests
        self.Status = Status
        self.friends =[]



    def addFriends(self, friend):
        self.friends.append(friend.name)
        friend.friends.append(self.name)
        print(f"{friend.name} has been added to {self.name}'s friend's list.")
    
    def showFriends(self):
        print(f"{self.name}'s friends are {self.friends}.")

    def day(self):
        print(f"Welcome {self.name}. How are you today?")
       
    def rn(self):
        print(f"{self.name}, you are currently {self.Status}.")

    def flatter(self):
        print(f"{self.name}, you are looking good for {self.age} years old.")
    
    def hobby(self):
        print(f"{self.name}, likes {self.Interests}.")

    



FolaA = Profile("Fola", "12", "football and gaming", "chilling on the couch")
FolaA.day()
FolaA.rn()
FolaA.flatter()
FolaA.hobby()

Samuel = Profile("Samuel", "20", "coding and reading", "teaching")
Samuel.day()
Samuel.rn()
Samuel.flatter()
Samuel.hobby()
Samuel.addFriends(FolaA)
Samuel.showFriends()
FolaA.showFriends()