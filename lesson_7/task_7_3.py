class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.quantity // rows)]) + '\n' + '*' * (self.quantity % rows)

    def __str__(self):
        return f'Result: {self.quantity}'

    def __add__(self, other):
        return f'Sum of cells = {self.quantity + other.quantity}'

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 \
            else print('There are fewer cells in the first cell than in the second! Subtraction is not possible!')

    def __mul__(self, other):
        return f'Multiply of cells = {self.quantity * other.quantity}'

    def __floordiv__(self, other):
        return f'Floordiv of cells = {round(self.quantity // other.quantity)}'


cells1 = Cell(54)
cells2 = Cell(69)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells1 * cells2)
print(cells2.make_order(6))
print(cells1.make_order(9))
print(cells1 // cells2)
