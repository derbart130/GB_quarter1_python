my_list = ['Nemo enim ipsam voluptatem\n',
           'Itaque earum rerum hic tenetur a sapiente delectus\n',
           'Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet\n',
           'Sed ut perspiciatis, qui in ea voluptate velit esse\n',
           'Sed ut perspiciatis\n'
           ]
with open("test_2.txt", 'w+', encoding="utf-8") as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    my_line = file_obj.readlines()
    for line, words in enumerate(my_line, 1):
        num_of_words = len(words.split())
        print(f"{num_of_words} words in line {line}")
    print(f"\nNumber of lines = {line}")
