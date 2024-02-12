import re


pattern = r'^#[0-9a-fA-F]{6}$'

z = input("Enter a hex color codes:")


if re.match(pattern, z):
    print(z)
else:
    print("invalid entry")