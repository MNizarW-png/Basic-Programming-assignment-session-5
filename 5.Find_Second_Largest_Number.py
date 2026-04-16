numbers = [9,100,101,88,3,7]
largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(f"The second largest number is {second_largest}")