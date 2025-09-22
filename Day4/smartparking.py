class vehicle:
    def __init__(self,licence,username):
        self.__licence=licence
        self.__username=username
    def setlicence(self,licence):
        self.__licence=licence
    def getlicence(self):
        return self.__licence
    def setname(self,username):
        self.__username=username
    def getname(self):
        return self.__username
    def display(self):
        print(f"vehicle[licence:{self.__licence},ownername:{self.__username}]")
class Bike(vehicle):
    def __init__(self,licence,ownername,helmet_required):
        self.helmet_required=helmet_required
        super().__init__(licence,ownername)
    def display(self):
        print(f"vehicle[licence:{self.getlicence()},ownername:{self.getname()},helmet_required:{self.helmet_required}]")
    def vehicle_parking_fee(self,hours):
        return hours*20
class Car(vehicle):
    def __init__(self,licence,ownername,seats):
        self.seats=seats
        super().__init__(licence,ownername)
    def display(self):
        print(f"vehicle[licence:{self.getlicence()},ownername:{self.getname()},Seats:{self.seats}]")
    def vehicle_parking_fee(self,hours):
        return hours*50
class suv(vehicle):
    def __init__(self,licence,ownername,four_wheel_drive):
        self.four_wheel_drive=four_wheel_drive
        super().__init__(licence,ownername)
    def display(self):
        print(f"vehicle[licence:{self.getlicence()},ownername:{self.getname()},four_wheel:{self.four_wheel_drive}]")
    def vehicle_parking_fee(self,hours):
        return hours*70
class Truck(vehicle):
    def __init__(self,licence,ownername,max_load_capaciy):
        self.max_load_capacity=max_load_capaciy
        super().__init__(licence,ownername)
    def display(self):
        print(f"vehicle[licence:{self.getlicence()},ownername:{self.getname()},four_wheel:{self.max_load_capacity}]")
    def vehicle_parking_fee(self,hours):
        return hours*700
class ParkingSpot:
    
class ParkingLot: