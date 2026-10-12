"""Advent of Code 2022 - Day 02 - Part One"""


def play(a, b):
    if a == b:
        return 3
    if (a + 2) % 3 == b:
        return 0
    return 6


def main():
    file = open("./input.txt")
    content = file.read()
    score = 0
    math_conversion = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
    for game in content.split("\n"):
        player_1, player_2 = game.split(" ")
        a = math_conversion[player_1]
        b = math_conversion[player_2]
        score += play(a, b) + b + 1
    print(f"default score is {score}")
    return score
    return 0


if __name__ == "__main__":
    main()

# answer 13005
