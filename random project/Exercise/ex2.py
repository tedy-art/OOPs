# Create a child class Bus that will inherit all the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 180, 12)
print(f"Vehicle Name: {bus.name}, Speed: {bus.max_speed}, Mileage: {bus.mileage}")
# Vehicle Name: School Volvo Speed: 180 Mileage: 12