import tkinter as tk
from tkinter import messagebox

class Calculator:
    #Konstruktor
    def __init__(self):
        self.window = tk.Tk(); 
        self.window.title("Taschenrechner"); 
        self.window.geometry("800x400"); 

        self.entry1 = tk.Entry(self.window); 
        self.entry1.place(x=10, y=10); 

        self.entry2 = tk.Entry(self.window); 
        self.entry2.place(x=10, y=40); 

        self.result_label = tk.Label(self.window, text="Ergebnis: ", font=("Arial", 12)); 
        self.result_label.place(x=200, y=10); 

        self.operator_var = tk.StringVar(); 


        '''
        Rechenarten/types of calculation
        '''
        self.add_button = tk.Button(self.window, text="+", command=self.addition, height=2, width=10); 
        self.add_button.place(x=10, y=80); 

        self.subtract_button = tk.Button(self.window, text="-", command=self.subtraction, height=2, width=10); 
        self.subtract_button.place(x=10, y=140); 

        self.multiply_button = tk.Button(self.window, text="*", command=self.multiplication, height=2, width=10); 
        self.multiply_button.place(x=10, y=200); 

        self.divide_button = tk.Button(self.window, text="/", command=self.division, height=2, width=10); 
        self.divide_button.place(x=10, y=260); 

        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear, height=2, width=10); 
        self.clear_button.place(x=10, y=320); 

        '''
        Rechenverlauf
        '''
        self.history_label = tk.Label(self.window, text="Rechenverlauf:"); 
        self.history_label.place(x=200, y=60); 

        #Anzeige von Rechnenverlauf
        self.history_text = tk.Text(self.window, height=10, width=30); 
        self.history_text.place(x=200, y=100); 

        self.rv_clear_button = tk.Button(self.window, text="RVClear", command=self.clear_history, height=2, width=10); 
        self.rv_clear_button.place(x=200, y=280); 

    def addition(self):
        try:
            num1 = float(self.entry1.get()); 
            num2 = float(self.entry2.get()); 

            result = num1 + num2; 

            self.result_label.config(text="Ergebnis: " + str(result)); 
            self.update_history(num1, num2, "+", result); 
        except ValueError:
            self.show_error_message("Bitte geben Sie gültige Zahlen ein!"); 

    def subtraction(self):
        try:
            num1 = float(self.entry1.get()); 
            num2 = float(self.entry2.get()); 

            result = num1 - num2; 

            self.result_label.config(text="Ergebnis: " + str(result)); 
            self.update_history(num1, num2, "-", result); 
        except ValueError:
            self.show_error_message("Bitte geben Sie gültige Zahlen ein!"); 

    def multiplication(self):
        try:
            num1 = float(self.entry1.get()); 
            num2 = float(self.entry2.get()); 

            result = num1 * num2; 

            self.result_label.config(text="Ergebnis: " + str(result)); 
            self.update_history(num1, num2, "*", result); 
        except ValueError:
            self.show_error_message("Bitte geben Sie gültige Zahlen ein!"); 

    def division(self):
        try:
            num1 = float(self.entry1.get()); 
            num2 = float(self.entry2.get()); 

            if num2 != 0:
                result = num1 / num2
                self.result_label.config(text="Ergebnis: " + str(result)); 
                self.update_history(num1, num2, "/", result); 
            else:
                self.show_error_message("Division durch Null ist nicht erlaubt!"); 
        except ValueError:
            self.show_error_message("Bitte geben Sie gültige Zahlen ein!"); 

    def clear(self):
        self.entry1.delete(0, tk.END); 
        self.entry2.delete(0, tk.END); 
        self.result_label.config(text="Ergebnis: "); 

    def update_history(self, num1, num2, operator, result):
        expression = f"{num1} {operator} {num2} = {result}\n"; 
        self.history_text.insert(tk.END, expression); 

    def clear_history(self):
        self.history_text.delete("1.0", tk.END); 

    def show_error_message(self, message):
        messagebox.showerror("Fehler", message); 

    def run(self):
        self.window.mainloop(); 

calculator = Calculator(); 
calculator.run(); 