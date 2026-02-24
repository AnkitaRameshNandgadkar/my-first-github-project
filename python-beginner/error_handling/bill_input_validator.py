try:
    units = int(input("Enter electricity units: "))

    if units < 0:
        raise ValueError("Units cannot be negative")

    bill = units * 8
    print("Bill amount:", bill)

except ValueError as e:
    print("Invalid input:", e)
