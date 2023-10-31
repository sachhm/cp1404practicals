"""
CP1404/CP5632 Practical
Project Management

Estimated: 1 hour
Actual:

"""

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Main program for Project Management"""
    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            # filename = input("Filename: ")
            filename = "projects.txt"
            print(load_projects(filename))
        elif menu_choice == "S":
            filename = input("Filename: ")
            save_projects(filename)
        elif menu_choice == "D":
            pass
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            pass
        else:
            print("Invalid input, please try again")
        print(MENU)
        menu_choice = input(">>>").upper()

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a given filename"""
    projects = []
    with open(filename, "r") as in_file:
        for line in in_file:
            line.split("\t")
            projects.append(line)
    return projects


def save_projects(filename):
    """Save projects to a given filename"""
    pass


def dispay_projectS():
    """Display incomplete and complete projects, sorted by priority"""
    pass


def filter_projects_by_date(date):
    """Return a list of projects sorted by date that start after a given date"""
    pass


def add_new_project():
    """Add a new project to memory given inputs"""
    pass


def update_project():
    """Modify completion or priority of an established project"""
    pass


main()
