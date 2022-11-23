# Single Inheritance
class Food:
    def __init__(self, expiration_date):
        self.expiration_date = expiration_date

class Fruit(Food):
    def __init__(self, expiration_date, name):
        super().__init__(expiration_date)
        self.name = name
