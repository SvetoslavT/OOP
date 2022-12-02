# user-defined polymorphic functions
# def add(*args):
#     return [x for x in args]
#
#
# l1 = 1
# l2 = 2
# l3 = 3
# l4 = 4
# l5 = 5
# print(add(l1, l2, l3, l4, l5))
# print(add(l1, l3, l5, l4, l5))

# Polimorphism with class methods

class Pistol:
    def shoot(self):
        return "Shooting the pistol"

    def reload(self):
        return "Reloading the pistol"


class AssaultRifle:
    def shoot(self):
        return "Shooting the AR"

    def reload(self):
        return "Reloading the AK"


pistol_obj = Pistol()
rifle_obj = AssaultRifle()

for obj in pistol_obj, rifle_obj:
    print(obj.shoot())
    print(obj.reload())