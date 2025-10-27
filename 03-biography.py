# biography
bioinfo = {'Name': 'Sam Cabiad', 'Hometown': 'Philippines', 'Age': 18}
for key, value in bioinfo.items():
    print(f"{key}: {value}")

# biography (the advanced  requirements one but i'm actually not good at this)
namewoah = str(input("Enter name: "))
hometownwoah = str(input("Enter hometown: "))
agewoah = (input("Enter age: "))
try:
    agewoaw = int(agewoah)
except ValueError:
    agewoaw = agewoah
    print(f"Please enter the number itself next time!")