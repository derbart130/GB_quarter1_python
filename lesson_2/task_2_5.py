my_list = [6, 4, 4, 3, 2]
print(f"Current rating: {my_list}")
while True:
    digit = int(input("Enter number (to exit enter 111): "))
    if digit != 111:
        i = 0
        for n in my_list:
            if digit <= n:
                i += 1
        my_list.insert(i, float(digit))
        print(f"Сurrent rating - {my_list}")
    else:
        break
