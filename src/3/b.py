import sys

lines = []
with open(sys.argv[1]) as inp:
    for row in inp:
        lines.append([int(token) for token in row.replace("\n", "")])

sum = 0
for row in lines:
    num = ""
    row_without_end = row[:-11]
    used_nums = []
    while len(num) < 12:
        for searched_num in [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
            index_i = -1
            for ni in range(((used_nums[-1] + 1) if used_nums else 0), len(row_without_end)):
                if row[ni] == searched_num:
                    index_i = ni
                    break
            if index_i != -1:
                num += str(row_without_end[index_i])
                used_nums.append(index_i)
                if len(num) == 11:
                    row_without_end = row
                else:
                    row_without_end = row[:(-11 + len(num))]
                break
    sum += int(num)
print(sum)