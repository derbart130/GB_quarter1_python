seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
while True:
    month = int(input("Enter the month number: "))
    if month > 12:
        print("You enter wrong month number.")
        continue
    if month == 1 or month == 2 or month == 12:
        print(seasons[0])
        break
    elif 3 <= month <= 5:
        print(seasons[1])
        break
    elif 6 <= month <= 8:
        print(seasons[2])
        break
    elif 9 <= month <= 11:
        print(seasons[3])
        break

