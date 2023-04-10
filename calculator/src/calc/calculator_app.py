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

        tk.Button(self.root, text="1", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("1")).grid(row=1, column=0)
        tk.Button(self.root, text="2", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("2")).grid(row=1, column=1)
        tk.Button(self.root, text="3", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("3")).grid(row=1, column=2)
        tk.Button(self.root, text="4", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("4")).grid(row=2, column=0)
        tk.Button(self.root, text="5", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("5")).grid(row=2, column=1)
        tk.Button(self.root, text="6", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("6")).grid(row=2, column=2)
        tk.Button(self.root, text="7", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("7")).grid(row=3, column=0)
        tk.Button(self.root, text="8", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("8")).grid(row=3, column=1)
        tk.Button(self.root, text="9", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("9")).grid(row=3, column=2)
        tk.Button(self.root, text="0", height=2, width=6, font=(
            "Arial", 18), command=lambda: self.button_click("0")).grid(row=4, column=1)

        tk.Button(self.root, text="+", height=2, width=6, font=("Arial", 18),
                  command=lambda: self.button_click("+")).grid(row=1, column=3)
        tk.Button(self.root, text="-", height=2, width=6, font=("Arial", 18),
                  command=lambda: self.button_click("-")).grid(row=2, column=3)
        tk.Button(self.root, text="*", height=2, width=6, font=("Arial", 18),
                  command=lambda: self.button_click("*")).grid(row=3, column=3)
        tk.Button(self.root, text="/", height=2, width=6, font=("Arial", 18),
                  command=lambda: self.button_click("/")).grid(row=4, column=3)

        tk.Button(self.root, text="C", height=2, width=6, font=(
            "Arial", 18), command=self.calculator.clear()).grid(row=4, column=0)
        tk.Button(self.root, text="=", height=2, width=6, font=(
            "Arial", 18), command=self.calculator.clear()).grid(row=4, column=2)

        self.root.mainloop()

    # next function doesn't work yet
    def button_click(self, text):
        if text == "C":
            self.calculator.clear()
        elif text == "=":
            self.calculator.get_result()
        else:
            pass


app = CalculatorApp()
