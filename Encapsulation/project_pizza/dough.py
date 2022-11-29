class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour(self):
        return self.flour_type

    @flour.setter
    def flour(self, value):
        if not value: raise ValueError("The flour type cannot be an empty string")
        self.flour_type = value
    
    @property
    def technique(self):
        return self.baking_technique
    
    @technique.setter
    def technique(self, value):
        if not value: raise ValueError("The baking technique cannot be an empty string")
        self.baking_technique = value

    @property
    def weight_validate(self):
        return self.weight

    @weight_validate.setter
    def weight_validate(self, value):
        if value <= 0: raise ValueError("The weight cannot be less or equal to zero")
        self.weight = value


