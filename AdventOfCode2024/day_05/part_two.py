"""Advent of Code 2024 - Day 05 - Part Two"""

import importlib

import shared as _s
from shared import *

# reload shared to get a fresh porder (day_05 part_one consumed it via pop)
importlib.reload(_s)
from shared import *  # noqa: E402


def main():
    def c_rule2(rules, index, stack):
        rule = rules.get(stack[index], [])
        valid = 1
        for i in rule:
            if i in stack[0:index]:
                valid = 0
                fv = i
                break
        if not valid:
            v = stack[index]
            stack[stack.index(fv)] = v
            stack[index] = fv
        return valid

    res = 0

    for c, seqp in enumerate(porder):
        index = 0
        modified = 0
        while len(seqp) > index:
            if not c_rule2(rules, index, seqp):
                index = 0
                modified = 1
                continue
            index += 1
        if modified:
            res += int(seqp[len(seqp) // 2])
    return res


if __name__ == "__main__":
    print(main())
