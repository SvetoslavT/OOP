from exercise.need_for_speed.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
    fuel_consumption = DEFAULT_FUEL_CONSUMPTION

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        fuel_needed = self.fuel_consumption * kilometers
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            return self.fuel
