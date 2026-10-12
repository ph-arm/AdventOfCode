"""Advent of Code 2022 - Day 03 - Part One"""

import string


def main():
    letters = string.ascii_letters
    file = open("./input.txt")
    content = file.read()
    score = 0
    for line in content.split("\n"):
        if not line:
            continue
        first_compartiment = line[: len(line) // 2]
        second_compartiment = line[len(line) // 2 :]
        used = ""
        for letter in first_compartiment:
            if letter in second_compartiment and letter not in used:
                score += letters.index(letter) + 1
                used += letter
                break
    print(f"sum of priorities of misplaced items: {score}")
    return score


if __name__ == "__main__":
    main()

# answer 8105
