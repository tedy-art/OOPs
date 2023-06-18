class Parent():
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name

class Child(Parent):
    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age

class GrandChild(Child):
    def assign_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender

gc = GrandChild()
gc.assign_name('AVINASH')
gc.assign_age(24)
gc.assign_gender('Male')

print(gc.show_name())
print(gc.show_age())
print(gc.show_gender())