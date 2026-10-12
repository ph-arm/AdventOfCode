"""Advent of Code 2024 - Day 14 - Part Two"""

import re

from shared import *


def main():
    pattern = re.compile(r"-?[0-9]+")
    robots = []
    for line in mt:
        matches = pattern.findall(line)
        robots.append(
            [int(matches[0]), int(matches[1]), int(matches[2]), int(matches[3])]
        )

    sizex, sizey = 101, 103

    def positions(r):
        return {((x + r * vx) % sizex, (y + r * vy) % sizey) for x, y, vx, vy in robots}

    # The Easter egg (Christmas tree) is the first time step where every robot
    # occupies a distinct cell. Positions repeat with period sizex * sizey.
    for r in range(sizex * sizey):
        if len(positions(r)) == len(robots):
            return r
    raise ValueError("tree pattern not found")


if __name__ == "__main__":
    print(main())
