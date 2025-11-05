# 5 — Days of the month

monthsbeam = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 31, 7: 31, 8: 31, 9: 31, 10: 31, 11: 31, 12: 31}
# A dictionary with the keys as the months, and the number of days as values.

inputmonth = int(input("Enter a number (1-12): "))
# Variable for user input.
febwoa = 2
# Variable to indicate February in the dictionary. (Trust the process...)

if inputmonth == febwoa:
    y = "Yes"
    n = "No"
    leap_year = input(f"Is it a leap year? \n{y} or {n}: ").strip()
    if leap_year.lower() == y.lower():
        monthsbeam[2] = 29
    elif leap_year.lower() == n.lower():
        monthsbeam[2] = 28
    else:
        print("Invalid! Please answer with 'Yes' or 'No' if the year is a leap year or not.")
        exit()
# If statement with "==" operator if the user inputs "2" for February, prompting a question for leap year.
# Another if statement using lower() to ignore if Y/N is capitalized or not. It will also take the user's input and change the number of days depending on their answer.
# I decided to place this before the actual output in case if February was entered :3

if inputmonth in monthsbeam:
    print(f"The month {inputmonth} has {monthsbeam[inputmonth]} days.")
else:
    print("Invalid! Please only enter a number from 1-12!")
# If statement for if the user inputs a number from 1-12.
# "{monthsbeam[inputmonth]}" to print the value (number of days) only, rather than the whole dictionary.
# Else statement if the user does not input a number from 1-12.
