class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Personal Details : ")
        print("")
        print("Name : ", self.name)
        print("age : ", self.age)
        print("Gender : ", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, ammount):
        self.ammount = ammount
        self.balance = self.balance + self.ammount
        print("Account balance has been updated : [INR]",self.balance)

    def withdrow(self, ammount):
        self.ammount = ammount
        if self.ammount > self.balance:
            print("Insufficient Funds | Balance Available : [INR]", self.balance)
        else:
            self.balance = self.balance - self.ammount
            print("Account have been updated : [INR]", self.balance)
    def view_balance(self):
        self.show_details()
        print("Account Balance is [INR]", self.balance)

info = Bank("tejas", 26, "male")
info.show_details()
info.deposit(10000)
info.view_balance()
info.withdrow(5400)
info.view_balance()