class Guns:
    def __init__(self, ammunition: list):
        self.ammunition = ammunition

    @classmethod
    def pistol_ammo(cls):
        return cls(["45 cal.", "50 cal. DE", "12mm MAC"])

    @classmethod
    def ar_ammo(cls):
        return cls(["335 cal.", "50 cal.", "Elephant 39 cal."])

    def __repr__(self):
        for cal in self.ammunition:
            print(cal)


print(Guns.pistol_ammo())
