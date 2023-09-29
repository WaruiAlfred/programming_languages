"""
SCT211-0023/2021
ALFRED WARUI KAHENYA
"""

"""
A simple calculator to perform basic mathematical operations
"""

user = input("Enter your name: ")
print(f"Hello {user}, welcome to the ultimate calculator😁")

operationToPerform = input(
    "What operation do you want to perform?\nChoose among the following:eg.Addition \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponentiation\n\n"
)
firstValue = int(input("Enter the first value: "))
secondValue = int(input("Enter the second value: "))
result = 0

if operationToPerform == "Addition":
    result = firstValue + secondValue
elif operationToPerform == "Subtraction":
    result = firstValue - secondValue
elif operationToPerform == "Multiplication":
    result = firstValue * secondValue
elif operationToPerform == "Division":
    result = firstValue / secondValue
elif operationToPerform == "Modulus":
    result = firstValue % secondValue
elif operationToPerform == "Exponentiation":
    result = firstValue**secondValue
else:
    print("Invalid operation")

print(
    f"The result of {operationToPerform} between {firstValue} and {secondValue} is {result}"
)
