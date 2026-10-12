"""Advent of Code 2024 - Day 05 - Part One"""

from shared import *


def main():
    def checking_rule(rule, stack):
        if len(stack) == 0:
            return 1
        for i in rule:
            if i in stack:
                return 0
        return 1

    res = 0

    for seqp in porder:
        v_add = int(seqp[len(seqp) // 2])
        current = seqp.pop(0)
        stack = []
        working = v_add
        while len(seqp) > 0:
            if checking_rule(rules[current], stack):
                stack.append(current)
                current = seqp.pop(0)
            else:
                working = 0
                break
        res += working
    return res


if __name__ == "__main__":
    print(main())
