import sys

sum = 0
with open(sys.argv[1]) as inp:
    for row in inp:
        str_list = [str(num) for num in row.replace("\n", "")]
        highest = 0
        for i in range(len(str_list) - 1):
            for j in range(i + 1, len(str_list)):
                if int(str_list[i] + str_list[j]) > highest:
                    highest = int(str_list[i] + str_list[j])
        sum += highest

print(sum)