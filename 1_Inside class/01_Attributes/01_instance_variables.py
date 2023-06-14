class Bank:
    bankname = 'SBI'
    def __init__(self, acc, name, ammt):
        self.account_no = acc   # self.account_no is a instance variable acc
        self.name = name        # self.name is a instance variables name
        self.ammount = ammt     # self.amount is a instance vairables ammt

c1 = Bank(101, 'jay', 5000)
print(c1)
print(id(c1))
print(type(c1))

print(c1.name)
print(c1.ammount)
print(c1.bankname)