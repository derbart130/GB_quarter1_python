with open("test_3.txt", "r") as file_obj:
    my_dict = {line.split(':')[0]: float(line.split(':')[1]) for line in file_obj}
    print(f"Low salary (<20000): {[el[0] for el in my_dict.items() if el[1] < 20000]}")
    print(f"Average salary = {round(sum(my_dict.values()) / len(my_dict), 2)}")
