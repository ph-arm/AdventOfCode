"""Advent of Code 2023 - Day 22 - Part One"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
with open(INPUT) as fh:
    data = [line.strip() for line in fh if line.strip()]


def parse(lines):
    bricks = []
    for line in lines:
        a, b = line.split("~")
        x1, y1, z1 = map(int, a.split(","))
        x2, y2, z2 = map(int, b.split(","))
        bricks.append((x1, y1, z1, x2, y2, z2))
    return bricks


def settle(bricks):
    """Drop every brick, returning support / supported-by adjacency sets."""
    bricks = sorted(bricks, key=lambda br: min(br[2], br[5]))
    heights = {}  # (x, y) -> (top_z, brick_index)
    supports = [set() for _ in bricks]
    supported_by = [set() for _ in bricks]
    for i, (x1, y1, z1, x2, y2, z2) in enumerate(bricks):
        cells = [
            (x, y)
            for x in range(min(x1, x2), max(x1, x2) + 1)
            for y in range(min(y1, y2), max(y1, y2) + 1)
        ]
        base = max((heights[c][0] for c in cells if c in heights), default=0)
        for c in cells:
            if c in heights and heights[c][0] == base:
                j = heights[c][1]
                supports[j].add(i)
                supported_by[i].add(j)
        top = base + abs(z2 - z1) + 1
        for c in cells:
            heights[c] = (top, i)
    return supports, supported_by


def main():
    bricks = parse(data)
    supports, supported_by = settle(bricks)
    # A brick is safe if every brick it holds up has another supporter.
    safe = 0
    for i in range(len(bricks)):
        if all(len(supported_by[j]) >= 2 for j in supports[i]):
            safe += 1
    return safe


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
