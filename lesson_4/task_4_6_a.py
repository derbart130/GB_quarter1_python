from itertools import count


def my_func():
    start = int(input("Enter first number: "))
    stop = int(input("Enter last number: "))
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


my_func()