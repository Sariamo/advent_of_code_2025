import sys


def d(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return abs(int(x2) - int(x1)) ** 2 + abs(int(y2) - int(y1)) ** 2 + abs(int(z2) - int(z1)) ** 2

coords = []
with open(sys.argv[1]) as inp:
    for row in inp:
        if row != "" and row != "\n":
            coords.append(row.replace("\n", "").split(","))

connection_ctr = 0
connections = []
connections_plat = []
distances = []

for coord1 in coords:
    for coord2 in coords:
        if coord1 == coord2 or [coord2, coord1] in connections_plat:
            continue
        distances.append(d(coord1, coord2))
        connections_plat.append([coord1, coord2])

connections_plat = [x for _, x in sorted(zip(distances, connections_plat))]
distances = []

for shortest_coords in connections_plat:
    new_con_1, new_con_2 = shortest_coords
    in_c = False
    for c in connections:
        for con_mem in c:
            if con_mem == new_con_1 and new_con_2 in c or con_mem == new_con_2 and new_con_1 in c:
                in_c = True
                break
            if con_mem == new_con_1 and new_con_2 not in c:
                c.append(new_con_2)
                in_c = True
                break
            if con_mem == new_con_2 and new_con_1 not in c:
                c.append(new_con_1)
                in_c = True
                break
        if in_c:
            break

    if not in_c:
        connections.append(shortest_coords)

    b = False
    for c1 in connections:
        for c2 in connections:
            for con_mem1 in c1:
                if c1 != c2 and con_mem1 in c2:
                    new_c = c1
                    new_c.extend(c2)
                    new_c_unique = []
                    for nc in new_c:
                        if nc not in new_c_unique:
                            new_c_unique.append(nc)
                    connections.append(new_c_unique)
                    connections.remove(c1)
                    connections.remove(c2)
                    b = True
                    break
            if b:
                break
        if b:
            break

    if len(connections) == 1 and len(connections[0]) == 1000:
        print(int(new_con_1[0]) * int(new_con_2[0]))
        break