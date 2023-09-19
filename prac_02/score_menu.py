"""
CP1404/CP5632 - Practical 2
Score menu program
"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
"""


def main():
    score = get_valid_score(0, 100)

    print(MENU)
    choice = input(">> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(0, 100)
        elif choice == "P":
            result = get_result(score)
            print(f"Score: {score}, Result: {result}")
        elif choice == "S":
            stars = get_stars(score)
            print(stars)
        else:
            print("Invalid input")
        choice = input(">> ").upper()

    print("Farewell.")


def get_valid_score(low, high):
    score = int(input("Enter score: "))
    while score < low or score > high:
        print("Invalid input")
        score = float(input("Enter score: "))
    return score


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


def get_stars(score):
    return "*" * score


main()
