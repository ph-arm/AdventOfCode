"""Advent of Code 2022 - Day 13 - Part Two"""

from functools import cmp_to_key

test_case = False


def mocked_content():
    pass


def main():
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().split("\n")
    list_of_signals = []

    for line in content:
        if not line:
            continue
        list_of_signals.append([eval(line), 0])

    def comp(a, b):
        if isinstance(a, int) and not isinstance(b, int):
            return comp([a], b)
        if not isinstance(a, int) and isinstance(b, int):
            return comp(a, [b])
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return 1
            if a == b:
                return 0
            if a > b:
                return -1
        if len(a) > len(b):
            for index in range(len(b)):
                c = comp(a[index], b[index])
                if c == 0:
                    continue
                return c
            return -1
        if len(a) < len(b):
            for index in range(len(a)):
                c = comp(a[index], b[index])
                if c == 0:
                    continue
                return c
            return 1
        for index in range(len(a)):
            c = comp(a[index], b[index])
            if c == 0:
                continue
            return c
        return 0

    def compare(a, b):
        return -comp(a[0], b[0])

    list_of_signals.append([[[2]], 1])
    list_of_signals.append([[[6]], 1])
    list_of_signals.sort(key=cmp_to_key(compare))
    res = 1
    for index, signal in enumerate(list_of_signals):
        if signal[1] == 1:
            res *= index + 1
    return res


if __name__ == "__main__":
    print(main())
