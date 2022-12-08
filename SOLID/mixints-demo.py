class Machine:
    def __int__(self, brand):
        self.brand = brand


class Radio:
    def __int__(self, name):
        self.name = name

    @staticmethod
    def play_frequency(frequency):
        return f"Playing {frequency} frequency"


class Car(Machine, Radio):
    def __int__(self, brand):
        super().__int__(brand)

    def __str__(self):
        return f"Brand: {self.brand}"


obj1 = Car()
print(obj1.name)
print(obj1.play_frequency(4883.1))
