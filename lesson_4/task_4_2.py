from random import randint

my_list = []
for i in range(0, 26):
    my_list.append(randint(1, 300))
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]

print(f"Original list: {my_list}\nNew list :{new_list}")