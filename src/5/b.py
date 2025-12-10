import sys

def remove_range(ranges, r):
    if r in ranges:
        ranges.remove(r)


ranges = []
num_mode = False
with open(sys.argv[1]) as inp:
    for row in inp:
        row = row.replace("\n", "")
        if row == "":
            break
        else:
            l, u = row.split("-")
            ranges.append([int(l), int(u)])

ctr = 0
nums = []
cutting_ranges = True
while cutting_ranges:
    cutting_ranges = False
    for r1 in ranges:
        l1, u1 = r1
        for r2 in ranges:
            l2, u2 = r2
            if r1 != r2:
                if l1 <= l2 <= u2 <= u1:
                    remove_range(ranges, r2)
                    cutting_ranges = True
                elif l2 <= l1 <= u1 <= u2:
                    remove_range(ranges, r1)
                    cutting_ranges = True
                elif l1 <= l2 <= u1 <= u2:
                    ranges.append([l1, u2])
                    remove_range(ranges, r1)
                    remove_range(ranges, r2)
                    cutting_ranges = True
                elif l2 <= l1 <= u2 <= u1:
                    ranges.append([l2, u1])
                    remove_range(ranges, r1)
                    remove_range(ranges, r2)
                    cutting_ranges = True

    ranges_without_doubles = []
    for range in ranges:
        if range not in ranges_without_doubles:
            ranges_without_doubles.append(range)
    ranges = ranges_without_doubles

for r in ranges:
    l, u = r
    ctr += u - l + 1
print(ctr)