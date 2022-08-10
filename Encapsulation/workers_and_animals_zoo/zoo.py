from wild_cat_zoo.animal import Animal
from wild_cat_zoo.caretaker import Caretaker
from wild_cat_zoo.cheetah import Cheetah
from wild_cat_zoo.keeper import Keeper
from wild_cat_zoo.lion import Lion
from wild_cat_zoo.tiger import Tiger
from wild_cat_zoo.vet import Vet
from wild_cat_zoo.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) < self.__animal_capacity and price > self.__budget:
            return f"Not enough budget"
        elif len(self.animals) == self.__animal_capacity and price <= self.__budget:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker.name} the {worker.__class__.__name__} fired successfully"

            return f"There is no {worker.name} in the zoo"

    def pay_workers(self):
        worker_salary_sum = sum([worker.salary for worker in self.workers])
        if self.__budget >= worker_salary_sum:
            self.__budget -= worker_salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        if self.__budget >= sum([animal.money_for_care for animal in self.animals]):
            self.__budget -= sum([animal.money_for_care for animal in self.animals])
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = [repr(ln) for ln in self.animals if isinstance(ln, Lion)]
        tigers = [repr(t) for t in self.animals if isinstance(t, Tiger)]
        cheetahs = [repr(c) for c in self.animals if isinstance(c, Cheetah)]

        return f"You have {len(self.animals)} animals" + "\n" + \
               f"----- {len(lions)} Lions:" + "\n" + \
               '\n'.join(lions) + "\n" + \
               f"----- {len(tigers)} Tigers:" + "\n" + \
               '\n'.join(tigers) + "\n" + \
               f"----- {len(cheetahs)} Cheetahs:" + "\n" + \
               '\n'.join(cheetahs) + "\n"

    def workers_status(self):
        caretakers = [repr(ln) for ln in self.workers if isinstance(ln, Caretaker)]
        vets = [repr(t) for t in self.workers if isinstance(t, Vet)]
        keepers = [repr(c) for c in self.workers if isinstance(c, Keeper)]

        return f"You have {len(self.workers)} workers" + "\n" + \
               f"----- {len(keepers)} Keepers:" + "\n" + \
               '\n'.join(keepers) + "\n" + \
               f"----- {len(caretakers)} Caretakers:" + "\n" + \
               '\n'.join(caretakers) + "\n" + \
               f"----- {len(vets)} Vets:" + "\n" + \
               '\n'.join(vets) + "\n"
