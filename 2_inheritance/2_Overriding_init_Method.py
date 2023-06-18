class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("I am a vehicle.")
        print("Mileage of vehicle is ",self.mileage)
        print("cost of a vehicle is ",self.cost)

class Car(Vehicle):
    def __init__(self,  mileage, cost, tyres, hp):
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("I am a car.")
        print("Number of tyres are ",self.tyres)
        print("Value of hP is ",self.hp)

c1 = Car(20,12000,4,300)
c1.show_details()
c1.show_car_details()