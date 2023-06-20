# Variable overriding

class Parent:
    name = "scatt"

class Child(Parent):
    name = "David" # Overriding variable called "name"

ob = Child()
print(ob.name)