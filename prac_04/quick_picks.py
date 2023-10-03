"""
CP1404/CP5632 Practical 04
Quick picks
"""
import random

NUMBER_OF_RANDOM_INTEGERS = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_picks = int(input("How many quick picks? "))
random_integers = []

for i in range(0, number_of_quick_picks):
    for j in range(0, NUMBER_OF_RANDOM_INTEGERS):
        generated_integer = random.randint(MINIMUM, MAXIMUM)
        if generated_integer in random_integers:
            generated_integer = random.randint(MINIMUM, MAXIMUM)

        random_integers.append(generated_integer)

    random_integers.sort()

    for random_integer in random_integers:
        print(f"{random_integer:>2}", end=" ")
    print()

    random_integers.clear()
