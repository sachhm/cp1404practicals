"""
CP1404/CP5632 Practical
Silver Service Taxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness
        self.flagfall = 4.50

    def __str__(self):
        """Return a string like a Taxi but with a flagfall"""
        return super().__str__() + f" plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return fare plus flagfall"""
        return super().get_fare() + self.flagfall
