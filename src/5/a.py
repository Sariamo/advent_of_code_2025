import sys

ranges = []
nums = []
num_mode = False
with open(sys.argv[1]) as inp:
    for row in inp:
        row = row.replace("\n", "")
        if row == "":
            num_mode = True
            continue
        if not num_mode and row != "":
            num1, num2 = row.split("-")
            ranges.append([int(num1), int(num2)])
        else:
            nums.append(int(row))

ctr = 0
for num in nums:
    for r in ranges:
        num1, num2 = r
        if num1 <= num <= num2:
            ctr += 1
            break

print(ctr)