"""Advent of Code 2022 - Day 03 - Part Two"""

import string


def check_individual_elve(elves, letter):
    truth = 1
    for elve in elves:
        truth *= elve.get(letter, 0)
    if truth >= 1:
        return True
    return False


def main():
    letters = string.ascii_letters
    file = open("./input.txt")
    content = file.read()
    score = 0
    line_count = 0
    current_elves = []
    for line in content.split("\n"):
        line_count += 1
        current_elves.append(line)
        if line_count % 3 != 0:  # buffer 3 lines
            continue
        elves_count = []
        for elve in current_elves:
            elve_count = {}
            for letter in elve:
                elve_count[letter] = 1 + elve_count.get(letter, 0)
            elves_count.append(elve_count)
        for letter in current_elves[0]:
            if check_individual_elve(elves_count, letter):
                score += letters.index(letter) + 1
                break
        current_elves = []

    print(f"total priority of badges : {score}")
    return score


if __name__ == "__main__":
    main()

# answer 2363
