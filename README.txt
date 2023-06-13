Main concept of object oriented programming (OOPS):
1)class
2)object
3)polymorphism
4)Encapdulation
5)Inheritance
6)Data Abstarction

** Object oriented programming(oops):
    Total code is divided into objects.
    There things are very important in oop:
        1)class
        2)object
        3)referance variable

**What is class:
    -> class is a blueprint plan to constact object
    -> class is a logical entity
    -> class does not require momory for execution
    -> class is a user defined data type
    syntax: 
        class class_name:
            body_of_class

    e.g.
        class A:
            pass

**What is object:
    -> It is a physical entity
    -> It is a instance of class. instance-> means object.
    -> Object requires memory for execution.
    syntax:
        referance_vairable = class_name
    e.g.
        a1 = A()

** What is referance vairable:
    -> It is a vairable which is pointing to object and used to access the functionality of the object.

**Relation between**
1) class and object --> one to many
2) object and referance vairable --> one to one

** By using class we can group variable ??
eg.1.

class student:
    def __init__(self, nm, rl, mk):
        self.name = nm
        self.roll = rl
        self.marks = mk

s1 = student('jay', 1, 88)
print(f"student name is {s1.name}, roll number is {s1.roll} and marks are {s1.marks}")

s1 = student('viru', 2, 70)
print(f"student name is {s1.name}, roll number is {s1.roll} and marks are {s1.marks}")

o/p
student name is jay, roll number is 1 and marks are 88
student name is viru, roll number is 2 and marks are 70

eg.2.

class student:
    def __init__(self, nm, rl, mk):
        self.name = nm
        self.roll = rl
        self.marks = mk

    def get_details(self):
        print(f"student name is {self.name}, roll number is {self.roll} and marks are {self.marks}")

s1 = student('jay', 2, 88)
s1.get_details()

s2 = student('viru', 2, 70)
s2.get_details()

o/p :
student name is jay, roll number is 1 and marks are 88
student name is viru, roll number is 2 and marks are 70

** What is inside class??
-> 1) attributes
   2) Methods

   **1) attributes :-
    -> 1)instance Variables
    -> 2)class variables
    -> 3)local Variables

    1)instance Variables :-
        -> The variables difined inside instance Methods is called instance vairable
        -> These vairables are always written with self.
    
    e.g.
        class Bank:
            bankname = 'SBI'
            def __init__(self, acc, name, ammt):
                self.account_no = acc   # self.account_no instance vairables
                self.name = name        # self.name instance vairables
                self.ammount = ammt     # self.ammount instance vairables

        c1 = Bank(101, 'jay', 5000)
        print(c1)
        print(id(c1))
        print(type(c1))

        print(c1.name)
        print(c1.ammount)
        print(c1.bankname)

    2) class vairables :-
    -> These vairables are defined inside class and above constaructor.
 
        e.g.
            class Bank:

                #  as per it defination inside class and above construtor
                bankname = 'SBI' # Class vaiables 

                def __init__(self, acc, name, ammt):    #Constructor
                    self.account_no = acc   
                    self.name = name           
                    self.ammount = ammt     
                    
            c1 = Bank(101, 'jay', 5000)
            print(c1)
            print(id(c1))
            print(type(c1))

            print(c1.name)
            print(c1.ammount)
            print(c1.bankname)

    3) Local vairables :-   
    -> These vaiables are used to store local data temparary

    e.g.
            class Bank:
            
                bank_name = 'SBI' 
                
                def __init__(self, acc, name, ammt):
                    self.account_no = acc   
                    self.name = name           
                    self.ammount = ammt 

                def new_bank(self):
                    bank_name = "BOM" # local vaiables
                    print(bank_name)

                
            c1 = Bank(101, 'jay', 5000)
            print(c1.name)
            print(c1.ammount)
            print(c1.bank_name)
            c1.new_bank()

    **2) Methods
        1) instance Methods
        2) Class Methods
        3) static Methods

    1) instance Methods:-
    -> Within the method if we access instance vaiables and first argument of the Methods is self then that method is called instance method.