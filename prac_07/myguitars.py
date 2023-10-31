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
in_file.readline()
reader = csv.reader(in_file)  # use default dialect, Excel
for row in reader:
    guitar = Guitar(row[0], int(row[1]), float(row[2]))
    guitars.append(guitar)
in_file.close()

# Sort guitars
guitars.sort()

# Display using a loop
for guitar in guitars:
    print(guitar)

