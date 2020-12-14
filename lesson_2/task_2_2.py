num_of_items = int(input("Enter the number of list items: "))
my_list = []
i = 0
while i < num_of_items:
    my_list.append(input("Enter the following list value: "))
    i += 1
el = 0
for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)
