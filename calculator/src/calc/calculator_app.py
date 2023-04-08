import tkinter as tk
from src.calc.calculator import Calculator

class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()

        self.root = tk.Tk()
        self.root.geometry("425x400")
        self.root.config(bg="white")
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.text = tk.Text(self.root, height=2, width=16, font=("Arial", 22))
        self.text.grid(columnspan=5)

        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)

        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)

        self.create_button("C", 4, 0)
        self.create_button("=", 4, 2)

        self.root.mainloop()
    
    def create_button(self, text, row, column):
        button = tk.Button(self.root, text=text, height=2, width=6, font=("Arial", 18), command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        if text == "C":
            self.clear()
        elif text == "=":
            self.result()



app = CalculatorApp()
        



