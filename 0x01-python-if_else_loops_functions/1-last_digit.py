#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_nos = abs(number) % 10
if number < 0:
    last_nos = -last_nos
if last_nos < 6 and last_nos != 0:
    print(f"Last digit of {number} is {last_nos} and is less than 6 and not 0")
elif last_nos == 0:
    print(f"Last digit of {number} is {last_nos} and is 0")
else:
    print(f"Last digit of {number} is {last_nos} and is greater than 5")
