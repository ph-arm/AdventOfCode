"""Advent of Code 2023 - Day 15 - Part One"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().strip().split(",")))


def hash_this(sl):
    c = 0
    for i in sl:
        e = ord(i)
        c += e
        c = c * 17
        c = c % 256
    return c


def process_input(data):
    res = 0
    for i in data:
        res += hash_this(i)
    return res


def main():
    res = process_input(data)
    print(res)
    return res


if __name__ == "__main__":
    main()
