from exercise.shop.drink import Drink
from exercise.shop.food import Food
from exercise.shop.product import Product


class ProductRepository:
    all_products = []

    def add(self, product: Product):
        self.all_products.append(product)

    def find(self, product_name: str):
        for product in self.all_products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.all_products:
            if product.name == product_name:
                self.all_products.remove(product)

    def __iter__(self):
        for i in self.all_products:
            yield i

    def __repr__(self):
        for product in self.all_products:
            return f"{product.name}: {product.quantity}"
