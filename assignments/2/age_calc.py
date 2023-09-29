"""
SCT211-0023/2021
ALFRED WARUI KAHENYA
"""

"""
Age Calculator
"""

import datetime

user_name = input("Enter your name: ")  # get user name

print(f"Welcome to age calculator, {user_name}")

# get user input
day_of_birth = int(input("Enter day of birth: "))
month_of_birth = int(input("Enter month of birth: "))
year_of_birth = int(input("Enter year of birth: "))

present_time = datetime.datetime.now()  # get current time from datetime module

years_old = present_time.year - year_of_birth  # calculate years old
months_old = present_time.month - month_of_birth  # calculate months old
days_old = present_time.day - day_of_birth  # calculate days old


def get_days_in_month(month):  # function to get days in a month
    if (
        month == 1
        or month == 3
        or month == 5
        or month == 7
        or month == 8
        or month == 10
        or month == 12
    ):
        return 31  # return 31 (months with 31 days)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 28


if (
    months_old < 0 and days_old > 0
):  # if months old is less than zero(birthday month has not been reached)
    years_old -= 1  # decrement years old by one
    months_old += 12  # increment months old by 12
    print(
        f"You are {years_old} years, {months_old} months and {days_old} days old"
    )  # print age
elif days_old < 0 and months_old > 0:
    years_old -= 1  # decrement years old by one
    days_old += get_days_in_month(
        present_time.month
    )  # increment days old by days in current month
    months_old -= 1
    print(f"You are {years_old} years, {months_old} months and {days_old} days old")
elif days_old < 0 and months_old < 0:
    years_old -= 1
    months_old += 12
    days_old += get_days_in_month(present_time.month)
    print(f"You are {years_old} years, {months_old} months and {days_old} days old")
else:
    print(f"You are {years_old} years, {months_old} months and {days_old} days old")
