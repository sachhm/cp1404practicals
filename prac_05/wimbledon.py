"""
CP1404/CP5632 Practical 05
Wimbledon
Estimate: 20 minutes
Actual: 55 minutes
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Main program for processing and returning Wimbledon records"""
    records = load_records()
    champions, countries = process_data(records)
    display_information(champions, countries)


def load_records():
    """Load the records from CSV file"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # get rid of the first line
        for line in in_file:
            line = line.strip()
            line = line.split(",")
            records.append(line)
    return records


def process_data(records):
    """Process loaded records and return a set of countries and a dictionary of champions"""
    champions_to_num_of_wins = {}
    countries = set()
    for record in records:
        if record[CHAMPION_INDEX] in champions_to_num_of_wins:
            champions_to_num_of_wins[record[CHAMPION_INDEX]] += 1
        else:
            champions_to_num_of_wins[record[CHAMPION_INDEX]] = 1
        countries.add(record[COUNTRY_INDEX])
    return champions_to_num_of_wins, countries


def display_information(champions_to_num_of_wins, countries):
    """Print the champions and countries"""
    print("Wimbledon Champions:")
    for champion, number_of_wins in champions_to_num_of_wins.items():
        print(f"{champion} {number_of_wins}")
    print()

    # Print countries
    print("These 12 countries have won Wimbledon:")
    countries = sorted(countries)
    countries = ", ".join(countries)
    print(countries)


main()
