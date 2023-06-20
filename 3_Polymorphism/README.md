**Polymorphism :**<br/><br/>
Poly = many<br/>
morphism = have forms<br/>

1] Sometimes an object comes in many types or forms.<br/>
2] If we have a button, there are many different draw outputs(round button, square button, button with image)but they do share the same logic: **onclick()**<br/>
3] we access them using the same method. This idea is called Polymorphism.<br/>

_<i>Polymorphism can be achieved in python though **method overloading** and **method overriding**<i/>_<br/>

**1] method overriding:**<br/>
1) Overriding means having two methods with the same name bur doing different tasks.<br/>
2) It means that one of the methods overrides the other.<br/>
3) If there is any method in the superclass and a method with the same name in a subclass, then by executing the method, the method of the corresponding class will be executed.<br/>

e.g.<br/>
**Variable overriding**<br/>

    # Variable overriding

    class Parent:
        name = "scatt"

    class Child(Parent):
        name = "David" # Overriding variable called "name"

    ob = Child()
    print(ob.name)

e.g.<br/>
**Method Overriding**    <br/>

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

    print(ob1.rateofInterest()) # 0
    print(ob2.rateofInterest()) # 10.5


**2]Method Overloading :**<br/>
1] In python you can define a method in a way that there are multiple ways to call it.<br/>
2] Given a single method or function, we can specify the number of parameters our self.<br/>
**IMP:-**<br/>
**Unlike some other programming languages, Python does not support method overloading by default**<br/>

e.g.

    class Calculator:
        def add(self, num1, num2):
            return num1 + num2

        def add(self, num1, num2, num3):
            return num1 + num2 + num3

    calculator = Calculator()
    print(calculator.add(2, 3))        # Output: TypeError: add() missing 1 required positional argument: 'num3'
    print(calculator.add(2, 3, 4))     # Output: 9
