# Mini Hostel Bill Generator

rooms = [
    {"room": 101, "units": 120},
    {"room": 102, "units": 150},
    {"room": 103, "units": 100}
]

rate = 8

file = open("generated_bill_report.txt", "w")

for r in rooms:
    total = r["units"] * rate
    line = f"Room {r['room']} - {r['units']} units - {total} Rs\n"
    file.write(line)

file.close()

print("Bill report generated successfully")
