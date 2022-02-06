"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    cargo = 0

    def load_cargo(self, massa):
        if (self.cargo+massa) > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += massa

    def remove_all_cargo(self):
        cargo_before_remove = self.cargo
        self.cargo = 0
        return cargo_before_remove



