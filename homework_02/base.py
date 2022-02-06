from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started==False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if (distance*self.fuel_consumption)>self.fuel:
            raise NotEnoughFuel()
        else:
            self.fuel -= distance*self.fuel_consumption


venicle = Vehicle(fuel=0)

#print(venicle.started)
#venicle.start()
#print(venicle.started)
