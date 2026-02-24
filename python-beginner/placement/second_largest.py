# Find second largest number without sorting

arr = [10, 45, 23, 89, 67]

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)
