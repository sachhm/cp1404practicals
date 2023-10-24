"""
CP1404/CP5632 Practical
Guitar Test

Expected Time: 10 Minutes
Actual Time: 4 Minutes
"""
from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
stratocaster = Guitar("Fender Stratocaster American Pro", 2021, 2510.28)

print(gibson)
print(f"Age: {gibson.get_age()}")  # Expected 101, got 101
print(f"Is Vintage: {gibson.is_vintage()}")  # Expected True, got True
print()
print(stratocaster)
print(f"Age: {stratocaster.get_age()}")  # Expected 2, got 2
print(f"Is Vintage: {stratocaster.is_vintage()}")  # Expected False, got False
