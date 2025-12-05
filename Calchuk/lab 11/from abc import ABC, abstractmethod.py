from abc import ABC, abstractmethod

# -------------------- Product --------------------
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> None:
        pass

class Truck(Transport):
    def deliver(self):
        print("Доставка вантажівкою 🚚")

class Ship(Transport):
    def deliver(self):
        print("Доставка кораблем 🚢")

# -------------------- Creator --------------------
class Logistic(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()

class RoadLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Ship()

# -------------------- Використання --------------------
if __name__ == "__main__":
    logistic = RoadLogistic()
    logistic.plan_delivery()

    logistic = SeaLogistic()
    logistic.plan_delivery()
