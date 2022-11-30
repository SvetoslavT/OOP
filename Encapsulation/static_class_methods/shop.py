class Shop:
    def __init__(self, name, shop_type, capacity):
        self.name = name
        self.shop_type = shop_type
        self.capacity = capacity
        self.items = {}

    def __repr__(self):
        return f"{self.name} of type {self.shop_type} with capacity {self.capacity}"

    @classmethod
    def small_shop(cls, name, shop_type):
        return cls(name, shop_type, capacity=10)

    def add_item(self, item_name):
        if len(self.items) == self.capacity:
            return "Not enough capacity in the shop"
        if item_name in self.items.keys():
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        else:
            self.items[item_name] = 1
            return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items.keys():

            if self.items[item_name] >= amount:
                self.items[item_name] -= amount
                if self.items[item_name] == 0:
                    del self.items[item_name]
                return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
