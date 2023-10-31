"""
CP1404/CP5632 Practical
Project

Estimated: 1 hour
Actual:
"""

class Project:
    """Represent a Project"""
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise a Project"""
        self.name = name
        self.start_date =  start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return Project details in a formatted string"""
        return (f"{self.name}, start:{self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}, "
                f"completion; {self.completion_percentage}%")
