class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'{self.name} current speed is {self.speed}'

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'
        else:
            return f'Speed of {self.name} is normal for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


lambo = SportCar(150, 'Yellow', 'Lamborghini', False)
vw = TownCar(30, 'White', 'Volkswagen', False)
scania = WorkCar(70, 'Red', 'Scania', False)
chevi = PoliceCar(110, 'Black', 'Chevrolet', True)
print(f'{lambo.go()}\n{vw.go()}\n{scania.go()}\n{chevi.go()}')
print(lambo.show_speed())
print(vw.show_speed())
print(scania.show_speed())
print(chevi.show_speed())
print(f'When {chevi.turn_left()}, then {lambo.stop()}')
print(f'{scania.name} is {scania.color}')
print(lambo.police())
print(chevi.police())
