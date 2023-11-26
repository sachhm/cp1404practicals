"""
CP1404/CP5632 Practical
Project

Estimated: 2 hour
Actual:
"""
from datetime import datetime


class Project:
    """Represent a Project"""

    def __init__(self, name="", start_date=datetime, priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise a Project"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return Project details in a formatted string"""
        return (
            f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, estimate: "
            f"${self.cost_estimate:}, completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return Project details in a formatted string for lists"""
        return (f"{self.name}, start:{self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Return whether the Project's start date is before another start date"""
        return self.start_date < other.start_date

    def is_complete(self):
        """Return whether a Project is complete"""
        return self.completion_percentage == 100
