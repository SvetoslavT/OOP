from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, amount):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption_per_km):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.fuel_consumption_per_km += 0.9

    def drive(self, distance):
        fuel_needed = distance * self.fuel_consumption_per_km
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, amount):
        self.fuel_quantity += amount


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption_per_km):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.fuel_consumption_per_km += 1.6

    def drive(self, distance):
        fuel_needed = distance * self.fuel_consumption_per_km
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, amount):
        self.fuel_quantity += amount * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
