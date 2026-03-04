# Comparing Linear and Binary Search

arr = [10, 20, 30, 40, 50, 60, 70]
target = 40

# Linear Search
for i in range(len(arr)):
    if arr[i] == target:
        print("Linear Search Found at:", i)

# Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print("Binary Search Found at:", binary_search(arr, target))
