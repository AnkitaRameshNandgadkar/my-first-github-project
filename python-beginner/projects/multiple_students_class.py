# Multiple students using class and list

class Student:

    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.rate = 8

    def calculate_bill(self):
        return self.units * self.rate


students = [
    Student("Ankita", 120),
    Student("Rahul", 150),
    Student("Neha", 100)
]

print("Student Bills")
print("----------------")

for s in students:
    print(s.name, ":", s.calculate_bill())
