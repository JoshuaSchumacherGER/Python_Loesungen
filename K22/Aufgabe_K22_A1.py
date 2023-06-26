

from tkinter import *



def btn_click():
    form["bg"] = "red"








form = Tk(); 
form.title("Aufgabe_K22_A1"); 
form.wm_geometry('400x200');  


#Label und Buttons
lbl = Label(form, text="Der Button der das Fenster Rot färbt"); 
lbl.place(x=150, y= 80); 

#Unser Button den wir erstellen sollen.
btnEnd = Button(form, text= "färbt rot", command = btn_click); 
btnEnd["height"] = 2; 
btnEnd["width"] = 10; 
btnEnd.place(x = 150, y = 100); 

form.mainloop(); 






