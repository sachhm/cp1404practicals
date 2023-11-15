"""
CP1404/CP5632 Practical - Pair Programming
Band class

- Eric Wagner
"""
from musician import Musician


class Band:
    def __init__(self, name=""):
        """ Initialise a Band"""
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} is playing {self.musicians}"

    def add(self, musician_name):
        """Add a musician"""
        new_musician = Musician(musician_name)
        self.musicians.append(new_musician)

    def play(self):
        play_string = ""
        for musician in self.musicians:
            play_string += f"{musician.play()}\n"

        return play_string
