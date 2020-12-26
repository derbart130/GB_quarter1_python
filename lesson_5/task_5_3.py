my_list = {'John Smith': 21300,
           'Ivan Drago': 17600,
           'Rokky Balboa': 64700,
           'John Nollan': 35400,
           'Gregory House': 13550
           }
file_obj = open("test_3.txt", 'w', encoding='utf-8')
for name, salary in my_list.items():
    file_obj.write(name + ':' + str(salary) + "\n")
with open("test_3.txt", "r") as file_obj:
    my_dict = {line.split(':')[0]: float(line.split(':')[1]) for line in file_obj}
    print(f"Low salary (<20000): {[el[0] for el in my_dict.items() if el[1] < 20000]}")
    print(f"Average salary = {round(sum(my_dict.values()) / len(my_dict), 2)}")
