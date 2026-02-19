# Hostel Room Class Example

class Room:

    def __init__(self, room_number, units):
        self.room_number = room_number
        self.units = units
        self.rate = 8
        self.fixed_charge = 50

    def total_bill(self):
        return (self.units * self.rate) + self.fixed_charge


room1 = Room(101, 120)

print("Room:", room1.room_number)
print("Total Bill:", room1.total_bill())
