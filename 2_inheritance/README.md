**Inheritance**

with inheritance one class derive the properties of another class.

**real-word logic of inheritance :**

    grandpa
        |
        |
    parent
        |
        |
    child

e.g.

    class Vehicle:
        def __init__(self, mileage, cost):
            self.mileage = mileage
            self.cost = cost

        def show_details(self):
            print("I am a vehicle.")
            print("Mileage of vehicle is ",self.mileage)
            print("cost of vehicle is ", self.cost)

    v1 = Vehicle(500,500)
    v1.show_details()

    class Car(Vehicle):
        def show_car(self):
            print("I am a car")

    c1 = Car(200,1200)
    c1.show_details()
    c1.show_car()

<br/>output

    I am a vehicle.
    Mileage of vehicle is  500
    cost of vehicle is  500
    I am a vehicle.
    Mileage of vehicle is  200
    cost of vehicle is  1200
    I am a car

**Overriding init method :**
e.g.

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

**Output**

    #Vehicle#
    I am a vehicle.
    Mileage of vehicle is  20
    cost of a vehicle is  12000
    #__init__() modified/ over-ride init#
    I am a car.
    Number of tyres are  4
    Value of hP is  300


**Types of Inheritance :**
1] Single Inheritance
2] Multiple Inheritance
3] Mulit-level Inheritance
4] Hybried Inheritance
5] Hierarchical Inheritance

**1] Single Inheritance**
In single inheritance, a class inherits from a single base class.<br/>
The derived class inherits the attributes and methods of the base class.<br/>
It enables the derived class to extend or modify the functionality of the base class.<br/>

![single inheritance](https://github.com/tedy-art/OOPs/blob/main/Images/Single.png?raw=true)

e.g.

        class Vehicle:
        def __init__(self, mileage, cost):
            self.mileage = mileage
            self.cost = cost

        def show_details(self):
            print("I am a vehicle.")
            print("Mileage of vehicle is ",self.mileage)
            print("cost of vehicle is ", self.cost)

    v1 = Vehicle(500,500)
    v1.show_details()

    class Car(Vehicle):
        def show_car(self):
            print("I am a car")

    c1 = Car(200,1200)
    c1.show_details()
    c1.show_car()

**Output**<br/>
    I am a vehicle.
    Mileage of vehicle is  500
    cost of vehicle is  500
    I am a vehicle.
    Mileage of vehicle is  200
    cost of vehicle is  1200
    I am a car


**Multiple Inheritance:**<br/>
In mulitple inheritance, the child inherit from more than 'one' parent class.
![mulitple inheritance](https://github.com/tedy-art/OOPs/blob/main/Images/multiple.png?raw=true)


