"""Advent of Code 2022 - Day 09 - Part One"""

from math import sqrt

import numpy as np

test_case = False
"""
..##..
...##.
.####.
....#.
s###..
"""


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

    def format_to_int(content):
        cl = content.split(" ")
        return [cl[0], int(cl[1])]

    moves = list(map(format_to_int, content))

    head_position = [0, 0]
    tail_position = [0, 0]
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

    f_translation = {"U": up, "D": down, "L": left, "R": right}
    for move in moves:
        for _repetition in range(move[1]):
            saved_head_position = [head_position[0], head_position[1]]
            move_call = f_translation[move[0]]
            # move :
            move_call(head_position)
            if distance(head_position, tail_position) >= 1.5:  # sqrt(2)==1.41
                tail_hitory = np.append(tail_hitory, [tail_position], axis=0)
                tail_position = saved_head_position
    tail_hitory = np.append(tail_hitory, [tail_position], axis=0)
    result = len(np.unique(tail_hitory, axis=0))
    if test_case:
        print(tail_hitory)
    return result


if __name__ == "__main__":
    print(main())

# answer 410400
