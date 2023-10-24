"""
CP1404/CP5632 Practical
Programming Languages

Expected Time: 25 Minutes
Actual Time: 30 Minutes
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage Object"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a Programming Langauge Instance

        language_name: str, name of Programming Language
        typing: str, typing style of Programming Language
        year: int, year of Programming Language's first release
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
    def is_dynamic(self):
        """Return whether a Programming Language is Dynamic or not"""
        return self.typing == "Dynamic"
