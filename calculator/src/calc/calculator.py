class Calculator:
    def __init__(self):
        self.number = 0
        self.calculation = ""
        self.result = 0

    def add(self, num):
        self.result = self.number + num

    def substract(self, num):
        self.result = self.number - num

    def multiply(self, num):
        self.result = self.number * num

    def divide(self, num):
        if num != 0:
            self.result = self.number / num
        else:
            self.result = None
            print("Error: Cannot divide by zero")

    def clear(self):
        self.number = 0
        self.calculation = ""
        self.result = 0

    def get_result(self):
        return self.result
