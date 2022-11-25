class Car:

    def __init__(self, brand: str, max_speed: int):
        self.brand = brand
        self.__max_speed = max_speed

    def drive(self):
        return f"Max speed: {self.max_speed}"

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value > 140:
            value = 140
            self.__max_speed = value


red_car = Car("BMW", 200)
red_car.drive()
red_car.max_speed = 512
red_car.drive()
print(red_car.brand)
