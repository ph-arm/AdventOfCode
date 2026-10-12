"""Advent of Code 2023 - Day 03 - Part Two"""


def main():
    test = 0
    INPUT = "input.txt"
    if test:
        INPUT = "input_sample.txt"
    f = open(INPUT)
    data = f.readlines()
    data = list(map(str.strip, data))
    ll = len(data[0]) - 1

    def process(word, item, c):
        ym = max(min(item) - 1, 0)
        ymax = min(max(item) + 1, ll)
        for i in range(ym, ymax + 1):
            for ci in range(max(c - 1, 0), min(c + 2, len(data))):
                if data[ci][i] == "*":
                    return ci * 1000 + i
        return False

    total = {}
    for c, line in enumerate(data):
        line.strip()
        items = []
        current = False
        word = ""
        for c2, char in enumerate(line):
            if char.isdigit():
                if current:
                    word += char
                else:
                    current = True
                    word = char
                items.append(c2)
                if c2 != len(line) - 1:
                    continue
            if current:
                r = process(word, items, c)
                if r:
                    cur = total.get(r, [])
                    cur.append(int(word))
                    total[r] = cur
                    # print(total)
                current = False
                items = []
    result = 0
    for k, v in total.items():
        if len(v) == 2:
            print(k, v)
            result += v[0] * v[1]
    return result


if __name__ == "__main__":
    print(main())
