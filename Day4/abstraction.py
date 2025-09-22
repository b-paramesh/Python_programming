from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("started vehicle")
ca=car()
ca.start()