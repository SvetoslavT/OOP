from exercise.shop.drink import Drink
from exercise.shop.food import Food
from exercise.shop.product_repository import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.all_products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
