class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


divider = input("Enter divider: ")
denominator = input("Enter denominator: ")

try:
    divider = int(divider)
except ValueError:
    print("Enter only number, please!")

try:
    denominator = int(denominator)
    if denominator == 0:
        raise OwnError("You can't divide by zero!!!")
except ValueError:
    print("Enter only number, please!")
except OwnError as err:
    print(err)
else:
    print(f"Result = {divider / denominator}")
