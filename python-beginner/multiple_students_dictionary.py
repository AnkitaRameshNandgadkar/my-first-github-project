# Dictionary with multiple students

students = {
    "Ankita": 120,
    "Rahul": 150,
    "Sneha": 100
}

rate = 5

for name, units in students.items():
    bill = units * rate
    print(name, "Bill:", bill)
