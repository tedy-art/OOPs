"""
Question:
Create a base class called Animal with attribute name and age, and a method called
make_sound() that prints a sound. Then create two derived classes called Dog and Cat that
inherit from the Animal class. Implement the make_sound() method in each derived class to
print a specific sound for a dog and a cat, respectively. Finally, create instances of the
Dog and Cat classes, set their name and age attributes, and call the make_sound() method on
 each instance.

Hierarchical Inheritance approach:
    Step 1: create parent class name 'Animal' -> attributes are 1)name ,2)age
                                              -> method call make_sound()

    Step 2: create child class name 'Dog' -> inherit attributes from 'Animal'
                                           -> method call make_sound()

    Step 3: create child class name 'Cat' -> inherit attributes from 'Animal'
                                          -> Method call make_sound()

    Step 4: Create object -> for Dog --> o/p: name + age -->make_sound()
                          -> for Cat --> o/p: name + age -->make_sound()
"""

class Animal():
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def show_details(self):
        print("Name of Animal is ", self.name)
        print("age of animal is ", self.age)
    def make_sounds(self):
        print("and this animal make a sound like", self.sound)

class Dog(Animal):
    def show_details1(self):
        print("This is a Dog.")

class Cat(Animal):
    def show_details2(self):
        print("This is a Cat.")

d = Dog("Tommy", 5, "barking")
c = Cat("Catty", 3, "Maow Maow")

d.show_details1()
d.show_details()
d.make_sounds()

c.show_details2()
c.show_details()
c.make_sounds()