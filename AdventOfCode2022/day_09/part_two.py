"""Advent of Code 2022 - Day 09 - Part Two"""

from math import sqrt

import numpy as np

test_case = 0
"""
..##..
...##.
.####.
....#.
s###..
"""


def mocked_content2():
    temp = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split("\n")
    return temp


def mocked_content():
    temp = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")
    return temp


def main():
    file = open("./input.txt")
    content = file.read().split("\n")
    if test_case:
        content = mocked_content()
    if test_case > 1:
        content = mocked_content2()

    def format_to_int(content):
        cl = content.split(" ")
        return [cl[0], int(cl[1])]

    moves = list(map(format_to_int, content))

    chain = np.array(
        [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
        ]
    )
    tail_hitory = np.array(
        [
            [0, 0],
        ]
    )

    def distance(a, b):
        return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def up(position):
        position[1] += 1

    def down(position):
        position[1] -= 1

    def right(position):
        position[0] += 1

    def left(position):
        position[0] -= 1

    def find_move(a, b):
        res = np.subtract(a, b)
        return res

    d = {-2: -1, -1: -1, 0: 0, 1: 1, 2: 1}
    f_translation = {"U": up, "D": down, "L": left, "R": right}
    for move in moves:
        move_call = f_translation[move[0]]
        for _repetition in range(move[1]):
            # move :
            move_call(chain[0])
            for index in range(1, 10):
                if distance(chain[index], chain[index - 1]) >= 1.5:
                    chain_distance = find_move(chain[index - 1], chain[index])
                    trans = [d[chain_distance[0]], d[chain_distance[1]]]
                    chain[index] = np.add(chain[index], trans)
                else:
                    break
                if index == 9:
                    tail_hitory = np.append(tail_hitory, [chain[-1]], axis=0)
    result = len(np.unique(tail_hitory, axis=0))
    if test_case:
        print(tail_hitory)
    return result


if __name__ == "__main__":
    print(main())
