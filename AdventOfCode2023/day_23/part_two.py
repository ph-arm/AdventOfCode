"""Advent of Code 2023 - Day 23 - Part Two"""

from part_one import solve


def main():
    # Slopes are treated as normal paths, so every trail is bidirectional.
    return solve(slopes=False)


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
