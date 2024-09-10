#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last_digit = int(number[-1])
print(f"The last digit of {number} is {last_digit}", end=" ")
if last_digit == 0:
    print("and is zero")
elif last_digit < 6:
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")
