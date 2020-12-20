from random import randint

my_list = []
for el in range(1, 15):
    my_list.append(randint(1, 20))

print(f"Original list:\n{my_list}\nResult:\n{[el for el in my_list if my_list.count(el) < 2]}")
