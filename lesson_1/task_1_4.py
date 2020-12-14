a = int(input('Enter a positive integer: '))
i = a % 10
a = a // 10
while a > 0:
    if a % 10 > i:
        i = a % 10
    a = a // 10
print(i)
