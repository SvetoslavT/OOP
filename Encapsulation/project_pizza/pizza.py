from dough import Dough
from topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, topping_capacity: int):
        self.name = name
        self.dough = dough
        self.topping_capacity = topping_capacity
        self.toppings = dict()

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.topping_capacity:
            raise ValueError("Not enough space for another topping")
        if topping in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = 0
        total_weight += self.dough.weight
        for topping in self.toppings.values():
            total_weight += topping
        return total_weight



