"""Advent of Code 2024 - Day 20 - Shared input & utilities"""

test = 1
f = open("./input.txt")
# f = open("./input_test.txt", "r")

content = f.read()
mt = content.split("\n")


def find(item):
    for c1, i in enumerate(mt):
        for c2, j in enumerate(i):
            if j == item:
                return c1, c2
    return -1, -1


xs, ys = find("S")
xe, ye = find("E")

queue = [[xs, ys, 0]]
mapping = [[-1 for i in range(len(mt[0]))] for j in range(len(mt))]
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
mapping[xs][ys] = 0


def process(x, y, v):
    cur = []
    for move in moves:
        if (
            x + move[0] >= 0
            and x + move[0] < len(mt)
            and y + move[1] >= 0
            and y + move[1] < len(mt[0])
        ):
            if mt[x + move[0]][y + move[1]] == "#":
                continue
            if (
                mapping[x + move[0]][y + move[1]] > v + 1
                or mapping[x + move[0]][y + move[1]] == -1
            ):
                mapping[x + move[0]][y + move[1]] = v + 1
                cur.append([x + move[0], y + move[1], v + 1])
    return cur


x = xs
y = ys
while x != xe or y != ye:
    x, y, v = queue.pop(0)
    cur = process(x, y, v)
    queue += cur
    queue.sort(key=lambda x: x[2])

print(v)


def process_diff(i, j):
    c = mapping[i][j]
    shortcut = []
    if c == -1:
        return 0
    res = 0
    for im in moves:
        for jm in moves:
            r = (im[0] + jm[0], im[1] + jm[1])
            if (
                i + r[0] >= 0
                and i + r[0] < len(mt)
                and j + r[1] >= 0
                and j + r[1] < len(mt[0])
            ):
                if (
                    mt[i + r[0]][j + r[1]] == "#"
                    or mapping[i + r[0]][j + r[1]] <= c + 100
                ):
                    continue
                res += 1
                shortcut.append([i + r[0], j + r[1]])
    return res
