from wild_cat_zoo.animal import Animal
from wild_cat_zoo.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, name: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(name)
            self.__budget -= price

            return f"{name.name} the {name.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > 0 and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return "There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_sum = 0
        for worker in self.workers:
            salaries_sum += worker.salary
        if salaries_sum <= self.__budget:
            self.__budget -= salaries_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_costs = 0
        # for price in ruun.prices:
        #     animals_costs += price
        for animal in self.animals:
            animals_costs += animal.money_for_care
        if animals_costs <= self.__budget:
            self.__budget -= animals_costs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        print(f"You have {len(self.animals)} animals:")
        for animal in self.animals:
            print("---")
            print(animal)

    def workers_status(self):
        names = {"Caretaker": [], "Vet": [], "Keeper": []}
        [names[x.__class__.__name__].append(str(x)) for x in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"--- {len(names['Keeper'])} Keepers:",
            *names["Keeper"],
            f"--- {len(names['Vet'])} Vets:",
            *names["Vet"],
            f"--- {len(names['Caretaker'])} Caretakers:",
            *names["Caretaker"],
        ]
        return "\n".join(result)
