from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance): pass
class Bus(Transport):
    def calculate_fare(self, distance): return distance * 2
class Train(Transport):
    def calculate_fare(self, distance): return distance * 1.5
class Taxi(Transport):
    def calculate_fare(self, distance): return 50 + distance * 12
class Flight(Transport):
    def calculate_fare(self, distance): return 1500 + distance * 5
for t in [Bus(), Train(), Taxi(), Flight()]:
    print(type(t).__name__, "fare for 100 km: ₹", t.calculate_fare(100))
