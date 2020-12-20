from functools import reduce


def my_func(a_1, a_2):
    return a_1 * a_2


my_list = []
for el in range(100, 1001, 2):
    my_list.append(el)

print(reduce(my_func, my_list))
