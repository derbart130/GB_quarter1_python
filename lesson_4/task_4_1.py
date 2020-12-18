#from sys import argv

#file_name, worked_hour, rate, benefit = argv

#calculation = (int(worked_hour) * int(rate)) + int(benefit)
#print(f"Your pay is equal {calculation}")

from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')