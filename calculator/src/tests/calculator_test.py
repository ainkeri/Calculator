import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.calculator.add(2)
        self.assertEqual(self.calculator.get_result(), 2)

        self.calculator.add(2)
        self.assertEqual(self.calculator.get_result(), 4)

    def test_substract(self):
        self.calculator.substract(2)
        self.assertEqual(self.calculator.get_result(), -2)

        self.calculator.substract(10)
        self.assertEqual(self.calculator.get_result(), -12)

    def test_multiply(self):
        self.calculator.add(2)
        self.calculator.multiply(3)
        self.assertEqual(self.calculator.get_result(), 6)

        self.calculator.multiply(0)
        self.assertEqual(self.calculator.get_result(), 0)

    def test_divide(self):
        self.calculator.add(3)
        self.calculator.divide(3)
        self.assertEqual(self.calculator.get_result(), 1)

    
    def test_divide_with_zero(self):
        self.calculator.add(3)
        self.calculator.divide(0)
        self.assertEqual(self.calculator.get_result(), None)

    
    def test_clear(self):
        self.calculator.clear()
        self.assertEqual(self.calculator.get_result(), 0)
        