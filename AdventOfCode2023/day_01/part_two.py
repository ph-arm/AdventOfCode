"""Advent of Code 2023 - Day 01 - Part Two"""


def main():
    test = 0
    INPUT = "input.txt"
    if test:
        INPUT = "input_sample2.txt"
    f = open(INPUT)
    data = f.read().split("\n")
    total = 0
    num_list = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    for _c, line in enumerate(data):
        line.strip()
        indexes = []
        for item in num_list:
            indexes.append(line.find(item))
        v = min([item for item in indexes if item >= 0])
        total += (indexes.index(v) % 10) * 10
        for item in num_list:
            indexes.append(line.rfind(item))
        v = max(indexes)
        total += (indexes.index(v)) % 10
    return total


if __name__ == "__main__":
    print(main())
