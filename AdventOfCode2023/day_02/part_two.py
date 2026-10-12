"""Advent of Code 2023 - Day 02 - Part Two"""


def main():
    f = open("./input.txt")
    data = f.read().split("\n")

    def works(line):
        jets = line.split(":")[1].split(";")
        res = {}
        for jet in jets:
            items = jet.split(",")
            for item in items:
                item = item.strip()
                k = item.split(" ")[1].strip()
                v = int(item.split(" ")[0])
                res[k] = max(res.get(k, 0), v)
        c = 1
        print(res)
        for _, v in res.items():
            c *= v
        return c

    total = 0
    for _c, line in enumerate(data):
        line.strip()
        total += works(line)
    return total


if __name__ == "__main__":
    print(main())
