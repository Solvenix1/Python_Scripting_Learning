class Vehicle:

    vehicle_count = 0

    def __init__(self, brand, year, motor, color):
        self.brand = brand
        self.year = year
        self.motor = motor
        self.color = color
        Vehicle.vehicle_count += 1

    def drive(self):
        print(f'You drive {self.brand}')

    def information(self):
        print(f"Your vehicle is {self.brand} and its year is {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, motor, color, lagguage_kq):
        super().__init__(brand, year,motor,color)
        
        self.lagguage_kq = lagguage_kq

    def work(self): 
        print(f'{self.brand} is working')


class Plane(Vehicle):
    def __init__(self,brand, year, motor, color, wing_count):
        super().__init__(brand,year,motor,color)
        self.wing_count = wing_count
    

        