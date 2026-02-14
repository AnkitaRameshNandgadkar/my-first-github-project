# Hostel Bill Management System
# Using Lists, Dictionaries, and Functions

# List of students with electricity units
students = [
    {"name": "Ankita", "units": 120},
    {"name": "Rahul", "units": 150},
    {"name": "Sneha", "units": 90},
    {"name": "Amit", "units": 110}
]

rate_per_unit = 5


# Function to calculate bill
def calculate_bill(units):
    return units * rate_per_unit


# Function to display all bills
def display_bills(student_list):
    total_revenue = 0

    print("Hostel Electricity Bill Report\n")

    for student in student_list:
        bill = calculate_bill(student["units"])
        total_revenue += bill

        print("Name:", student["name"])
        print("Units:", student["units"])
        print("Bill:", bill)
        print("----------------------")

    print("Total Revenue:", total_revenue)


# Run program
display_bills(students)
