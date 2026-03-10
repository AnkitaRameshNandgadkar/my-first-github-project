# Two Pointer Technique Example
# Find if a pair exists with given sum

arr = [2, 4, 7, 11, 15, 20]
target = 18

left = 0
right = len(arr) - 1

found = False

while left < right:

    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print("Pair found:", arr[left], arr[right])
        found = True
        break

    elif current_sum < target:
        left += 1

    else:
        right -= 1


if not found:
    print("No pair found")
