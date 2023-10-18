"""
CP1404/CP5632 Practical 04
List exercises
"""
NUMBER_OF_INPUTS = 5

# Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
numbers = []
for i in range(0, NUMBER_OF_INPUTS):
    number_input = int(input("Number: "))
    numbers.append(number_input)

average = sum(numbers) / len(numbers)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username_input = input("Username: ")
if username_input in usernames:
    print("Access granted")
else:
    print("Access denied")
