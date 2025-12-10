import sys

m = []
with open(sys.argv[1]) as inp:
    for row in inp:
        m.append(list(str(row.replace("\n", ""))))

dirs = [[0, 1], [1, 0], [1, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
rolls_removed = 0
go_on = True
while go_on:
    go_on = False
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

        for a in range(len(m)):
            for b in range(len(m[a])):
                if m[a][b] == "x":
                    m[a][b] = "."
                    go_on = True
                    rolls_removed += 1

print(rolls_removed)
