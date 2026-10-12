"""Advent of Code 2024 - Day 03 - Part Two"""

from shared import *


def main():
    pattern = re.compile(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))")
    pattern2 = re.compile(r"[0-9]+")

    # Find all matches for each pattern in the string
    result = 0
    matches = pattern.findall(lines)
    # Print the matches
    state = 1
    for match in matches:
        match = "".join(match)
        if "do" in match:
            if match == "do()":
                state = 1
            else:
                state = 0
            continue
        a, b = pattern2.findall(match)
        result += int(a) * int(b) * state
    return result


if __name__ == "__main__":
    print(main())
