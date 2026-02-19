# Save student bill to file using class

class Student:

    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.rate = 8

    def bill(self):
        return self.units * self.rate


s = Student("Ankita", 120)

file = open("student_bill.txt", "w")
file.write("Name: " + s.name + "\n")
file.write("Bill: " + str(s.bill()))
file.close()

print("Data saved to file")
