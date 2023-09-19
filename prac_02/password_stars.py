"""
CP1404/CP5632 - Practical 2
Password Stars
"""

MIN_LENGTH = 8


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print(f"Minimum password length is {MIN_LENGTH} characters. Please try again")
        password = input("Password: ")
    return password


main()
