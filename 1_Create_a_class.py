# Creating a class
class student:
    #Creating function in class
    def __init__(self, nm, rl, mk):
        self.name = nm
        self.roll = rl
        self.marks = mk

# Creating Object/ referance variable

# object 1
s1 = student('jay', 1, 88)
print(f"student name is {s1.name}, roll number is {s1.roll} and marks are {s1.marks}")

# Object 2
s1 = student('Viru', 2, 70)
print(f"student name is {s1.name}, roll number is {s1.roll} and marks are {s1.marks}")