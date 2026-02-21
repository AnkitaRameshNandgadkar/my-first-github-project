# Read bill report file

file = open("bill_report_sample.txt", "r")
content = file.read()
file.close()

print("Bill Report Content:")
print(content)
