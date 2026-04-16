list = ["Regyt", "Mirna", "Syifa"]
reversed_list = []

for i in range(len(list)-1, -1, -1):
    reversed_list.append(list[i])

print(f"Output: {reversed_list}")