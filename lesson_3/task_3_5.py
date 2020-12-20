def my_sum():
    result = 0
    while True:
        dig = input('Enter the numbers separated by a space or Q for quit - ').split()
        for el in dig:
            if el.upper() == 'Q':
                return result
            else:
                try:
                    result += int(el)
                except ValueError:
                    print('Enter digit or Q for exit!')
        print(f'total = {result}')


print(my_sum())