import sys

sum = 0
with open(sys.argv[1]) as line:
    for row in line:
        for pair in row.replace("\n", "").split(","):
            if pair == "":
                continue
            num1, num2 = pair.split("-")
            for num in range(int(num1), int(num2) + 1):
                for i in range(1, len(str(num))):
                    factor = len(str(num)) // i
                    if (str(num)[:i] * factor) == str(num):
                        sum += num
                        break
print(sum)