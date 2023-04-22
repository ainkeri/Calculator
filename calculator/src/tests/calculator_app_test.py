import unittest
from src.application.calculator_app import CalculatorApp


class TestCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.calculator_app = CalculatorApp()
        self.calculator_app.root.mainloop()
