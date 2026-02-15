# Hostel Bill System with File Saving

students = [
    {"name": "Ankita", "units": 120},
    {"name": "Rahul", "units": 150},
    {"name": "Sneha", "units": 90},
    {"name": "Amit", "units": 110}
]

rate_per_unit = 5

# Open file in write mode
file = open("bill_report.txt", "w")

total_revenue = 0

# List of student electricity usage
file.write("Hostel Electricity Bill Report\n\n")

for student in students:
    bill = student["units"] * rate_per_unit
    total_revenue += bill

    line = f"Name: {student['name']}, Units: {student['units']}, Bill: {bill}\n"

    print(line)
    file.write(line)

file.write(f"\nTotal Revenue: {total_revenue}")

file.close()

print("\nBill report saved to bill_report.txt")
