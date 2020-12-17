def my_func(x_1, x_2, x_3):
    data = [x_1, x_2, x_3]
    try:
        data.remove(min(data))
    except TypeError:
        print("Enter only a numbers!")
    return sum(data)


digit_1 = int(input("Enter first digit: "))
digit_2 = int(input("Enter second digit: "))
digit_3 = int(input("Enter third digit: "))
print(f'Result = {my_func(digit_1, digit_2, digit_3)}')
