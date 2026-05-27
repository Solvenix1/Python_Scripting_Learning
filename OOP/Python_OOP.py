from Vehicle1class import Vehicle
from Vehicle1class import Car
from Vehicle1class import Plane
vehicle1 = Vehicle("Mercedes", 2000, 2.5, "Red")
vehicle2 = Vehicle("Mercedes", 2000, 2.5, "Red")
vehicle3 = Vehicle("Mercedes", 2000, 2.5, "Red")

vehicle1.drive()
vehicle1.information()

print(Vehicle.vehicle_count)

car1 = Car("Bmw", 2005, 1.8, "Black",150)

print(car1.brand)
car1.work()

pl1 = Plane(None, 2020, 12, "White", 2)
print(pl1.brand)

