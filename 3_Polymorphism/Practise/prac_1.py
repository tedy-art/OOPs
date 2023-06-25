class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog makes sound: Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Cat makes sound: Meow!")

class Lion(Animal):
    def make_sound(self):
        print("Lion makes sound: Roar!")

# Create a list of animal objects
animals = [Dog(), Cat(), Lion()]

# Iterate over the list and call the make_sound() method
for animal in animals:
    animal.make_sound()
