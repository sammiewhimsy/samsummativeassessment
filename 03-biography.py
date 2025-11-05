# 3 — Biography

bioinfo = {'Name': 'Sam Cabiad', 'Hometown': 'Philippines', 'Age': 18}
# Stored information in key-value dictionary.
for key, value in bioinfo.items():
    print(f"{key}: {value}")
# Using items() method to return the list as tuples.

# (The advanced  requirements one but i'm actually not good at this)
namewoah = str(input("Enter name: "))
hometownwoah = str(input("Enter hometown: "))
agewoah = (input("Enter age: "))
# Variables for user input.
try:
    agewoaw = int(agewoah)
except ValueError:
    print("Please enter the number itself next time!")
# Whenever anything that isn't a integer is entered, a ValueError is prompted.
# To fix the issue, I used a ValueError exception to inform the user that the function received an invalid value.
