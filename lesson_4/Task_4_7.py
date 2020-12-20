from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


gen = fact()
x = 0
stop = int(input("Enter number of iterations: "))
for i in gen:
    if x < stop:
        print(i)
        x += 1
    else:
        break
