"""Advent of Code 2024 - Day 24 - Part One"""

from shared import *


def main():
    size = sum([1 for i in process_lines if i[3][0] == "z"])
    res = [-1 for i in range(size)]
    cur_v = dict(init_values)
    while -1 in res:
        for line in process_lines:
            if line[0] in cur_v.keys() and line[2] in cur_v.keys():
                if line[1] == "XOR":
                    cur_v[line[3]] = cur_v[line[0]] ^ cur_v[line[2]]
                if line[1] == "OR":
                    cur_v[line[3]] = cur_v[line[0]] | cur_v[line[2]]
                if line[1] == "AND":
                    cur_v[line[3]] = cur_v[line[0]] & cur_v[line[2]]
                if line[3][0] == "z":
                    res[int(line[3][1:])] = cur_v[line[3]]
    total = 0
    ind = 0
    for i in res:
        total += i * (2**ind)
        ind += 1
    return total


if __name__ == "__main__":
    print(main())
