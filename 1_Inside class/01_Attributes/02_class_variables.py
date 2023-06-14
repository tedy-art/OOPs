class Bank:
    #  as per it definition inside class and above constructor
    bankname = 'SBI' # Class variables
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