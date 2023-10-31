"""
CP1404/CP5632 Practical
My Guitars

Expected Time: 30 Minutes
Actual Time: Minutes
"""
import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

# Write a program to read all of these guitars and store them in a list of Guitar objects,
# using the class that you wrote recently.
guitars = []
in_file = open(FILENAME, 'r')
reader = csv.reader(in_file)  # use default dialect, Excel
for row in reader:
    guitar = Guitar(row[0], int(row[1]), float(row[2]))
    guitars.append(guitar)
in_file.close()

# Get guitars, store in list and write
name = input("Name: ")

while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("Name: ")

guitars.sort()

for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

out_file = open(FILENAME, 'w')
out_file.write("")
for guitar in guitars:
    guitar_to_write = f"{guitar.name},{guitar.year},{guitar.cost}"
    out_file.write(guitar_to_write + "\n")
#
# out_file.close()