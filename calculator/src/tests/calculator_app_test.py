import unittest
from src.calc.calculator import Calculator

class TestCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def test_addition(self):
        self.calculator.add(3)
        self.assertEqual(self.calculator.get_result(), 3)

    def test_substraction(self):
        self.calculator.substract(3)
        self.assertEqual(self.calculator.get_result(), -3)
    
    def test_multiplication(self):
        self.calculator.multiply(3)
        self.assertEqual(self.calculator.get_result(), 0)
    
    def test_division(self):
        self.calculator.divide(3)
        self.assertEqual(self.calculator.get_result(), 0)
    
    def test_division_by_zero(self):
        self.calculator.divide(0)
        self.assertEqual(self.calculator.get_result(), None)

    def test_clearing(self):
        self.calculator.clear()
        self.assertEqual(self.calculator.get_result(), 0)