"""Advent of Code 2023 - Day 12 - Part One"""

import itertools

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().split("\n")))


def n_generate(elist):
    for p in itertools.product([0, 1], repeat=elist.count(2)):
        total = 0
        e = 0
        r = 0
        s = 0
        d = 0
        c = list(elist)
        for ind, i in enumerate(elist):
            if i == 2:
                c[ind] = p[e]
                e += 1
            if c[ind] == 1:
                r += 1
                d = 1
            if c[ind] == 0:
                if d:
                    total += r * (base**s)
                    d = 0
                    r = 0
                    s += 1
        if d:
            total += r * (base**s)
            d = 0
        yield total


def process(line):
    s, items = line.split(" ")
    items = list(map(int, items.split(",")))
    c = []
    for i in s:
        if i == ".":
            c.append(0)
        elif i == "?":
            c.append(2)
        elif i == "#":
            c.append(1)
    found = 0
    target = sum([int(i) * (base**k) for k, i in enumerate(items)])
    for n in n_generate(c):
        if n == target:
            found += 1
    return found


def main():
    res = 0
    for line in data:
        res += process(line)
    print(res)
    return res


if __name__ == "__main__":
    main()
