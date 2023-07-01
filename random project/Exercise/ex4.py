"""
OOP Exercise 5:
Define a property that must have the same value for every class instance(object)
Define a class attribute “color” with a default value white.
I.e., Every Vehicle should be white.

to do:
1) same value for every class object
2)
"""
class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

school_bus = Bus("School Volvo", 150, 12)
print(f"color : {Bus.color}, Vehicle name : {school_bus.name}, Speed : {school_bus.max_speed}, Mileage : {school_bus.mileage}")
car = Car("Audi A8", 240, 18)
print(f"color : {car.color}, Vehicle name : {car.name}, Speed : {car.max_speed}, Mileage : {car.mileage}")