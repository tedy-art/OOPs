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