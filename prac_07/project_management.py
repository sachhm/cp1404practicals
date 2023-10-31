"""
CP1404/CP5632 Practical
Project Management

Estimated: 2 hours
Actual:

"""
import datetime

PROJECT_NAME_INDEX = 0
PROJECT_DATE_INDEX = 1
PROJECT_PRIORITY_INDEX = 2
PROJECT_EST_COST_INDEX = 3
PROJECT_COMPLETION_INDEX = 4

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Main program for Project Management"""
    projects = []
    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            # filename = input("Filename: ")
            filename = "projects.txt"
            projects = load_projects(filename)
        elif menu_choice == "S":
            filename = input("Filename: ")
            save_projects(filename)
        elif menu_choice == "D":
            display_projects(projects)
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
        in_file.readline()
        for line in in_file:
            line = line.strip("\n")
            parts = line.split("\t")
            project = [parts[PROJECT_NAME_INDEX], parts[PROJECT_DATE_INDEX], parts[PROJECT_PRIORITY_INDEX],
                       parts[PROJECT_EST_COST_INDEX], parts[PROJECT_COMPLETION_INDEX]]
            projects.append(project)
    return projects


def save_projects(filename):
    """Save projects to a given filename"""
    pass


def display_projects(projects):
    """Display incomplete and complete projects, sorted by priority"""
    # TODO: FINISH THIS
    completed_projects = [project for project in projects if project[PROJECT_COMPLETION_INDEX]]
    print("Incomplete projects:")
    print("Completed projects:")


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
