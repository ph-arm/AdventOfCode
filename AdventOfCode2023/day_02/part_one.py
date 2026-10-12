"""Advent of Code 2023 - Day 02 - Part One"""


def main():
    f = open("./input.txt")
    data = f.read().split("\n")
    limits = {
        "green": 13,
        "blue": 14,
        "red": 12,
    }

    def works(line):
        jets = line.split(":")[1].split(";")
        for jet in jets:
            items = jet.split(",")
            for item in items:
                item = item.strip()
                k = item.split(" ")[1].strip()
                v = int(item.split(" ")[0])
                if limits[k] < v:
                    return False
        return True

    total = 0
    for c, line in enumerate(data):
        line.strip()
        if works(line):
            total += c + 1
    return total


if __name__ == "__main__":
    print(main())
