class Vehicle:
    def __init__(self, distance, engine_size):
        self.distance = distance
        self.engine_size = engine_size

    def fuel_consumption(self):
        raise NotImplementedError


class RoadTransport(Vehicle):
    def fuel_consumption(self):
        return self.distance * 0.08 * self.engine_size

    def co2_emission(self):
        return self.fuel_consumption() * 2.68


class Ship(Vehicle):
    def fuel_consumption(self):
        return self.distance * 0.12 * self.engine_size

    def co2_emission(self):
        return self.fuel_consumption() * 3.10


class Airplane(Vehicle):
    def fuel_consumption(self):
        return self.distance * 0.18 * self.engine_size

    def co2_emission(self):
        return self.fuel_consumption() * 3.16
