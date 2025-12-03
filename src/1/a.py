import sys

pos = 50
zero_ctr = 0
with open(sys.argv[1]) as inp:
    for row in inp:
        dir = str(row)[0]
        num = int(str(row)[1:].replace("\n", ""))
        if dir == "L":
            pos -= num
            while pos < 0:
                pos += 100
        elif dir == "R":
            pos += num
            while pos > 99:
                pos -= 100
        if pos == 0:
            zero_ctr += 1
print(zero_ctr)