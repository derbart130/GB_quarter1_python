my_list = []
while True:
    string = input("Enter anything: ")
    if string == '':
        print(my_list)
        exit()
    else:
        newline = string + '\n'
        my_list.append(newline)

    with open("test_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)
