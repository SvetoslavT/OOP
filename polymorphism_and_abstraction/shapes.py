import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def calculate_area(self):
        p = math.pi
        area = p * (self.radius ** 2)
        return area

    def calculate_perimeter(self):
        p = math.pi
        perimeter = 2 * p * self.radius
        return perimeter


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * self.height + 2 * self.width


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
