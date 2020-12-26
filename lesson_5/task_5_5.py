from random import randint

with open("test_5.txt", "w", encoding="utf-8") as my_file:
    my_list = [randint(1, 256) for _ in range(128)]
    my_file.write(" ".join(map(str, my_list)))

print(f"Sum of elements = {sum(my_list)}")