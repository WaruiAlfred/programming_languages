"""
A simple calculator to perform basic mathematical operations implementing the object oriented programming paradigm
"""


class Calculator:
    def __init__(self, firstValue, secondValue):
        self.firstValue = firstValue
        self.secondValue = secondValue

    def addition(self):
        return self.firstValue + self.secondValue

    def subtraction(self):
        return self.firstValue - self.secondValue

    def multiplication(self):
        return self.firstValue * self.secondValue

    def division(self):
        return self.firstValue / self.secondValue

    def modulus(self):
        return self.firstValue % self.secondValue

    def exponentiation(self):
        return self.firstValue**self.secondValue


class User(Calculator):
    def __init__(self, firstValue, secondValue, username):
        super().__init__(firstValue, secondValue)
        self.username = username

    def greetUser(self):
        print(f"Hello {self.username}, welcome to the ultimate calculator😁")


username = input("Enter your name: ")
operationToPerform = input(
    "What operation do you want to perform?\nChoose among the following:eg.Addition \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponentiation\n\n"
)
actualOperation = operationToPerform.lower()
firstValue = int(input("Enter the first value: "))
secondValue = int(input("Enter the second value: "))
calculate = User(firstValue, secondValue, username)
result = 0

calculate.greetUser()

if actualOperation == "addition":
    result = calculate.addition()
elif actualOperation == "subtraction":
    result = calculate.subtraction()
elif actualOperation == "multiplication":
    result = calculate.multiplication()
elif actualOperation == "division":
    result = calculate.division()
elif actualOperation == "modulus":
    result = calculate.modulus()
elif actualOperation == "exponentiation":
    result = calculate.exponentiation()
else:
    print("Invalid operation")

print(
    f"The result of {actualOperation} between {firstValue} and {secondValue} is {result}"
)
