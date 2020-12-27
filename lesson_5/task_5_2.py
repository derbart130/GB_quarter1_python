with open("test_2.txt") as file_obj:
    my_line = file_obj.readlines()
    for line, words in enumerate(my_line, 1):
        num_of_words = len(words.split())
        print(f"{num_of_words} words in line {line}")
    print(f"\nNumber of lines = {line}")
