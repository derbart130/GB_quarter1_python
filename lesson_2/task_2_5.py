my_list = [6, 4, 4, 3, 2]
print(f"Current rating: {my_list}")
while True:
    digit = int(input("Enter number from 0 to 99 (to exit enter 100): "))
    if digit != 100:
        for i in range(len(my_list)):
            if my_list[0] < digit:
                my_list.insert(0, digit)
            elif my_list[-1] > digit:
                my_list.append(digit)
            elif my_list[i] == digit:
                my_list.insert(i + 1, digit)
                break
        print(f"Сurrent rating - {my_list}")
    else:
        break
