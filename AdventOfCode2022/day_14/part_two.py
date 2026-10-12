"""Advent of Code 2022 - Day 14 - Part Two"""

import numpy as np

test_case = 0


def mocked_content():
    pass


def main():
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().split("\n")
    mb = 0
    line_points = []
    for line in content:
        row = line.split(" ")
        current_points = []
        point: list = []
        for item in row:
            if item == "->":
                current_points.append(point)
                continue
            point = list(map(int, item.split(",")))
            mb = max(mb, point[1])
        current_points.append(point)
        line_points.append(current_points)

    truth_table = np.zeros((800, mb + 2), dtype=np.uint8)
    if test_case:
        truth_table = np.zeros((20, 17))

    def draw_line(a, b, truth_table):
        if test_case:
            return draw_line2(a, b, truth_table)
        if a[0] > b[0] or a[1] > b[1]:
            draw_line(b, a, truth_table)
            return 0
        for index in range(a[0], b[0] + 1):
            truth_table[index, a[1]] = 100
        for index in range(a[1], b[1] + 1):
            truth_table[a[0], index] = 100
        return 0

    def draw_line2(c, d, truth_table):
        a = [0, 0]
        b = [0, 0]
        a[0] = c[0] - 490
        a[1] = c[1]
        b[1] = d[1]
        b[0] = d[0] - 490

        if a[0] > b[0] or a[1] > b[1]:
            b[0] += 490
            a[0] += 490
            draw_line(b, a, truth_table)
            return 0
        for index in range(a[0], b[0] + 1):
            truth_table[index, a[1]] = -1
        for index in range(a[1], b[1] + 1):
            truth_table[a[0], index] = -1
        return 0

    for line in line_points:
        for index, point in enumerate(line[:-1]):
            draw_line(point, line[index + 1], truth_table)
            print(truth_table)

    def step(truth_table, sand):
        x, y = sand
        if y == truth_table.shape[1] - 1:
            return 1
        if truth_table[x, y + 1] == 0:
            sand[1] = y + 1
            truth_table[x, y] = 0
            truth_table[x, y + 1] = 250
            return 0
        elif truth_table[x - 1, y + 1] == 0:
            sand[0] = x - 1
            sand[1] = y + 1
            truth_table[x, y] = 0
            truth_table[x - 1, y + 1] = 250
            return 0
        elif truth_table[x + 1, y + 1] == 0:
            sand[0] = x + 1
            sand[1] = y + 1
            truth_table[x, y] = 0
            truth_table[x + 1, y + 1] = 250
        else:
            return 1

    sand = [500, 0]
    if test_case:
        sand = [10, 0]
    count = 0
    index_to_delete = []
    run = 1
    while run:
        count += 1
        while 1:
            step_result = step(truth_table, sand)
            if sand in [[500, 0], [10, 0]]:
                run = 0
                break
            if step_result == 1:
                index_to_delete.append(index)
                if test_case:
                    sand = [10, 0]
                else:
                    sand = [500, 0]
                break

    return count


if __name__ == "__main__":
    print(main())
