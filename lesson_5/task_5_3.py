my_list = {'John Smith': 21300,
           'Ivan Drago': 17600,
           'Rokky Balboa': 64700,
           'John Nollan': 35400,
           'Gregory House': 13550
           }
file_obj = open("test_3.txt", 'w')
for name, salary in my_list.items():
    file_obj.write(name + ':' + str(salary) + "\n")
total = 0
count = 0
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        total += int(tokens[1])
        count += 1
result = total / count
print(f"Low salary (<20000): {persons}")
print(f"Average salary: {result}")
