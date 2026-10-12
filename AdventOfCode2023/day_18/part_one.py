"""Advent of Code 2023 - Day 18 - Part One"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().split("\n")))


def process_open(res, a, b, c):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    node = []
    futures = [[a, b]]
    for item in futures:
        x, y = item
        is_open = False
        for i in range(4):
            if (
                y + dy[i] < 0
                or y + dy[i] >= len(res)
                or x + dx[i] < 0
                or x + dx[i] >= len(res[0])
            ):
                is_open = True
                continue
            else:
                if res[y + dy[i]][x + dx[i]] == 0:
                    res[y + dy[i]][x + dx[i]] = c
                    futures.append([x + dx[i], y + dy[i]])
        node.append([x, y])
    if is_open:
        for i in futures:
            res[i[1]][i[0]] = -1


def process_dig(res, data):
    c = 4
    while 1:
        found = False
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j] == 0:
                    found = True
                    y = i
                    x = j
                    break
            if found:
                break
        if not found:
            break
        process_open(res, x, y, c)
        c += 1


def process_input(data):
    ran = 20
    while 1:
        overflows = 0
        try:
            direction = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}
            res = [[0] * ran for i in range(ran)]
            init = [ran // 2, ran // 2]
            for i in data:
                inst = i.split(" ")
                d = direction[inst[0]]
                for _j in range(int(inst[1])):
                    init[0] += d[0]
                    init[1] += d[1]
                    res[init[0]][init[1]] = 1
                if init[0] < 0 or init[1] < 0:
                    raise Exception
        except Exception:
            overflows = 1
            pass
        if overflows:
            print("Overflow")
            ran *= 2
        else:
            break
    return res


def main():
    res = process_input(data)
    process_dig(res, data)
    score = 0
    for line in res:
        for i in line:
            if i > 0:
                score += 1
    print(score)
    return score


if __name__ == "__main__":
    main()
