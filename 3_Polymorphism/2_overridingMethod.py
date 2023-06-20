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
