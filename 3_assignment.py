class employee():
    def __init__(self, nm, id, salary):
        self.name = nm
        self.id = id
        self.salary = salary

    def get_details(self):
        print(f"Employee name is {self.name}, id is {self.id} and salary is {self.salary}.")


e1 = employee('pqr', 1, 25000)
e1.get_details()

e2 = employee('xyz', 2, 65000)
e2.get_details()