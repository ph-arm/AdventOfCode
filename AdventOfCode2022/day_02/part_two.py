"""Advent of Code 2022 - Day 02 - Part Two"""

math_conversion = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}


def play(a, b):
    if a == b:
        return 3
    if (a + 2) % 3 == b:
        return 0
    return 6


def oracle(a, b):
    if b == 2:  # player a loose
        return (a + 1) % 3
    if b == 1:  # draw
        return a
    return (a + 2) % 3  #  player a win


def process(content):
    score = 0
    for game in content.split("\n"):
        player_1, result = game.split(" ")
        a = math_conversion[player_1]
        r = math_conversion[result]
        b = oracle(a, r)
        score += play(a, b) + b + 1  # because lazy
    return score


def test():
    content = "A Y\nB X\nC Z"
    process(content)


def main():
    file = open("./input.txt")
    content = file.read()
    return process(content)


if __name__ == "__main__":
    print(main())
