class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25
    fuel_consumption = DEFAULT_FUEL_CONSUMPTION

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        fuel_needed = self.fuel_consumption * kilometers
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            return self.fuel
