class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def intake(self, thickness):
        weigth = 25
        intake = self.__length * self.__width * weigth * thickness / 1000
        print(f'Need {intake} ton for the building')


road_to_village = Road(20000, 6)
road_to_village.intake(0.06)
