class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Input number and press Enter - '))
                self.my_list.append(val)
                print(f'Current list - {self.my_list} \n ')
            except:
                print(f"Invalid value - 'str' or 'bool'")
                to_be_continued = input(f'Try again? Y/N ')
                if to_be_continued.lower() == 'y':
                    print(try_except.my_input())
                elif to_be_continued.lower() == 'n':
                    return f'Finish'
                else:
                    return f'Finish'


try_except = Error(1)
print(try_except.my_input())