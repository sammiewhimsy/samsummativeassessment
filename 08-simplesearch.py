listofnames = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
huntthisguy = "Sam"
fella = huntthisguy in listofnames
print(f"{fella}, the name is {huntthisguy} a part of the list")
# Created a list of names.
# Created a variable for the specific name to be searched.
# Created a second variable to determine if Sam is a part of the list.
# Displayed the result, where "fella" is a boolean variable that confirms that Sam is in the list.

# I also created an alternate version using "if-else" with the "in" keyword as another way to check if Sam is in the list.
# The "huntthisguy" variable is still there to specify the name to be searched.

listofnames = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
huntthisguy = "Sam"

if huntthisguy in listofnames:
    print(f"{huntthisguy} is in the list.")
else:
    print(f"{huntthisguy} is not in the list.")
