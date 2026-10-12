"""Advent of Code 2023 - Day 06 - Part Two"""

import math

t = [44, 70, 70, 80]
d = [283, 1134, 1134, 1491]


def main():
    time = int("".join(str(x) for x in t))
    dist = int("".join(str(x) for x in d))

    # Winning holds h satisfy h*(time-h) > dist, i.e. h^2 - time*h + dist < 0.
    # Count the integers strictly between the two roots of that quadratic.
    disc = time * time - 4 * dist
    if disc < 0:
        return 0
    root = math.isqrt(disc)
    lo = (time - root) // 2
    while lo * (time - lo) <= dist:
        lo += 1
    hi = (time + root) // 2
    while hi * (time - hi) <= dist:
        hi -= 1
    return hi - lo + 1


if __name__ == "__main__":
    print(main())
