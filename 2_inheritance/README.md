**Inheritance**<br/>

with inheritance, one class derives the properties of another class.<br/>

**real-word logic of inheritance :**<br/>

    grandpa
        |
        |
    parent
        |
        |
    child

e.g.<br/>

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

<br/>**output**<br/>

    I am a vehicle.
    Mileage of vehicle is  500
    cost of vehicle is  500
    I am a vehicle.
    Mileage of vehicle is  200
    cost of vehicle is  1200
    I am a car

**Overriding init method :**<br/>
e.g.<br/>

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

**Output**<br/>

    #Vehicle#
    I am a vehicle.
    Mileage of vehicle is  20
    cost of a vehicle is  12000
    #__init__() modified/ over-ride init#
    I am a car.
    Number of tyres are  4
    Value of hP is  300


**Types of Inheritance :**<br/>
1] Single Inheritance<br/>
2] Multiple Inheritance<br/>
3] Multi-level Inheritance<br/>
4] Hybrid Inheritance<br/>
5] Hierarchical Inheritance<br/>

**1] Single Inheritance**<br/>
In single inheritance, a class inherits from a single base class.<br/>
The derived class inherits the attributes and methods of the base class.<br/>
It enables the derived class to extend or modify the functionality of the base class.<br/>

![single inheritance](https://github.com/tedy-art/OOPs/blob/main/Images/Single.png?raw=true)<br/>

e.g.<br/>

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
In multiple inheritance, the child inherits from more than 'one' parent class.<br/>
Multiple inheritance allows a class to inherit from multiple base classes.<br/>
The derived class can access attributes and methods from all the base classes.<br/>
It enables the derived class to combine functionalities from different classes.<br/>
![mulitple inheritance](https://github.com/tedy-art/OOPs/blob/main/Images/multiple.png?raw=true)<br/>

e.g.<br/>

    class Parent1:
        def assign_string_one(self, str1):
            self.str1 = str1

        def show_string_one(self):
            return self.str1

    class Parent2:
        def assgin_string_two(self, str2):
            self.str2 = str2

        def show_string_two(self):
            return self.str2

    class Derived(Parent1, Parent2):
        def assgin_string_three(self, str3):
            self.str3 = str3

        def show_string_three(self):
            return self.str3

    d1 = Derived()
    d1.assign_string_one('one')
    d1.assgin_string_two('two')
    d1.assgin_string_three('three')

    print(d1.show_string_one())
    print(d1.show_string_two())
    print(d1.show_string_three())


**Output**<br/>

    one
    two
    three

**Multi-level Inheritance:**<br/>
In multi-level inheritance, we have parent, child ,grandchild relationship.<br/>
Multilevel inheritance involves inheriting from a derived class, which itself is derived from another class.<br/>
The derived class at each level inherits the attributes and methods of its immediate parent class.<br/>
It forms a hierarchical relationship between classes<br/>

![multilevel inheritance](https://github.com/tedy-art/OOPs/blob/main/Images/multilevel.png?raw=true)<br/>

e.g. <br/>

    class Parent():
        def assign_name(self, name):
            self.name = name

        def show_name(self):
            return self.name

    class Child(Parent):
        def assign_age(self, age):
            self.age = age

        def show_age(self):
            return self.age

    class GrandChild(Child):
        def assign_gender(self, gender):
            self.gender = gender

        def show_gender(self):
            return self.gender

    gc = GrandChild()
    gc.assign_name('AVINASH')
    gc.assign_age(24)
    gc.assign_gender('Male')

    print(gc.show_name())
    print(gc.show_age())
    print(gc.show_gender())

**output**<br/>
    
    AVINASH
    24
    Male


**Hybrid Inheritance:**<br/>
Hybrid inheritance combines multiple types of inheritance, such as single, multiple, multilevel, or hierarchical inheritance.<br/>
It enables the creation of complex class hierarchies with diverse functionality.<br/>
It provides flexibility in designing class relationships.<br/>

![hybrid Inheritance](https://github.com/tedy-art/OOPs/blob/main/Images/Hybrid.png?raw=true)<br/>

e.g.<br/>

    # Python program to demonstrate hybrid inheritance
    class School:
	    def func1(self):
		    print("This function is in school.")


    class Student1(School):
	    def func2(self):
		    print("This function is in student 1. ")


    class Student2(School):
	    def func3(self):
		    print("This function is in student 2.")


    class Student3(Student1, School):
	    def func4(self):
		    print("This function is in student 3.")


    # Driver's code
    object = Student3()
    object.func1()
    object.func2()

**Output:**<br/>

    This function is in school.
    This function is in student 1. 

**Hierarchical Inheritance:**<br/>

Hierarchical inheritance involves multiple classes inheriting from a single base class.<br/>
Multiple derived classes share common attributes and methods from the base class.<br/>
It allows the derived classes to specialize or modify the inherited functionality.<br/>
![Hierarchical](https://github.com/tedy-art/OOPs/blob/main/Images/Hierarchical.png?raw=true)<br/>
e.g.<br/>

    # Python program to demonstrate Hierarchical inheritance
    # Base class
    class Parent:
	    def func1(self):
		    print("This function is in parent class.")

    # Derived class1
    class Child1(Parent):
	    def func2(self):
		    print("This function is in child 1.")

    # Derivied class2
    class Child2(Parent):
	    def func3(self):
		    print("This function is in child 2.")


    # Driver's code
    object1 = Child1()
    object2 = Child2()
    object1.func1()
    object1.func2()
    object2.func1()
    object2.func3()

**Output:**
    
    This function is in parent class.
    This function is in child 1.
    This function is in parent class.
    This function is in child 2.