import tkinter as tk
from src.calc.calculator import Calculator


class CalculatorApp:
    """
    Luokka, joka käyttää tkinteriä ja Calculator luokkaa suorittaakseen laskutoimituksia.
    
    Attributes:
        calculator: uusi Calculator()
        root: sovelluksen tkinter juuri
        text: tkinterin teksti, joka näyttää käyttäjän syötteet ja laskujen tulokset 
    """

    def __init__(self):
        """
        Luokan konstruktori, alustaa luokan ja määrittää graafisen käyttöliittymän.
        """
        self.calculator = Calculator()
        self.calculation = ""

        self.root = tk.Tk()
        self.root.geometry("425x400")
        self.root.config(bg="white")
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.text = tk.Text(self.root, height=2, width=16, font=("Arial", 22))
        self.text.grid(columnspan=5)

        self.create_button()

        self.root.mainloop()

    def create_button(self):
        """
        Metodi luo laskimen painikkeet ja sijoittaa ne laskimen graafiseen käyttöliittymään.
        """

        buttons = [
        {"text": "1", "row": 1, "column": 0},
        {"text": "2", "row": 1, "column": 1},
        {"text": "3", "row": 1, "column": 2},
        {"text": "4", "row": 2, "column": 0},
        {"text": "5", "row": 2, "column": 1},
        {"text": "6", "row": 2, "column": 2},
        {"text": "7", "row": 3, "column": 0},
        {"text": "8", "row": 3, "column": 1},
        {"text": "9", "row": 3, "column": 2},
        {"text": "0", "row": 4, "column": 1},
        {"text": "+", "row": 1, "column": 3},
        {"text": "-", "row": 2, "column": 3},
        {"text": "*", "row": 3, "column": 3},
        {"text": "/", "row": 4, "column": 3},
        {"text": "C", "row": 4, "column": 0},
        {"text": "=", "row": 4, "column": 2},
        ]

        for button in buttons:
            tk.Button(self.root, text=button["text"], height=2, width=6
            , font=("Arial", 18), command=lambda txt=button["text"]:
            self.button_click(txt)).grid(row=button["row"], column=button["column"])

    def button_click(self, text):
        """
        Metodi luo tapahtuman eri näppäimille. Päivittää laskinta riippuen käyttäjän syötteestä.
        """

        if text == "C":
            self.calculator.clear()
            self.text.delete("1.0", tk.END)

        elif text == "=":
            if self.calculator.calculation:
                self.calculator.num = int(self.text.get("1.0", tk.END))
                if self.calculator.calculation == "+":
                    self.calculator.add(self.calculator.num)
                elif self.calculator.calculation == "-":
                    self.calculator.substract(self.calculator.num)
                elif self.calculator.calculation == "*":
                    self.calculator.multiply(self.calculator.num)
                elif self.calculator.calculation == "/":
                    self.calculator.divide(float(self.calculator.num))

                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", str(self.calculator.get_result()))
                self.calculator.clear()

        elif text in ["+", "-", "*", "/"]:
            if self.calculator.calculation:
                self.button_click("=")
            self.calculator.number = int(self.text.get("1.0", tk.END))
            self.calculator.calculation = text
            self.text.delete("1.0", tk.END)

        else:
            self.text.insert(tk.END, text)
