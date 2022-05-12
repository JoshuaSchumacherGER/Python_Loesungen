#Author Daniel Heinz

import tkinter
from tkinter import NSEW, StringVar, ttk
from tkinter.messagebox import showinfo

mainwindow = tkinter.Tk()
mainwindow.title("MainWindow")
mainwindow.wm_geometry('300x150')
mainwindow.resizable(False,False)

###Aufgabe 4###
label = tkinter.Label(mainwindow,text="MainLabel")
label.grid(row=0,column=1,columnspan=2,sticky="nsew")

stringVariable = StringVar()
def reply(name):
    showinfo(title="Reply", message = "Hello %s!" % name)
ent = ttk.Entry(mainwindow, textvariable=stringVariable, width=20)
ent.grid(row=1,column=1,columnspan=2,sticky="nsew")
ent.bind("<Return>", (lambda event: reply(ent.get())))


###MenuBar - Aufgabe 5###
def btnNewWindow():
    newWindow = tkinter.Toplevel()
    newWindow.title("about")
    newWindow.wm_geometry("225x50")
    newWindow.resizable(False,False)
    ttk.Label(newWindow, text="Daniel Heinz").pack()
    pass

menubar = tkinter.Menu(mainwindow)

filemenu = tkinter.Menu(menubar)
filemenu.add_command(label="about",command=btnNewWindow)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="File", menu=filemenu)

mainwindow.config(menu=menubar)


mainwindow.mainloop()
