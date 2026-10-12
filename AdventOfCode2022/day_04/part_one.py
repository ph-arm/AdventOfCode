"""Advent of Code 2022 - Day 04 - Part One"""


def main():
    file = open("./input.txt")
    content = file.read()
    score = 0
    for line in content.split("\n"):
        if not line:
            continue
        first_pair, second_pair = line.split(",")
        first_low, first_high = map(int, first_pair.split("-"))
        second_low, second_high = map(int, second_pair.split("-"))
        if (first_low <= second_low and first_high >= second_high) or (
            first_low >= second_low and first_high <= second_high
        ):
            score += 1

    print(f"sum of mispaired included: {score}")
    return score


if __name__ == "__main__":
    main()

# answer 644
