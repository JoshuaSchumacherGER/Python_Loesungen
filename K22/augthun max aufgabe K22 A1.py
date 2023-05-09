import tkinter as tk

# Aufgabe K22 A1 von Max Augthun

# Fenster rot


def rot_faerben():
    hauptfenster.configure(background="red")


hauptfenster = tk.Tk()
hauptfenster.geometry("300x200")

# Button
mein_button = tk.Button(
    hauptfenster, text="Fenster rot färben", command=rot_faerben)
mein_button.pack()

hauptfenster.mainloop()
