my_dict = {}
with open("test_6.txt", encoding="utf-8") as my_file:
    for line in my_file:
        discipline, duration = line.split(":")
        disc_duration = sum(map(int, "".join([i for i in duration if i == ' ' or '0' <= i <= '9']).split()))
        my_dict[discipline] = disc_duration
print(f"{my_dict}")
