class Student:

    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.rate = 8

    def bill(self):
        return self.units * self.rate


name = input("Enter name: ")
units = int(input("Enter units: "))

s = Student(name, units)

print("Bill:", s.bill())
