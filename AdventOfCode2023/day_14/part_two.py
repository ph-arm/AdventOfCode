"""Advent of Code 2023 - Day 14 - Part Two"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
with open(INPUT) as fh:
    data = [line.strip() for line in fh if line.strip()]

TARGET = 1000000000


def roll_left(row):
    # Within each '#'-bounded segment, rocks slide to the front (O sorts > .).
    return "#".join("".join(sorted(seg, reverse=True)) for seg in row.split("#"))


def roll_right(row):
    return "#".join("".join(sorted(seg)) for seg in row.split("#"))


def transpose(grid):
    return ["".join(col) for col in zip(*grid, strict=True)]


def tilt_north(grid):
    return transpose([roll_left(r) for r in transpose(grid)])


def tilt_south(grid):
    return transpose([roll_right(r) for r in transpose(grid)])


def spin_cycle(grid):
    grid = tilt_north(grid)
    grid = [roll_left(r) for r in grid]  # west
    grid = tilt_south(grid)
    grid = [roll_right(r) for r in grid]  # east
    return grid


def north_load(grid):
    rows = len(grid)
    return sum(rows - r for r, row in enumerate(grid) for ch in row if ch == "O")


def main():
    grid = list(data)
    seen = {}
    i = 0
    jumped = False
    while i < TARGET:
        if not jumped:
            key = tuple(grid)
            if key in seen:
                period = i - seen[key]
                i += ((TARGET - i) // period) * period
                jumped = True
                if i >= TARGET:
                    break
            else:
                seen[key] = i
        grid = spin_cycle(grid)
        i += 1
    return north_load(grid)


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
