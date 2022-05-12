#Author Daniel Heinz

import tkinter
from tkinter import TclError, Toplevel, ttk, DoubleVar
from random import randrange

mainwindow = tkinter.Tk()
mainwindow.title("MainWindow")
mainwindow.wm_geometry('400x200')
mainwindow.resizable(False,False)

label = tkinter.Label(mainwindow,text="MainLabel")
label.place(x=155, y=60)

#End Program (example in the script)
class btnEndProg(tkinter.Button):
    def __init__(self, window, textstr):
        super().__init__(window, text=textstr, command=self.btnClick)
        self.place(x=150, y=100)
        self["height"] = 1
        self["width"] = 10   
    
    def btnClick(self):
        mainwindow.destroy()

#Change Color (K22 A1)
class btnChangeColor(tkinter.Button):
    def __init__(self, window, textstr):
        super().__init__(window, text=textstr, command=self.btnClick)
        self.place(x=150, y=130)
        self["height"] = 1
        self["width"] = 10

    def btnClick(self):
        if(mainwindow['bg'] == "#FF0000"):
            mainwindow.config(bg="#FFFFFF")
            label.config(bg="#FFFFFF")
        else:
            mainwindow.config(bg="#FF0000")
            label.config(bg="#FF0000")

#random Place Button (K22 A2)    
class btnClickMe(tkinter.Button):
    def __init__(self, window, textstr):
        super().__init__(window, text=textstr, command=self.btnClick)
        self.place(x=150, y=100)
        self["height"] = 1
        self["width"] = 10

    def btnClick(self):
        self.place(x=self.dice(0,390), y=self.dice(0,180))

    def dice(self,start:int,stop:int) -> int:
        randnumber = randrange(start,stop+1)
        return randnumber

#Calculator (K22 A3)
#CalculatorWindow
class newWindow(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Calculator")
        self.geometry("300x200")
        self.resizable(False,False)

        #first input
        self.IntVariableA = DoubleVar()
        self.IntVariableA.set(0)
        ttk.Label(self, text="Enter First Number", font=('Calibri 10')).pack()
        self.a=ttk.Entry(self, textvariable=self.IntVariableA, width=35)
        self.a.pack()

        #second input
        self.IntVariableB = DoubleVar()
        self.IntVariableB.set(0)
        ttk.Label(self, text="Enter Second Number", font=('Calibri 10')).pack()
        self.b=ttk.Entry(self, textvariable=self.IntVariableB, width=35)
        self.b.pack()
        
        resultlabel = tkinter.Label(self,text="0")
        resultlabel.pack()

        #Buttons
        btnCalculateSum = btnCreateSum(self, textstr="+", inputone=self.IntVariableA, 
                                        inputtwo=self.IntVariableB, numlabel=resultlabel)
        btnCalculateSum.place(x=90, y=120)
        
        btnCalculateDiff = btnCreateDiff(self, textstr="-", inputone=self.IntVariableA, 
                                        inputtwo=self.IntVariableB, numlabel=resultlabel)
        btnCalculateDiff.place(x=120, y=120)
        
        btnCalculateProd = btnCreateProduct(self, textstr="x", inputone=self.IntVariableA, 
                                        inputtwo=self.IntVariableB, numlabel=resultlabel)
        btnCalculateProd.place(x=150, y=120)
        
        btnCalculateQuote = btnCreateQuotation(self, textstr="/", inputone=self.IntVariableA, 
                                        inputtwo=self.IntVariableB, numlabel=resultlabel)
        btnCalculateQuote.place(x=180, y=120)
              


#ButtonForCalculatorWindow
class btnOpenCalc(tkinter.Button):
    def __init__(self,window, textstr):
        super().__init__(window, text=textstr, command=self.btnClick)
        self.place(x=130, y=170)
        self["height"] = 1
        self["width"] = 15

    def btnClick(self):
        newwindow = newWindow(mainwindow)

#Button Definition
#AddingOperation
class btnCreateSum(ttk.Button):
    def __init__(self, window, textstr, inputone:float, inputtwo:float, numlabel:ttk.Label):
        super().__init__(window, text=textstr, command=self.btnClick,width=3)
        self.a = inputone
        self.b = inputtwo
        self.window = window        
        self.sumlabel = numlabel
    def btnClick(self):
        try:
            self.t1=self.a.get()
            self.t2=self.b.get()
            self.sum=self.t1+self.t2
            self.sumlabel.config(text=self.sum)
        except TclError:
            ttk.Label(self.window,text="Falsche Eingabe").place(x=100, y=150)

#SubtractionOperation
class btnCreateDiff(ttk.Button):
    def __init__(self, window, textstr, inputone, inputtwo, numlabel:ttk.Label):
        super().__init__(window, text=textstr, command=self.__btnClick__,width=3)
        self.a = inputone
        self.b = inputtwo
        self.window = window
        self.difflabel = numlabel
    
    def __btnClick__(self):
        try:
            self.t1=self.a.get()
            self.t2=self.b.get()
            self.diff=self.t1-self.t2 
            self.difflabel.config(text=self.diff)
        except TclError:
            ttk.Label(self.window,text="Falsche Eingabe").place(x=100, y=150)

#MultiplicationOperation
class btnCreateProduct(ttk.Button):
    def __init__(self, window, textstr, inputone, inputtwo, numlabel:ttk.Label):
        super().__init__(window, text=textstr, command=self.__btnClick__,width=3)
        self.a = inputone
        self.b = inputtwo
        self.window = window        
        self.prodlabel = numlabel
    
    def __btnClick__(self):
        try:
            self.t1=self.a.get()
            self.t2=self.b.get()
            self.prod=self.t1*self.t2 
            self.prodlabel.config(text=self.prod)
        except TclError:
            ttk.Label(self.window,text="Falsche Eingabe").place(x=100, y=150)

#DivisionOperation
class btnCreateQuotation(ttk.Button):
    def __init__(self, window, textstr, inputone, inputtwo, numlabel:ttk.Label):
        super().__init__(window, text=textstr, command=self.__btnClick__,width=3)
        self.a = inputone
        self.b = inputtwo
        self.window = window        
        self.divlabel = numlabel

    def __btnClick__(self):
        try:
            self.t1=self.a.get()
            self.t2=self.b.get()
            self.div=self.t1/self.t2 
            self.divlabel.config(text=self.div)
        except TclError:
            ttk.Label(self.window,text="Falsche Eingabe").place(x=100, y=150)



#MainWindowLogic
btnClickEnd = btnEndProg(mainwindow, "Exit")
btnClickColor = btnChangeColor(mainwindow, "Change Color")
btnClickrandom = btnClickMe(mainwindow, "Click Me!")
btnOpenCalculus = btnOpenCalc(mainwindow, "Open Calculator")


mainwindow.mainloop()
