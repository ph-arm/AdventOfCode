"""Advent of Code 2023 - Day 10 - Part One"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
data = list(map(str.strip, f.read().split("\n")))


def main():
    start = []
    for row_idx, line in enumerate(data):
        if "S" in line:
            start.append(row_idx)
            start.append(line.index("S"))
            break

    map_opened = [[0 for i in range(len(data[0]))] for j in range(len(data))]
    map_opened[start[0]][start[1]] = 1

    def check(x, y):
        """| is a vertical pipe connecting north and south.
        - is a horizontal pipe connecting east and west.
        L is a 90-degree bend connecting north and east.
        J is a 90-degree bend connecting north and west.
        7 is a 90-degree bend connecting south and west.
        F is a 90-degree bend connecting south and east.
        . is ground; there is no pipe in this tile."""
        if data[x][y] == "|":
            return [(x - 1, y), (x + 1, y)]
        if data[x][y] == "-":
            return [(x, y - 1), (x, y + 1)]
        if data[x][y] == "L":
            return [(x - 1, y), (x, y + 1)]
        if data[x][y] == "J":
            return [(x - 1, y), (x, y - 1)]
        if data[x][y] == "7":
            return [(x + 1, y), (x, y - 1)]
        if data[x][y] == "F":
            return [(x + 1, y), (x, y + 1)]
        if data[x][y] == ".":
            return []
        if data[x][y] == "S":
            if test:
                return [(x + 1, y), (x, y + 1)]
            return [(x + 1, y), (x, y - 1)]

    list_to_pop = [start]
    while 1:
        x, y = list_to_pop.pop(0)
        data[x][y]
        v = map_opened[x][y]
        to_open = check(x, y)
        for i in to_open:
            if map_opened[i[0]][i[1]] == 0:
                map_opened[i[0]][i[1]] = 1 + v
                list_to_pop.append(i)
        if list_to_pop == []:
            break

    d = map(max, map_opened)
    return max(d) - 1


if __name__ == "__main__":
    print(main())
