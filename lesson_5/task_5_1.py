with open("test_1.txt", "w", encoding='utf-8') as file_1:
    while True:
        string = input("Enter anything or empty string for exit: ")
        if string == '':
            break
        print(string, file = file_1)


