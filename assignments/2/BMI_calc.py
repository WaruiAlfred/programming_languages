"""
SCT211-0023/2021
ALFRED WARUI KAHENYA
"""

print("BMI CALCULATOR")
print("==============")
height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f} and you are underweight")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi:.2f} and you are normal")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi:.2f} and you are overweight")
elif bmi >= 30:
    print(f"Your BMI is {bmi:.2f} and you are obese")
