"""Advent of Code 2022 - Day 10 - Part One"""

import numpy as np

test_case = False


def main():
    file = open("./input.txt")
    if test_case:
        file = open("./test_input.txt")

    content = file.read().split("\n")

    def format_to_int(content):
        if content[0] == "n":
            return ["noop"]
        cl = content.split(" ")
        return [cl[0], int(cl[1])]

    moves = list(map(format_to_int, content))
    max_cycle = len(moves) * 2
    value_cycle = np.zeros(max_cycle)
    index = 1
    for move in moves:
        if move[0] == "noop":
            index += 1
        else:
            value_cycle[index + 2] = move[1]
            index += 2

    signal = [20 + 40 * v for v in range(6)]
    res = 1
    answer = 0
    for cycle_index in range(1, 241):
        res += value_cycle[cycle_index]
        if cycle_index in signal:
            answer += cycle_index * res
    return int(answer)


if __name__ == "__main__":
    print(main())
