from itertools import cycle


def fill_my_list(el):
    my_list = []
    for i in range(el):
        my_list.append(input("Enter list item: "))
    return my_list


def my_func(list_, iteration):
    i = 0
    iter = cycle(list_)
    while i < iteration:
        print(next(iter))
        i += 1


el = int(input("Enter number of list elements: "))

my_func(fill_my_list(el), iteration=int(input("Enter number of iterations: ")))
