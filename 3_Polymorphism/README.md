**Polymorphism :**
Poly = many
morphism = have forms

1] Sometimes an object comes in many types or forms.
2] If we have a button, there are many different draw outputs(round button, square button, button with image)but they do share the same logic: **onclick()**
3] we access them using the same method. This idea is called Polymorphism.

Polymorphism can be achieved in python though **method overloading** and **method overriding**

**1] method overriding:**
1) Overriding means having two methods with the same name bur doing different tasks.
2) It means that one of the methods overrides the other.
3) If there is any method in the superclass and a method with the same name in a subclass, then by executing the method, the method of the corresponding class will be executed.

e.g.<br/>
**Variable overriding**

    # Variable overriding

    class Parent:
        name = "scatt"

    class Child(Parent):
        name = "David" # Overriding variable called "name"

    ob = Child()
    print(ob.name)

e.g.<br/>
**Method Overriding**    

    # Method Overriding

    class Bank:
        def rateofInterest(self):
            return 0

    class ICICI(Bank):
        def rateofInterest(self): # Method Overriding
            return 10.5

    # Object creation
    ob1 = Bank()
    ob2 = ICICI()

    print(ob1.rateofInterest())
    print(ob2.rateofInterest())


2]Method Overloading