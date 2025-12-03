import sys

pos = 50
zero_ctr = 0
with open(sys.argv[1]) as inp:
    for row in inp:
        dir = str(row)[0]
        num = int(str(row)[1:].replace("\n", ""))
        from_zero = pos == 0
        if dir == "L":
            pos -= num
            if pos < 0:
                while pos < 0:
                    pos += 100
                    if not from_zero or pos == 0:
                        zero_ctr += 1
                    from_zero = False
            if pos == 0:
                zero_ctr += 1
        elif dir == "R":
            pos += num
            while pos > 99:
                pos -= 100
                zero_ctr += 1
print(zero_ctr)