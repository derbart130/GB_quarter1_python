print('Hello')
proceeds = int(input('Enter the proceeds value: '))
outlay = int(input('Enter the outlay value: '))
if proceeds > outlay:
    print('Сongratulations, you are in profit')
    profit = (proceeds - outlay) / proceeds
    print(f'Your profit = {profit:.2f}')
    staff = int(input('Enter number of staff: '))
    profit_staff = profit / staff
    print(f'Profit per employee = {profit_staff:.2f}')
elif proceeds < outlay:
    print('Sorry, you at a loss!')
else:
    print("You didn't earn anything!")
