"""Advent of Code 2024 - Day 09 - Part One"""

from shared import *


def main():
    sign = 0
    block = []
    empty_block = []
    for c, i in enumerate(mt):
        if c % 2 == 0:
            block.append(int(i))
        else:
            empty_block.append(int(i))

    i = 0
    ib = len(block)
    p = 0
    rem = 0
    while i < len(block) and ib > 0 and ib > i:
        c = block[i]
        for j in range(c):
            sign += p * i
            p += 1

        to_add = empty_block[i]
        while to_add > 0:
            if rem == 0:
                ib -= 1
                rem = block[ib]
            sign += p * ib
            to_add -= 1
            rem -= 1
            p += 1
        i += 1
    while rem > 0:
        sign += p * ib
        rem -= 1
        p += 1
    return sign


if __name__ == "__main__":
    print(main())
