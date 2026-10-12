"""Advent of Code 2022 - Day 06 - Part One"""

test_set = False


def main():
    file = open("./input.txt")
    content = file.read()
    for index in range(len(content) - 4):
        word = content[index : index + 4]
        if len(word) == len(set(word)):
            return index + 4


if __name__ == "__main__":
    print(main())
