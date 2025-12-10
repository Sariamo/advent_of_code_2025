import sys

m = []
places = []
with open(sys.argv[1]) as inp:
    for i, row in enumerate(inp):
        r = []
        for j, token in enumerate(row):
            t = str(token).replace("\n", "")
            r.append(t)
            if t == "S":
                places.append([i, j])
        m.append(r)

split_ctr = 0

while places:
    new_places = []
    for p in places:
        if p[0] + 1 == len(m):
            continue
        elif m[p[0] + 1][p[1]] == ".":
            m[p[0] + 1][p[1]] = "|"
            new_places.append([p[0] + 1, p[1]])
        elif m[p[0] + 1][p[1]] == "^":
            m[p[0] + 1][p[1] - 1] = "|"
            m[p[0] + 1][p[1] + 1] = "|"
            new_places.append([p[0] + 1, p[1] - 1])
            new_places.append([p[0] + 1, p[1] + 1])
            split_ctr += 1
    places = new_places

print(split_ctr)