"""
CP1404/CP5632 Practical
Silver Service Taxi Runner
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 4)
print(hummer)

fancy_car = SilverServiceTaxi("Toyota 86", 100, 2)
fancy_car.drive(18)
print(f"For an 18km drive in a taxi with fanciness 2, the rate should be ${fancy_car.get_fare():.2f} (yikes!)")
