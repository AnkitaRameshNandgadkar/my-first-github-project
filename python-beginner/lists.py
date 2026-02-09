# Day 11 - Python Lists

# Creating a list
room_numbers = [101, 102, 103, 104, 105]
water_units = [120, 150, 100, 180, 130]

rate_per_unit = 3

print("Water bill per room:")

# Looping through list
for units in water_units:
    bill = units * rate_per_unit
    print(bill)

# Real-world example
students = ["Ankita", "Ravi", "Neha", "Amit"]

print("\nStudents staying in hostel:")
for student in students:
    print(student)

print("\nTotal students:", len(students))
