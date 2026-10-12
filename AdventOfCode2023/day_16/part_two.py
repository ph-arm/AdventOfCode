"""Advent of Code 2023 - Day 16 - Part Two"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().split("\n")))


def process_item(item, res, data):
    x, y, d = item
    if d == 1:  # right
        if x + 1 < len(data[0]):
            if res[y][x + 1] & 1:
                return []
            res[y][x + 1] += 1
            if data[y][x + 1] == "|":
                return [(x + 1, y, 2), (x + 1, y, 8)]
            if data[y][x + 1] == "/":
                return [(x + 1, y, 8)]
            if data[y][x + 1] == "\\":
                return [(x + 1, y, 2)]
            if data[y][x + 1] in ["-", "."]:
                return [(x + 1, y, 1)]

    if d == 2:  # down
        if y + 1 < len(data):
            if res[y + 1][x] & 2:
                return []
            res[y + 1][x] += 2
            if data[y + 1][x] == "-":
                return [(x, y + 1, 1), (x, y + 1, 4)]
            if data[y + 1][x] == "/":
                return [(x, y + 1, 4)]
            if data[y + 1][x] == "\\":
                return [(x, y + 1, 1)]
            if data[y + 1][x] in ["|", "."]:
                return [(x, y + 1, 2)]

    if d == 4:  # left
        if x - 1 >= 0:
            if res[y][x - 1] & 4:
                return []
            res[y][x - 1] += 4
            if data[y][x - 1] == "|":
                return [(x - 1, y, 2), (x - 1, y, 8)]
            if data[y][x - 1] == "/":
                return [(x - 1, y, 2)]
            if data[y][x - 1] == "\\":
                return [(x - 1, y, 8)]
            if data[y][x - 1] in ["-", "."]:
                return [(x - 1, y, 4)]

    if d == 8:  # up
        if y - 1 >= 0:
            if res[y - 1][x] & 8:
                return []
            res[y - 1][x] += 8
            if data[y - 1][x] == "-":
                return [(x, y - 1, 1), (x, y - 1, 4)]
            if data[y - 1][x] == "/":
                return [(x, y - 1, 1)]
            if data[y - 1][x] == "\\":
                return [(x, y - 1, 4)]
            if data[y - 1][x] in ["|", "."]:
                return [(x, y - 1, 8)]
    return []


def process_input(data, entry):
    res = [[0] * len(data[0]) for i in range(len(data))]
    x, y, d = entry
    queue = [[x, y, d]]  # x:0 ,y:0, r:1 d:2,l:4,u:8
    while 1:
        item = queue.pop(0)
        n = process_item(item, res, data)
        queue += n
        if not len(queue):
            break
    return res


def calc_score(data):
    score = 0
    for line in data:
        for i in line:
            if i > 0:
                score += 1
    return score


def main():
    score_array = []
    for i in range(len(data)):
        res = process_input(data, (-1, i, 1))
        score_array.append(calc_score(res))

    for i in range(len(data)):
        res = process_input(data, (len(data[0]), i, 4))
        score_array.append(calc_score(res))

    for i in range(len(data[0])):
        res = process_input(data, (i, -1, 2))
        score_array.append(calc_score(res))

    for i in range(len(data)):
        res = process_input(data, (i, len(data), 8))
        score_array.append(calc_score(res))

    print(max(score_array))
    return max(score_array)


if __name__ == "__main__":
    main()
