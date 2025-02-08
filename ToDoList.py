from tkinter import*
import json
class Checklist:


    def __init__(self, jsonfile,):
        self.toDo = []
        self.jsonfile = jsonfile
        self.tasknumber = 1

        self.window = Tk()
        self.window.title("ToDoList")
        self.window.geometry("500x500")

        self.titlelabel = Label(self.window, text = "Welcome to ToDoList")
        self.titlelabel.pack()

        self.tasklabel = Label(self.window, text = "Task")
        self.tasklabel.pack()
        self.taskentry = Entry(self.window, width = 60 ,bg = "azure")
        self.taskentry.pack()

        self.taskdescriptionLBL = Label(self.window, text = "Task Description")
        self.taskdescriptionLBL.pack()
        self.taskdescriptionentry = Text(self.window, width = 60, height = 3, bg = "azure" )
        self.taskdescriptionentry.pack()

        self.taskduedateLBL = Label(self.window, text = "Due Date")
        self.taskduedateLBL.pack()
        self.taskduedateEntry = Entry(self.window, width = 60, bg = "azure")
        self.taskduedateEntry.pack()

        self.submitbtn = Button(self.window, text = "Add to List", width = 30, bg ="lightpink", command= self.submit)
        self.submitbtn.pack()

        self.changebtn = Button(self.window, text= "Edit Task", width = 30, bg= "lightpink", command = self.updateTask)
        self.changebtn.pack()
        self.changeEntry = Entry(self.window, width = "60", bg= "azure")
        self.changeEntry.pack()

        self.deleteTaskbtn = Button(self.window, text = "Delete Task", width = 40, bg = "lightpink", command = self.deleteTASK)
        self.deleteTaskbtn.pack()
        self.deleteTaskEntry = Entry(self.window, width = "60", bg = "azure")
        self.deleteTaskEntry.pack()

        self.myToDoListbtn = Button(self.window, text = "Show List", width = 30, bg = "lightpink", command = self.findTask )
        self.myToDoListbtn.pack()

        self.specificitembtn = Button(self.window, text = "Find a Task", width = 30, bg = "lightpink", command = self.findSpecificTask)
        self.specificitembtn.pack()
        self.myToDoListEntry = Entry(self.window, width = 40, bg = "azure")
        self.myToDoListEntry.pack()
        
        self.listtoolbox = Listbox(self.window, width =60, height = 5, bg ="azure")
        self.listtoolbox.pack()
        self.loadToDo()
        self.window.mainloop()
    
    def toDict(self, item, description, date, tasknumber):
        return {
            
            "item":item,
            "description":description,
            "date":date,
            "tasknumber": tasknumber
        }

    def updateTask(self):
        UpdTask = self.changeEntry.get()
        with open(self.jsonfile, "r")as fola:
            toDo = json.load(fola)
            for task in toDo["task"]:
                if task["item"] == UpdTask:
                    self.taskentry.insert(END, f"{task["item"]}")
                    self.taskdescriptionentry.insert(END, f"{task["description"]}")
                    self.taskduedateEntry.insert(END, f"{task["date"]}")
                    self.deleteTASK(task["item"])
                    
                    
    def clear(self):
        self.taskentry.delete(END, f"{"item"}")
        self.taskdescriptionentry.delete(END, f"{"description"}")
        self.taskduedateEntry.delete(END, f"{"date"}")
        

    def deleteTASK(self, updated = None):
        DelTask = updated if updated else self.deleteTaskEntry.get()   
        for task in self.toDo:
            if task["item"] == DelTask:
                print(f"Found Task {task["item"]}")
                self.toDo.remove(task)
        with open(self.jsonfile, "w") as fola:
            json.dump({"task":self.toDo}, fola, indent = 4)
            self.tasknumber = self.tasknumber + 1 
        
    
    def submit(self):   
        task = self.taskentry.get()
        description = self.taskdescriptionentry.get("1.0", "end-1c")
        date = self.taskduedateEntry.get()
        self.addTask(task, description, date, self.tasknumber)
    
    def addTask(self, task, description, date, tasknumber):
        newTask = self.toDict(task, description, date, tasknumber)
        self.toDo.append(newTask)
        with open(self.jsonfile, "w") as fola:
            json.dump({"task":self.toDo}, fola, indent = 4)
            self.tasknumber = self.tasknumber + 1 
    
    def findTask(self):
        findTask = self.myToDoListEntry.get()
        with open(self.jsonfile, "r")as fola:
            toDo = json.load(fola)
            for task in toDo["task"]:
                self.listtoolbox.insert(END, f"{task["item"]}- {task["description"]}- {task["date"]} - {task["tasknumber"]}") 


    def loadToDo(self):
        with open(self.jsonfile, "r")as fola:
            toDo = json.load(fola)
            for task in toDo["task"]:
                self.toDo.append(task)


    def findSpecificTask(self):
        specificTask = self.myToDoListEntry.get()
        with open(self.jsonfile, "r")as fola:
            toDo = json.load(fola)
            for task in toDo["task"]:
                if task["item"] == specificTask:
                    self.listtoolbox.insert(END, f"{task["item"]}- {task["description"]}- {task["date"]} - {task["tasknumber"]}") 

Fola = Checklist("ToDoList.json")


# update and delete task