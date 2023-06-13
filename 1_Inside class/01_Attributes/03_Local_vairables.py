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