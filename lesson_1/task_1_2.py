print('Hello')
a = int(input('Enter time in seconds: '))
hours = a // 3600
minutes = (a % 3600) // 60
seconds = a % 60
print(f'Result: {hours:02}:{minutes:02}:{seconds:02}')
