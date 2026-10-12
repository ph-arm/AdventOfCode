"""Advent of Code 2024 - Day 14 - Part One"""

import re

from shared import *


def main():
    pattern = re.compile(r"-?[0-9]+")
    # Example string to search
    # Find all matches in the string
    robots = []
    for line in mt:
        matches = pattern.findall(line)
        robots.append(
            [int(matches[0]), int(matches[1]), int(matches[2]), int(matches[3])]
        )

    sizex, sizey = 101, 103

    def run_100(robot):
        x, y, vx, vy = robot
        fx = (x + 100 * vx) % sizex
        fy = (y + 100 * vy) % sizey
        return fx, fy

    def factor_calc(mapping):
        res = 1
        offsets = [
            (0, 0),
            (sizex // 2 + 1, 0),
            (0, sizey // 2 + 1),
            (sizex // 2 + 1, sizey // 2 + 1),
        ]
        for offset in offsets:
            temp = 0
            for i in range(sizey // 2):
                temp += sum(
                    mapping[i + offset[1]][offset[0] : offset[0] + (sizex // 2)]
                )
            res *= temp
        return res

    mapping = [[0 for i in range(sizex)] for j in range(sizey)]
    for robot in robots:
        c = run_100(robot)
        mapping[c[1]][c[0]] += 1
    res = factor_calc(mapping)
    return res


if __name__ == "__main__":
    print(main())
