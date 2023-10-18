"""
CP1404/CP5632 Practical 05
Emails
Estimate: 25 minutes
Actual: 36 minutes
"""


def main():
    """Main program to store users emails and names in a dictionary"""
    email_to_name = {}
    email = input("Email: ").lower()
    while email != "":
        name = extract_name(email)

        name_check = input(f"Is your name {name}? (Y/n) ").lower()

        if name_check != "" and name_check != "y":
            name = input("Name: ")
        email_to_name[email] = name

        email = input("Email: ").lower()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from a given email"""
    name = email.split("@")
    name = name[0]
    name = name.replace(".", " ")

    return name.title()


main()
