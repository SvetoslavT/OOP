class Flower:

    def __init__(self, name, water_requierments):
        self.name = name
        self.water_requierments = water_requierments
        self.is_happy = False

    def water(self, amount):
        self.is_happy = amount >= self.water_requierments

    def status(self):
        if self.is_happy:

            return f"The {self.name} is happy"
        else:
            return f"The {self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
