class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def substract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            self.result = None
            print("Error: Cannot divide by zero")

    def clear(self):
        self.result = 0

    def get_result(self):
        return self.result
