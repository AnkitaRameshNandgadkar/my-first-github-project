# Hostel Bill System with Exception Handling

def calculate_bill(units, rate):
    return units * rate


try:
    name = input("Enter student name: ")
    units = int(input("Enter electricity units used: "))
    rate = 8

    bill = calculate_bill(units, rate)

    print("\nBill Details")
    print("------------------")
    print("Student:", name)
    print("Units:", units)
    print("Rate per unit:", rate)
    print("Total Bill:", bill)

except ValueError:
    print("Error: Please enter valid numeric value for units.")

except Exception as e:
    print("Unexpected error occurred:", e)

finally:
    print("\nProgram executed successfully.")
