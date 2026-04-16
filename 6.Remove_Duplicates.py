numbers = [1,1,2,2,4,4,5,6]
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print(f"Output: {unique_list}")