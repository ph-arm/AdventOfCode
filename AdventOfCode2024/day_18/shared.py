"""Advent of Code 2024 - Day 18 - Shared input & utilities"""

test = 1
f = open("./input.txt")
content = f.read()
mt = content.split("\n")
mem_cor = []
for i in mt:
    mem_cor.append(i.split(","))

mt = [[0 for i in range(71)] for j in range(71)]
mapping = [[-1 for i in range(71)] for j in range(71)]
x, y = 0, 0


def corrupt(x, y):
    x, y = int(x), int(y)
    mt[x][y] = 1


queue = [[0, 0, 0]]
# simulate mem corr:
for i in mem_cor[0:1025]:
    x, y = int(i[1]), int(i[0])
    corrupt(x, y)
    mt[x][y] = 1
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def process(x, y, v):
    cur = []
    for move in moves:
        if (
            x + move[0] >= 0
            and x + move[0] < len(mt)
            and y + move[1] >= 0
            and y + move[1] < len(mt[0])
        ):
            if mt[x + move[0]][y + move[1]] == 1:
                continue
            if (
                mapping[x + move[0]][y + move[1]] > v + 1
                or mapping[x + move[0]][y + move[1]] == -1
            ):
                mapping[x + move[0]][y + move[1]] = v + 1
                cur.append([x + move[0], y + move[1], v + 1])
    return cur


pos = x, y
while x != 70 or y != 70:
    x, y, v = queue.pop(0)
    cur = process(x, y, v)
    queue += cur
    queue.sort(key=lambda x: x[2])
