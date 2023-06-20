class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def add(self, num1, num2, num3):
        return num1 + num2 + num3

calculator = Calculator()
print(calculator.add(2, 3))        # Output: TypeError: add() missing 1 required positional argument: 'num3'
print(calculator.add(2, 3, 4))     # Output: 9
