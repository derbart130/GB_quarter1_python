num_of_items = int(input("Enter the number of list items: "))
my_list = []
item = 0
while item < num_of_items:
    my_list.append(input("Enter the following list value: "))
    item += 1
print(f"Current list: {my_list}")
for i in range(1, num_of_items, 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i-1]
print(f"Result: {my_list}")
