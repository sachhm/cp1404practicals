"""
CP1404/CP5632 - Practical 03
Create a new file called files.py and do all the following separate questions in it
"""

# 1.
name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)

# 2.
with open("name.txt", "r") as in_file:
    name = in_file.read()
    print(f"Your name is {name}")

# 3.
with open("numbers.txt", "r") as file:
    num1 = float(file.readline().strip())
    num2 = float(file.readline().strip())
    print("Total of first two: ", num1 + num2)

# 4.
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += float(line.strip())
    print("Total of every number: ", total)
    