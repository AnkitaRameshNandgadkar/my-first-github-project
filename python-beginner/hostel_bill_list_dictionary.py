# Lists + Dictionaries combined example
# Hostel Utility Bill System

students = [
    {"name": "Ankita", "units": 120},
    {"name": "Rahul", "units": 150},
    {"name": "Sneha", "units": 100},
    {"name": "Amit", "units": 130}
]

rate_per_unit = 5

print("Hostel Electricity Bills:\n")

for student in students:
    bill = student["units"] * rate_per_unit
    print("Name:", student["name"])
    print("Units:", student["units"])
    print("Bill:", bill)
    print("-------------------")
