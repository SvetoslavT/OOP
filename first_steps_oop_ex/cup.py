class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def status(self):
        return f"{self.size - self.quantity}"

    def fill(self, amount):
        if self.size - self.quantity >= amount:
            self.quantity += amount
            return self.quantity



cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
