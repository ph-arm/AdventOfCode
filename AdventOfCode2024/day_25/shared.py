"""Advent of Code 2024 - Day 25 - Shared input & utilities"""

f = open("./input.txt")
# f = open("./input_test.txt", "r")

content = f.read()
blocks = content.strip().split("\n\n")

# A schematic is 7 rows tall; the two solid edge rows leave 5 units of pin space.
SPACE = 5

locks = []  # column-height tuples for schematics whose top row is filled (#####)
keys = []  # column-height tuples for schematics whose top row is empty (.....)


def to_heights(grid):
    """Convert a '#'/'.' schematic into a tuple of per-column heights.

    Each column height is the number of '#' cells minus the one solid edge
    row, so a fully empty pin is 0 and a fully filled column is 6.
    """
    rows = grid.splitlines()
    width = len(rows[0])
    return tuple(sum(row[col] == "#" for row in rows) - 1 for col in range(width))


for block in blocks:
    rows = block.splitlines()
    heights = to_heights(block)
    if set(rows[0]) == {"#"}:  # solid top row -> lock (pins hang down)
        locks.append(heights)
    else:  # empty top row -> key (teeth point up)
        keys.append(heights)
