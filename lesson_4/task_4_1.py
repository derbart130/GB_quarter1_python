from sys import argv

file_name, worked_hour, rate, benefit = argv

result = (int(worked_hour) * int(rate)) + int(benefit)

print(f"Your estimated salary {result}")