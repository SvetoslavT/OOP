# Polymorphism with Inheritance

class Gun:

    @staticmethod
    def warning():
        return "GUNS ARE DANGEROUS"

    def shoot(self):
        return "Shooting the gun"


class AssaultRifle(Gun):
    def shoot(self):
        return "Shooting the AR"


class Pistol(Gun):
    def shoot(self):
        return "Shooting the pistol"


def shoot_func(obj):
    print(obj.warning())
    print(obj.shoot())


obj1 = Gun()
obj2 = AssaultRifle()
obj3 = Pistol()

shoot_func(obj1)
shoot_func(obj2)
shoot_func(obj3)
