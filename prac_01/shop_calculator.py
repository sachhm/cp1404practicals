"""
CP1404/CP5632 - Practical A shop requires a small program that would allow them to quickly work out the total
price for a number of items, each with different prices.
"""

number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
    
total_price = 0

for item in range(0, number_of_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price -= total_price * .10
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
