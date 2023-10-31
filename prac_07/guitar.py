"""
CP1404/CP5632 Practical
Guitar
"""
CURRENT_YEAR = 2023
VINTAGE_THRESHOLD = 50


class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar object

        name: str, name of the Guitar
        year: int, year of Guitar's release
        cost: float, cost of Guitar in dollars
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Guitar as string"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Return Guitar as string for list printing"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars by year"""
        return self.year < other.year

    def get_age(self):
        """Get age of Guitar given year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage given a threshold"""
        return self.get_age() > VINTAGE_THRESHOLD
