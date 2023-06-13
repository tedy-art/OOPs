class student:
    def __init__(self, nm, rl, mk):
        self.name = nm
        self.roll = rl
        self.marks = mk

    def get_details(self):
        print(f"student name is {self.name}, roll number is {self.roll} and marks are {self.marks}")

s1 = student('jay', 1, 88)
s1.get_details()

s2 = student('viru', 2, 70)
s2.get_details()