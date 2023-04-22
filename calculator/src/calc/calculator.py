class Calculator:
    def __init__(self):
        self.a = 0
        self.b = ""
        self.result = 0

    def add(self, num):
        self.result = self.a + num

    def substract(self, num):
        self.result = self.a - num

    def multiply(self, num):
        self.result = self.a * num

    def divide(self, num):
        if num != 0:
            self.result = self.a / num
        else:
            self.result = None
            print("Error: Cannot divide by zero")

    def clear(self):
        self.a = 0
        self.b = ""
        self.result = 0

    def get_result(self):
        return self.result
