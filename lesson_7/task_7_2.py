from abc import ABC, abstractmethod


class Textil(ABC):
    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def expenditure(self):
        pass

    def __add__(self, other):
        return self.expenditure + other.expenditure


class Coat(Textil):
    @property
    def expenditure(self):
        print(f'Area of fabric on the coat = {round(self.size / 6.5) + 0.5}')
        return round(self.size / 6.5) + 0.5


class Jacket(Textil):
    @property
    def expenditure(self):
        print(f'Area of fabric on the jacket {round((2 * self.size + 0.3) / 100, 3)}')
        return (2 * self.size + 0.3) / 100


coat = Coat(56)
jacket = Jacket(183)

print(coat + jacket)