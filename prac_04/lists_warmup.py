"""
CP1404/CP5632 - Practical 04
Lists warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

'''
numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = 2,9,5,1,4,1,3 -> Actually [3, 1, 4, 1, 5, 9]
numbers[3:4] = 1, 5 -> Actually just 1
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

Got everything except for numbers[:-1] and numbers[3:4]
'''
# 1.
numbers[0] = "ten"

# 2.
numbers[6] = 1

# 3.
print(numbers[:-2])

# 4.
print(9 in numbers)
