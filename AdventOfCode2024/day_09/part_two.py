"""Advent of Code 2024 - Day 09 - Part Two"""

from shared import *


def main():
    def process_entry_2(entry):
        block = []
        empty_block = []
        index = 0
        value = 0
        for c, i in enumerate(entry):
            if c % 2 == 0:
                block.append([int(i), index, value])
                value += 1
            else:
                empty_block.append([int(i), index])
            index += int(i)
        return block, empty_block

    block, empty_block = process_entry_2(mt)
    found = []
    while len(empty_block) > 1:
        current = empty_block.pop(0)
        size = current[0]
        index = current[1]
        placed = 1
        while size > 0 and placed:
            placed = 0
            for c, i in enumerate(block[::-1]):
                if index > i[1]:
                    break
                if i[0] <= size:
                    size -= i[0]
                    pblock = block.pop(len(block) - c - 1)
                    pblock[1] = index
                    index += i[0]
                    found.append(pblock)
                    placed = 1
                    break

    def calc_sign(item):
        res = 0
        index = item[1]
        for c in range(item[0]):
            res += index * item[2]
            index += 1
        return res

    def calc_sign_2(item):
        return item[2] * item[0] * (2 * item[1] + item[0] - 1) // 2

    sign = 0
    for item in found:
        sign += calc_sign_2(item)
    for item in block:
        sign += calc_sign_2(item)
    return sign


if __name__ == "__main__":
    print(main())
