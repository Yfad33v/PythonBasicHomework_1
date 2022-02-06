"""
создайте класс `Car`, наследник `Vehicle`
"""
from engine import Engine
from homework_02.base import Vehicle


class Car(Vehicle):
    engine: Engine = None

    def set_engine(self, motor: Engine):
        self.engine = motor

