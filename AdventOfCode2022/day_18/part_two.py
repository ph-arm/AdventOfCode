"""Advent of Code 2022 - Day 18 - Part Two"""

import numpy as np

test_case = False


def check_neighbour(index, truth_table):
    result = 6
    for x in [-1, 1]:
        if truth_table[(index[0] - x, index[1], index[2])] in [0, 1]:
            result -= 1
        if truth_table[(index[0], index[1] - x, index[2])] in [0, 1]:
            result -= 1
        if truth_table[(index[0], index[1], index[2] - x)] in [0, 1]:
            result -= 1
    return result


def pollute(index, truth_table):
    truth_table[index] = 2
    if min(index) == 0 or max(index) == 24:
        return []
    res = []
    for x in [-1, 1]:
        if truth_table[(index[0] - x, index[1], index[2])] == 0:
            truth_table[(index[0] - x, index[1], index[2])] = 2
            res.append((index[0] - x, index[1], index[2]))
        if truth_table[(index[0], index[1] - x, index[2])] == 0:
            truth_table[(index[0], index[1] - x, index[2])] = 2
            res.append((index[0], index[1] - x, index[2]))
        if truth_table[(index[0], index[1], index[2] - x)] == 0:
            truth_table[(index[0], index[1], index[2] - x)] = 2
            res.append((index[0], index[1], index[2] - x))
    return res


def main():
    result = []
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().split("\n")

    def intp1(n):
        return int(n) + 2

    def format_line(line):
        items = tuple(map(intp1, line.split(",")))
        return items

    items = tuple(map(format_line, content))

    truth_table = np.zeros((25, 25, 25))
    for cube in items:
        truth_table[tuple(cube)] = 1
    result = 0
    pollution = [(1, 1, 1)]
    while pollution:
        current = []
        for poll in pollution:
            current += pollute(poll, truth_table)
        pollution = current
    for index, x in np.ndenumerate(truth_table):
        if x == 1:
            if min(index) == 0 or max(index) == 24:
                continue
            result += check_neighbour(index, truth_table)
    return int(result)


if __name__ == "__main__":
    print(main())
