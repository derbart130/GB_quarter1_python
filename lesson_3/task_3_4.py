def my_func(x, y):
    if x < 0:
        print("'x' must be positive,")
    elif y >= 0:
        print("'y' must be a negative integer!")
    else:
        return x ** y


dig_1 = float(input("Enter digit: "))
dig_2 = int(input("Enter negative integer: "))

print(f"{my_func(dig_1, dig_2):.10f}")
