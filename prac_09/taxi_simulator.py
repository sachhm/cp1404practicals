"""
CP1404/CP5632 Practical
Taxi Simulator
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi


def main():
    print("Let's drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>>").upper()

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    bill_to_date = 0

    while menu_choice != "Q":
        if menu_choice == "C":
            display_taxis(taxis)
            current_taxi = get_valid_taxi(taxis)
        elif menu_choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi first.")
            else:
                current_fare = drive_taxi(current_taxi)
                bill_to_date += current_fare
                print(f"Your {current_taxi.name} trip cost you ${current_fare:.2f}")
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>>").upper()

    print("Taxis are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(taxi):
    distance = int(input("Drive how far?"))
    taxi.start_fare()
    taxi.drive(distance)
    cost = taxi.get_fare()
    return cost


def get_valid_taxi(taxis):
    try:
        taxi_choice = int(input("Choose taxi "))
        if taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None


main()
