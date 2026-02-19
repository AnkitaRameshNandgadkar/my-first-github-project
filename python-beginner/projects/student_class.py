# Student Class Example (OOP)

class Student:

    def __init__(self, name, room, units):
        self.name = name
        self.room = room
        self.units = units
        self.rate = 8

    def calculate_bill(self):
        return self.units * self.rate

    def display(self):
        print("\nStudent Details")
        print("---------------------")
        print("Name:", self.name)
        print("Room:", self.room)
        print("Units:", self.units)
        print("Bill:", self.calculate_bill())


# Creating object
student1 = Student("Ankita", 101, 120)

student1.display()
