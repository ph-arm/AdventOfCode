"""Advent of Code 2023 - Day 09 - Part Two"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
data = list(map(str.strip, f.read().split("\n")))


def check(currt):
    r = currt[0]
    nextline = []
    for i in currt[1:]:
        k = i - r
        r = i
        nextline.append(k)
    return nextline


def check2(line):
    ia = line[0]
    for i in line:
        if i != ia:
            return False
    return True


def process(line):
    temp = []
    current = list(map(int, line.split(" ")))
    temp.append(current)

    while 1:
        nextline = check(temp[-1])
        temp.append(nextline)
        if check2(nextline):
            break
    for i in range(1, len(temp)):
        c = temp[-i - 1][0] - temp[-i][0]
        temp[-i - 1] = [c] + temp[-i - 1]
    return temp[0][0]


def main():
    res = 0
    for line in data:
        res += process(line)
    print(res)
    return res


if __name__ == "__main__":
    main()
