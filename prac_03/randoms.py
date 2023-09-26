"""
CP1404/CP5632 - Practical 03
Randoms

"""
import random

# 1. What did you see on line 1? What was the smallest number you could have seen, what was the largest?
# Line 1 printed values between 5 and 20. The smallest number could have been 5 and the largest could have been 20

# 2. What did you see on line 2? Could line 2 have produced a 4? Line 2 printed values between 3 and 10 in steps of
# 2, therefore it could not have produced a 4 as it did not follow the step pattern

# 3. What did you see on line 3? What was the smallest number you could have seen? What was the largest?
# The code printed a random floating number. The smallest number could have been 2.5,
# largest, 5.5

random_number = random.randint(1, 100)
