my_list = ['Nemo enim ipsam voluptatem\n',
           'Itaque earum rerum hic tenetur a sapiente delectus\n',
           'Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet\n',
           'Sed ut perspiciatis, qui in ea voluptate velit esse\n',
           'Sed ut perspiciatis\n'
           ]
with open("test_2.txt", 'w+', encoding="utf-8") as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    words = 0
    for line in file_obj:
        lines += line.count("\n")
        words = len(line.split())
        print(f"{words} words in line {lines}")
    print(f"\nNumber of lines = {lines}")
