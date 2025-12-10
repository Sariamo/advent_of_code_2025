import sys

nums = []
operations = []
with open(sys.argv[1]) as inp:
    for row in inp:
        row_list = str(row).replace("\n", "").replace("  ", " ").split(" ")
        row_list = [num for num in row_list if num != ""]
        if "+" in row_list or "*" in row_list:
            operations = row_list
        else:
            nums.append(row_list)

sum = 0
for j in range(len(nums[0])):
    if operations[j] == "+":
        for i in range(len(nums)):
            sum += int(nums[i][j])
    elif operations[j] == "*":
        product = 1
        for i in range(len(nums)):
            product *= int(nums[i][j])
        sum += product
print(sum)