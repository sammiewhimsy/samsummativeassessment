def inputyaya():
    while True:
        try:
            x = (int(input("Enter a number: ")))
            return x
        except ValueError:
            print("Invalid. Please enter an integer.")
# First function is for the user input and to check if the value is valid.
# When valid, the function will exit the program and return the value.
# When invalid (ValueError), it will prompt an invalid message and loop until the user enters an integer.
# While loop to loop until the condition is met.

def evenorodd(numnum):
    if numnum % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Second function checks if the entered number is odd or even.
# If the number is not divisible by 2, it will be odd.
    
def main():
    numnum = inputyaya()
    boombayeah = evenorodd(numnum)
    print(f"The number {numnum} is an {boombayeah} number.")
# "numnum" variable stores the user's input.
# "boombayeah" is the result after checking if the number is odd or even
# F-string used to directly embed both variables.
    
if __name__ == '__main__':
    main()

