"""Advent of Code 2023 - Day 06 - Part One"""

t = [44, 70, 70, 80]
d = [283, 1134, 1134, 1491]


def main():
    def find_lower(ti, di):
        lower = int(di / ti)
        for i in range(lower, ti):
            v = i
            d = v * (ti - i)
            if d > di:
                return i
        return -1

    def find_higher(ti, di):
        for i in range(ti):
            v = ti - i
            d = v * i
            if d > di:
                return ti - i
        return -1

    res = []
    for i in range(len(t)):
        m = find_lower(t[i], d[i])
        h = find_higher(t[i], d[i])
        res.append(h - m + 1)
    result = 1
    for i in res:
        result *= i
    return result


if __name__ == "__main__":
    print(main())
