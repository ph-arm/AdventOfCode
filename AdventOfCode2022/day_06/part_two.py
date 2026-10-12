"""Advent of Code 2022 - Day 06 - Part Two"""

test_set = False


def main():
    file = open("./input.txt")
    content = file.read()
    for index in range(len(content) - 14):
        word = content[index : index + 14]
        if len(word) == len(set(word)):
            return index + 14


if __name__ == "__main__":
    print(main())


# answer 3645
