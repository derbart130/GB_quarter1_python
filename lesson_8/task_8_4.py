class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)


class Equipment:
    def __init__(self, model, price, quantity):
        self.model = model
        self.price = price
        self.quantity = quantity
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.model} {self.price} {self.quantity}'


class Printer(Equipment):
    def __init__(self, model, series, price, quantity):
        super().__init__(model, price, quantity)
        self.series = series

    def __repr__(self):
        return f'{self.model} {self.series} {self.price} {self.quantity}'


class Scaner(Equipment):
    def __init__(self, model, price, quantity):
        super().__init__(model, price, quantity)


class Xerox(Equipment):
    def __init__(self, model, price, quantity):
        super().__init__(model, price, quantity)


sklad = Sklad()
scaner = Scaner('hp', 2500, 90)
sklad.add_to(scaner)
xerox = Xerox('epson', 2450, 72)
sklad.add_to(xerox)
scaner = Scaner('canon', 2750, 25)
sklad.add_to(scaner)
printer = Printer('canon', 'mp-210', 6700, 13)
sklad.add_to(printer)
print(sklad._dict)
