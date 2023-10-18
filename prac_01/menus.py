"""
CP1404/CP5632 - Practical
Simple menu driven program
"""
name = input("Enter name: ")

print("(H)ello ")
print("(G)oodbye ")
print("(Q)uit ")
user_choice = input(">>> ").upper()

while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello, {name}")
    elif user_choice == "G":
        print(f"Goodbye, {name}")
    else:
        print("Invalid Choice!")

    print("(H)ello ")
    print("(G)oodbye ")
    print("(Q)uit ")
    user_choice = input(">>> ").upper()

print("Finished.")