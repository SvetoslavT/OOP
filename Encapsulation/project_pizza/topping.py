class Topping:
    def __init__(self, topping_type, weight):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping(self):
        return self.topping_type

    @topping.setter
    def topping(self, value):
        if not value: raise ValueError("The topping type cannot be an empty string")
        self.topping_type = value

    @property
    def weight_num(self):
        return self.weight

    @weight_num.setter
    def weight_num(self, value):
        if value <= 0: raise ValueError("The weight cannot be less or equal to zero")
        self.weight = value

