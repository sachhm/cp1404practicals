"""
CP1404/CP5632 Practical 04
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    data = format_subject_details(data)
    print_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_details.append(parts)
    input_file.close()

    return subject_details


def format_subject_details(subject_details):
    formatted_subject_details = []
    for subject in subject_details:
        statement = f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students"
        formatted_subject_details.append(statement)
    return formatted_subject_details


def print_subject_details(formatted_subject_details):
    for subject in formatted_subject_details:
        print(subject)


main()
