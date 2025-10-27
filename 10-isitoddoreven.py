def inputyaya():
    while True:
        try:
            x = (int(input("Enter a number: ")))
            return x
        except ValueError:
            print("Invalid. Please enter an integer.")

def evenorodd(numnum):
    if numnum % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def main():
    numnum = inputyaya()
    boombayeah = evenorodd(numnum)
    print(f"The number {numnum} is an {boombayeah} number.")
    
if __name__ == '__main__':
    main()