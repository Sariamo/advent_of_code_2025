import sys

m = []
with open(sys.argv[1]) as inp:
    for row in inp:
        m.append(list(str(row.replace("\n", ""))))

ctr = 0
dirs = [[0, 1], [1, 0], [1, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] != "@":
            continue
        local_ctr = 0
        for dir in dirs:
            x, y = dir
            if 0 <= x + i < len(m) and 0 <= y + j < len(m[i]) and (m[x + i][y + j] == "@" or m[x + i][y + j] == "x"):
                local_ctr += 1
        if local_ctr < 4:
            m[i][j] = "x"
            ctr += 1

for row in m:
    print(" ".join(row))
print(ctr)
