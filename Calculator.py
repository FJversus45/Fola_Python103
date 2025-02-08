from tkinter import*

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title('My Calculator')
        self.window.geometry('500x500')

        self.display = Entry(self.window, width=45, bg="light green")
        self.display.grid()

        self.numPad = Frame(self.window)
        self.numPad.grid(row=1, column=0, sticky=W)

        self.operatorPad = Frame(self.window)
        self.operatorPad.grid(row=1, column = 0 , sticky = E)

        self.constantPad = Frame(self.window)
        self.constantPad.grid(row=7, column = 0, sticky = W)

        self.numPadList = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.', '='
        ]

        self.constantList = ["pi", "Speed of Light", "Speed of Sound", "Avg dist to Sun",] 

        self.operatorList = [
            '*', '/',
            '+', '-',
            '(', ')',
            'C']

        r=0
        c=0

        for i in self.numPadList:
            myButton = Button(self.numPad, text=i, width = 5, command= lambda x = i: self.mynumber(x))
            myButton.grid(row=r, column = c)
            c=c+1
            if c>2:
                c=0
                r=r+1


        r1 = 0
        c1=0

        for btn in self.operatorList:
            operatorButton = Button(self.operatorPad, text=btn, width = 5, command = lambda x = btn: self.mynumber(x))
            operatorButton.grid(row=r1, column = c1)
            c1=c1+1
            if c1>1:
                c1=0
                r1=r1+1

        r2 = 0
        for btn in self.constantList:
            constantBtn = Button(self.constantPad, text=btn, width = 15, command = lambda y = btn: self.mynumber(y))     
            constantBtn.grid(row=r2,column = 0)
            r2 = r2 + 1



        self.window.mainloop()


    #myLabel = Label(window, text ="My Label")
    #myLabel.grid(row=2, column =4, sticky= W)
    # sticky = W west, N North, S South, E East

    def mynumber(self, num):
        if num == 'C':
            self.display.delete(0, END)
        elif num == '=':
            try:
                calc = self.display.get()
                result = str(eval(calc))
                self.display.insert(END, "=" + result)
            except:
                self.display.delete(0, END)
                self.display.insert(END, 'ERONOUS CALCULATION')
        elif num == "pi":
            self.display.insert(END, "3.14")
        elif num == "Speed of Light":
            self.display.insert(END, "3000000000")
        elif num == "Speed of Sound":
            self.display.insert(END, "330")
        elif num == "Avg dist to Sun":
            self.display.insert(END, "149597887.5")
        else:
            self.display.insert(END, num)


Fola = Calculator()