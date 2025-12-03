import sys

sum = 0
with open(sys.argv[1]) as line:
    for row in line:
        for pair in row.replace("\n", "").split(","):
            if pair == "":
                continue
            num1, num2 = pair.split("-")
            for num in range(int(num1), int(num2) + 1):
                if str(num)[(len(str(num)) // 2):] == str(num)[:(len(str(num)) // 2)]:
                    sum += num
print(sum)