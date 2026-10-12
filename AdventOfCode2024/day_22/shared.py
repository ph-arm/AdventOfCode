"""Advent of Code 2024 - Day 22 - Shared input & utilities"""

test = 1
f = open("./input.txt")
# f = open("./input_test.txt", "r")

content = f.read()
mt = content.split("\n")


def m64(a):
    res = (a ^ (64 * a)) % 16777216
    return res


def d32(a):
    res = (a ^ (a // 32)) % 16777216
    return res


def m2048(a):
    res = (a ^ (2048 * a)) % 16777216
    return res


def process_num(a):
    res = m64(a)
    res = d32(res)
    res = m2048(res)
    return res


r = [
    15887950,
    16495136,
    527345,
    704524,
    1553684,
    12683156,
    11100544,
    12249484,
    7753432,
    5908254,
]
for i in range(1, len(r)):
    if not (process_num(r[i - 1]) == r[i]):
        raise Exception(f"Error at {i}")


def n2000(a):
    res = a
    for i in range(2000):
        res = process_num(res)
    return res
