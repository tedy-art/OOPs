"""
OOP Exercise 8: Determine if School_bus is also an instance(object) of the Vehicle class
"""
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
# if isinstance(School_bus, Vehicle):
#     print("School Bus is instance of Vehicle.")
# else:
#     print("No")
print(isinstance(School_bus, Vehicle))