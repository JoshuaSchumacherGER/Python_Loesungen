import tkinter as tk

class MainApplication:
    def __init__(self, window):
        self.window = window
        self.window.title("Aufgabe_K22_A4")
        self.window.geometry("600x300")

        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        self.show_name_button = tk.Button(self.window, text="Namen anzeigen", command=self.show_name_window, height=2, width=25)
        self.show_name_button.pack()

    def show_name_window(self):
        name = self.name_entry.get()
        name_window = tk.Toplevel(self.window)
        name_window.title("Name anzeigen")
        name_window.geometry("600x300")

        name_label = tk.Label(name_window, text="Ihr Name:")
        name_label.pack()

        name_text = tk.Label(name_window, text=name)
        name_text.pack()

if __name__ == "__main__":
    window = tk.Tk()
    app = MainApplication(window)
    window.mainloop()

