print("Enter your personal information: ")
name = input('Enter name: ')
surname = input('Enter surname: ')
year = int(input('Enter year of birth: '))
city = input('Enter city: ')
email = input('Enter email: ')
phone = input('Enter telephone: ')


def my_func(**kwargs):
    return kwargs


print(f"Your details:\n{my_func(Name=name, Surname=surname, Year=year, City=city, Email=email, Phone=phone)}")
