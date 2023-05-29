import tkinter as tk
from math import sqrt, sin, cos, tan, log, log10, pi, e

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("350x350")
        self.master.resizable(False, False)

        self.display = tk.Entry(master, width=20, font=("Arial", 16), justify="right")
        self.display.grid(row=0, column=0, columnspan=6, padx=5, pady=5)
        
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            {"text": "C", "row": 1, "column": 0},
            {"text": "CE", "row": 1, "column": 1},
            {"text": "±", "row": 1, "column": 2},
            {"text": "√", "row": 1, "column": 3},
            {"text": "7", "row": 2, "column": 0},
            {"text": "8", "row": 2, "column": 1},
            {"text": "9", "row": 2, "column": 2},
            {"text": "/", "row": 2, "column": 3},
            {"text": "4", "row": 3, "column": 0},
            {"text": "5", "row": 3, "column": 1},
            {"text": "6", "row": 3, "column": 2},
            {"text": "*", "row": 3, "column": 3},
            {"text": "1", "row": 4, "column": 0},
            {"text": "2", "row": 4, "column": 1},
            {"text": "3", "row": 4, "column": 2},
            {"text": "-", "row": 4, "column": 3},
            {"text": "0", "row": 5, "column": 0},
            {"text": ".", "row": 5, "column": 1},
            {"text": "=", "row": 5, "column": 2},
            {"text": "+", "row": 5, "column": 3},
            {"text": "sin", "row": 2, "column": 4},
            {"text": "cos", "row": 3, "column": 4},
            {"text": "tan", "row": 4, "column": 4},
            {"text": "log", "row": 2, "column": 5},
            {"text": "ln", "row": 3, "column": 5},
            {"text": "pi", "row": 4, "column": 5},
            {"text": "e", "row": 5, "column": 5},
        ]

        for button in buttons:
            command = lambda x=button["text"]: self.calculate(x)
            tk.Button(self.master, text=button["text"], width=5, height=2, command=command).grid(
                row=button["row"], column=button["column"], padx=5, pady=5)

    def calculate(self, key):
        if key == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == "C":
            self.display.delete(0, tk.END)
        elif key == "CE":
            self.display.delete(0, tk.END)
        elif key == "±":
            try:
                value = self.display.get()
                if value[0] == "-":
                    self.display.delete(0)
                else:
                    self.display.insert(0, "-")
            except IndexError:
                pass
        elif key == "√":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, sqrt(value))
            except ValueError:
                pass
        elif key == "sin":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, sin(value))
            except ValueError:
                pass
        elif key == "cos":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, cos(value))
            except ValueError:
                pass
        elif key == "tan":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, tan(value))
            except ValueError:
                pass
        elif key == "log":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, log10(value))
            except ValueError:
                pass
        elif key == "ln":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, log(value))
            except ValueError:
                pass
        elif key == "pi":
            self.display.insert(tk.END, pi)
        elif key == "e":
            self.display.insert(tk.END, e)
        else:
            self.display.insert(tk.END, key)

root = tk.Tk()
app = Calculator(root)
root.mainloop()