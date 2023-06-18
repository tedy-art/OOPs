"""
Create a base class called Vehicle with attributes name and speed, and a method
called start() that prints a message indicating the vehicle has started. Then create two
derived classes called Car and Bike that inherit from the Vehicle class. Implement the
start() method in each derived class to print a specific message for starting a car and a
bike, respectively. Finally, create instances of the Car and Bike classes, set their name
and speed attributes, and call the start() method on each instance.
"""
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def start(self):
        print("The Vehicle is started.")

class Car(Vehicle):
    def start(self):
        print("Car is started.")
class Bike(Vehicle):
    def start(self):
        print("Bike is started.")

car = Car("volvo", 150)
bike = Bike("FZ", 90)

car.start()
print(f"name of car is {car.name} and speed is {car.speed}")

bike.start()
print(f"name of bike is {bike.name} and speed is {bike.speed}")