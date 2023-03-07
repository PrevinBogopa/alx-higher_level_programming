#!/usr/bin/python3
import random
number = random.randint(-10, 10)
name=""
if number > 0:
    name="is positive"
elif number == 0:
    name="is zero"
else :
    name="is negative"
print(number,name,end="\n")
