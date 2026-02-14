students = [
    {"name": "Ankita", "units": 120},
    {"name": "Rahul", "units": 150}
]

rate = 5
total_revenue = 0

for student in students:
    bill = student["units"] * rate
    total_revenue += bill

print("Total Hostel Revenue:", total_revenue)
