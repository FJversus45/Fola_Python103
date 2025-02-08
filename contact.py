from mainEntry import MainEntry
import json
# contacts.json
class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def toDict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
    
class ContactManager:
    def __init__(self, jsonfile):
        self.jsonFile = jsonfile
        self.contacts = self.loadContact()

    
    def loadContact(self):
        try:
            with open(self.jsonFile, "r")as fola:
                data = json.load(fola)
                return[Contact(**contact)for contact in data.get("contacts", [])]
        except FileNotFoundError:
            return []

    def addContact(self, name, phone, email):
        newContact = Contact(name, phone, email)
        self.contacts.append(newContact)
        self.saveContacts()

    def saveContacts(self):
        with open(self.jsonFile, 'w')as fola:
            json.dump({"contacts": [contact.toDict()for contact in self.contacts]}, fola, indent = 4)

    def findContact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.toDict()
        return None
# list comprehension is just a roundabout way of working with list

sam= ContactManager("contacts.json")
app = MainEntry(sam)