"""Advent of Code 2023 - Day 01 - Part One"""


def main():
    test = 0
    INPUT = "input.txt"
    if test:
        INPUT = "input_sample.txt"
    f = open(INPUT)
    data = f.read().split("\n")
    total = 0
    for line in data:
        line.strip()
        for char in line:
            if char.isdigit():
                total += int(char) * 10
                break
        for char in line[::-1]:
            if char.isdigit():
                total += int(char)
                break

    return total


if __name__ == "__main__":
    print(main())
