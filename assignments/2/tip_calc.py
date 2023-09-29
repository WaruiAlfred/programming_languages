"""
SCT211-0023/2021
ALFRED WARUI KAHENYA
"""

total_bill = float(input("Enter the total bill amount: "))
tip = input(
    "Enter the tip amount(percentage of total bill,eg:1):\n1. 10%\n2. 12%\n3. 15%\n"
)
no_of_people_splitting_bill = int(
    input("Enter the number of people splitting the bill: ")
)

individual_bill = 0

if tip == "1":
    individual_bill = (total_bill + (total_bill * 0.1)) / no_of_people_splitting_bill
    print("The individual bill is: ", round(individual_bill, 2))
elif tip == "2":
    individual_bill = (total_bill + (total_bill * 0.12)) / no_of_people_splitting_bill
    print("The individual bill is: ", round(individual_bill, 2))
elif tip == "3":
    individual_bill = (total_bill + (total_bill * 0.15)) / no_of_people_splitting_bill
    print("The individual bill is: ", round(individual_bill, 2))
