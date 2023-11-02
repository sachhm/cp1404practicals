"""
CP1404/CP5632 Practical
Project Management

Estimated: 2 hours
Actual:

"""
import datetime

from prac_07.project import Project

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
    filename = "projects.txt"
    projects = load_projects(filename)

    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        incomplete_projects, completed_projects = sort_project_completion_status(projects)
        if menu_choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif menu_choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif menu_choice == "D":
            display_projects(incomplete_projects, completed_projects)
        elif menu_choice == "F":
            filter_projects_by_date(projects)
        elif menu_choice == "A":
            add_new_project(projects)
        elif menu_choice == "U":
            update_project(projects)
        else:
            print("Invalid input, please try again")
        print(MENU)
        menu_choice = input(">>>").upper()
    save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a given filename"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip("\n")
            parts = line.split("\t")
            project_start_date = datetime.datetime.strptime(parts[PROJECT_DATE_INDEX], "%d/%m/%Y").date()
            project = Project(parts[PROJECT_NAME_INDEX], project_start_date, parts[PROJECT_PRIORITY_INDEX],
                              float(parts[PROJECT_EST_COST_INDEX]), int(parts[PROJECT_COMPLETION_INDEX]))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to a given filename"""
    with open(filename, "w") as out_file:
        out_file.write("")  # clear file before new inputs
        out_file.write(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            project.start_date = project.start_date.strftime("%d/%m/%Y")
            line = (f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                    f"{project.completion_percentage}\n")
            out_file.write(line)


def get_valid_number_input(prompt, error_message, threshold):
    is_valid_input = False
    while not is_valid_input:
        try:
            num_input = float(input(prompt))
            if num_input < threshold:
                print(error_message)
            else:
                is_valid_input = True
                return num_input
        except ValueError:
            print("Invalid (not an float)")


def get_valid_date_input(prompt, error_message):
    is_valid_input = False
    while not is_valid_input:
        try:
            date_input = input(prompt)
            date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
            is_valid_input = True
            return date
        except ValueError:
            print(error_message)


def display_projects(incomplete_projects, completed_projects):
    """Display incomplete and complete projects, sorted by priority"""
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"\t{project}")


def sort_project_completion_status(projects):
    """Sort the projects by complete and incomplete"""
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]
    return incomplete_projects, completed_projects


def filter_projects_by_date(projects):
    """Return a list of projects sorted by date that start after a given date"""
    cutoff_date = get_valid_date_input("Show projects that start after date (dd/mm/yy): ",
                                       "Not a valid date, please try again")

    filtered_projects = [project for project in projects if project.start_date >= cutoff_date]

    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Add a new project to memory given inputs"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_valid_date_input("Start date (dd/mm/yy): ", "Invalid format, please try again")
    print(type(start_date))
    priority = get_valid_number_input("Priority: ", "Cannot have negative priority number", 0)
    cost_estimate = get_valid_number_input("Cost estimate: $", "Cannot have negative cost", 0)
    completion_percentage = get_valid_number_input("Percent complete: ", "Cannot have negative percentage", 0)
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Modify completion or priority of an established project"""
    for project in projects:
        print(f"{projects.index(project)} {project}")

    project_choice_index = int(input("Project choice: "))
    chosen_project = projects[project_choice_index]
    print(chosen_project)
    new_percentage = input("New percentage: ")
    new_priority = input("New priority: ")

    if new_percentage != "":
        chosen_project.completion_percentage = int(new_percentage)
    if new_priority != "":
        chosen_project.priority = int(new_priority)


main()
