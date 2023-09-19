"""
CP1404/CP5632 - Practical 2
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)

    random_result = random.randint(0, 100)
    result = get_result(random_result)
    print(f"Score: {random_result}, Result: {result}")


def get_result(score):
    result = ""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
