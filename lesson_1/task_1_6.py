while True:
    start = int(input('Enter first day result: '))
    finish = int(input('Enter the desired result: '))
    i = 1
    if start <= 0 or finish <= 0:
        print('Error. Enter correct values!')
        continue
    while start < finish:
        start = start + start * 0.1
        i += 1
    print(f'You will achieve the result on day: {i}')
    break
