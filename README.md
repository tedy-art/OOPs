**Main concept of object-oriented programming (OOPS):<br />**
    1) class<br />
    2) object<br />
    3) polymorphism<br />
    4) Encapsulation<br />
    5) Inheritance<br />
    6) Data Abstraction<br />

**Object oriented programming(oops):**<br />
    Total code is divided into objects.<br />
    There things are very important in oop:<br />
        1)class<br />
        2)object<br />
        3)reference variable<br />

**What is class:**<br />
    -> class is a blueprint plan to construct object<br />
    -> class is a logical entity<br />
    -> class does not require momory for execution<br />
    -> class is a user defined data type<br />
    syntax: <br />

        class class_name:
            body_of_class

        e.g.
            class A:
                pass

**What is object:<br />**
    -> It is a physical entity<br />
    -> It is a instance of class. instance-> means object.<br />
    -> Object requires memory for execution.<br />
    syntax:<br />

        referance_vairable = class_name

        e.g.
            a1 = A()

**What is reference variable:<br />**
    -> It is a vairable which is pointing to object and used to access the functionality of the object.<br />

**Relation between**
1) class and object --> one to many<br />
2) object and referance vairable --> one to one<br />

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

o/p<br />
student name is jay, roll number is 1 and marks are 88<br />
student name is viru, roll number is 2 and marks are 70<br />

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
student name is jay, roll number is 1 and marks are 88<br />
student name is viru, roll number is 2 and marks are 70<br />
<br />
**What is inside class??**<br />
**->1) attributes<br/>
->  2) Methods<br />**

   **1) attributes :-<br />**
    -> 1)instance Variables<br />
    -> 2)class variables<br />
    -> 3)local Variables<br />

**1)instance Variables :-<br />**
        -> The variables difined inside instance Methods is called instance variable.<br />
        -> These vairables are always written with self.<br />
    
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

**2) class variables :-<br />**
    -> These variables are defined inside class and above constructor.<br />
 
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

**3) Local variables :- <br />**
    -> These variables are used to store local data temporary.<br />

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

**2) Methods <br />**
        1) instance Methods<br />
        2) Class Methods<br />
        3) static Methods<br />

**1) instance Methods:-<br />**
    -> Within the method if we access instance vaiables and first argument of the Methods is self then that method is called instance method.<br />