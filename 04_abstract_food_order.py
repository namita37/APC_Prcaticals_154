from abc import ABC, abstractmethod
class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self): pass
    @abstractmethod
    def delivery_charge(self): pass
class RestaurantOrder(FoodOrder):
    def __init__(self, amount): self.amount = amount
    def calculate_bill(self): return self.amount
    def delivery_charge(self): return 0
class HomeDeliveryOrder(FoodOrder):
    def __init__(self, amount): self.amount = amount
    def calculate_bill(self): return self.amount + self.delivery_charge()
    def delivery_charge(self): return 40 if self.amount < 500 else 0
for o in [RestaurantOrder(350), HomeDeliveryOrder(350), HomeDeliveryOrder(650)]:
    print("Bill:", o.calculate_bill(), "| Delivery:", o.delivery_charge())
