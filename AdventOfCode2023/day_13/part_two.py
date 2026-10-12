"""Advent of Code 2023 - Day 13 - Part Two"""

import numpy as np

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().split("\n")))


def process_input(data):
    temp = []
    res = []
    for i in data:
        if i.strip() == "":
            res.append(temp)
            temp = []
            continue
        temp.append(list(i))
    return res


def process_test(a, b):
    co = 0
    for i in range(len(a)):
        for c, j in enumerate(a[i]):
            if j != b[i][c]:
                if co:
                    return 0
                co += 1
    if co:
        return 1
    return 0


def process_vertical(item, y):
    res = 0
    for i in range(1, y):
        a = min(i, y - i)
        if a == i:
            g = item[:i][::-1]
            right = item[i : 2 * i]
            res = res + process_test(g, right) * i
        else:
            g = item[i - a : i][::-1]
            right = item[i:]
            res = res + process_test(g, right) * i
    return res


def process_item(item):
    x = len(item[0])
    y = len(item)
    r = process_vertical(item, y)
    item_T = np.array(item).T
    k = process_vertical(item_T, x)
    return r * 100 + k


def main():
    training_set = process_input(data)
    res = 0
    for item in training_set:
        # print(item)
        res += process_item(item)
    print(res)
    return res


if __name__ == "__main__":
    main()
