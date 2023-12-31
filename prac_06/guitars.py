"""
CP1404/CP5632 Practical
Guitars

Expected Time: 40 Minutes
Actual Time:  20 Minutes
"""
from prac_06.guitar import Guitar

print("My guitars!")

guitars = []

name = input("Name: ")

while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("Name: ")

for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
