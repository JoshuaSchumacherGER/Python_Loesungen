

from tkinter import *
import random

def moveButton():
    new_x, new_y = generateNewPositionen()
    btnEnd.place(x=new_x, y=new_y)

def generateNewPositionen():
    new_x = random.randrange(375)
    new_y = random.randrange(175)
    return new_x, new_y

form = Tk()
form.title("Aufgabe_K22_A2")
form.geometry('400x200')

btnEnd = Button(form, text="Klick mich!", command=moveButton)
btnEnd["height"] = 2
btnEnd["width"] = 10
btnEnd.place(x=150, y=100)

form.mainloop()





