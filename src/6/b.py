import math
import sys

s = 0
m = []
operations = []
with open(sys.argv[1]) as inp:
    for row in inp:
        if not "+" in row and not "*" in row:
            m.append(list(row.replace("\n", "")))
        else:
            operations = list([op for op in row.replace("\n", "").split(" ") if op != ""])
curr_nums = []
op_ctr = 0
for j in range(len(m[0])):
    num = ""
    all_empty = True
    operator = ""
    for i in range(len(m)):
        token = m[i][j]
        if token != " ":
            num += token
            all_empty = False
    if not all_empty:
        curr_nums.append(int(num))
    if all_empty or j == len(m[0]) - 1:
        if operations[op_ctr] == "+":
            s += sum(curr_nums)
        else:
            s += math.prod(curr_nums)
        op_ctr += 1
        all_empty = False
        curr_nums = []
print(s)
