"""Advent of Code 2023 - Day 21 - Part One"""

from collections import deque

test = 0
if test:
    INPUT = "./input_sample.txt"
    STEPS = 6
else:
    INPUT = "./input.txt"
    STEPS = 64
with open(INPUT) as fh:
    grid = [line.strip() for line in fh if line.strip()]


def main():
    rows, cols = len(grid), len(grid[0])
    start = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "S")
    seen = {start: 0}
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        dist = seen[(r, c)]
        if dist == STEPS:
            continue
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                if (nr, nc) not in seen:
                    seen[(nr, nc)] = dist + 1
                    queue.append((nr, nc))
    # A plot is reachable in exactly STEPS iff it is within STEPS and shares
    # the parity of STEPS.
    return sum(1 for v in seen.values() if v % 2 == STEPS % 2)


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
