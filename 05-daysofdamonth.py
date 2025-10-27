monthsbeam = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 31, 7: 31, 8: 31, 9: 31, 10: 31, 11: 31, 12: 31}

inputmonth = int(input("Enter a number (1-12): "))
febwoa = 2

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

if inputmonth in monthsbeam:
    print(f"The month {inputmonth} has {monthsbeam[inputmonth]} days.")
else:
    print("Invalid! Please only enter a number from 1-12!")