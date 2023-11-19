"""
CP1404/CP5632 Practical
Unreliable Car Test
"""
import random

from car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        Only drive the car if a randomly generated value is less than the car's reliability
        """
        reliability_tester = random.randint(0, 100)
        print(reliability_tester)
        if reliability_tester >= self.reliability:
            distance = 0
        super().drive(distance)
        return distance
