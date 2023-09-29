"""
SCT211-0023/2021
ALFRED WARUI KAHENYA
"""

print("LEAP YEAR CHECKER")
print("=================")
year = int(input("Enter a year: "))

# conditions for leap year
if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
elif year % 4 != 0 and year % 100 != 0:
    print(f"{year} is not a leap year")
elif year % 100 == 0 and year % 400 != 0:
    print(f"{year} is not a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")
