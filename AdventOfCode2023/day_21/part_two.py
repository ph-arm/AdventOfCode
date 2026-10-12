"""Advent of Code 2023 - Day 21 - Part Two"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
with open(INPUT) as fh:
    grid = [line.strip() for line in fh if line.strip()]


def find_start(g):
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            if ch == "S":
                return (r, c)
    raise ValueError("no start found")


def reach(steps, g, start):
    """Count plots reachable in exactly `steps` on the infinite (wrapping) grid.

    Key insight: a plot first reached at distance d can be re-reached at every
    later step of the same parity (pace one tile back and forth). So the answer
    is simply the number of plots whose shortest distance has the same parity as
    `steps`. We flood outward once and bucket each plot by that parity.
    """
    rows, cols = len(g), len(g[0])
    seen = {start}
    current = {start}  # frontier: plots first reached at the previous step
    counts = [1, 0]  # plots settled per distance parity (index = distance % 2)
    for step in range(1, steps + 1):
        nxt = set()
        for r, c in current:
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                # Modulo wraps into the tiled copies of the base grid.
                if g[nr % rows][nc % cols] != "#" and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    nxt.add((nr, nc))
        counts[step % 2] += len(nxt)  # tally newly-settled plots by their parity
        current = nxt
    return counts[steps % 2]


def main():
    # 26501365 = 65 + 131 * 202300: the start sits dead-centre of a 131-wide grid
    # with a clear centre row/col and empty border, so the reachable region grows
    # as a perfect diamond and the plot count is a quadratic in x, the number of
    # whole grid-widths the frontier has crossed.
    start = find_start(grid)
    size = len(grid)  # 131 on the real input
    target = 26501365
    x = target // size  # 202300: whole grid-widths the frontier reaches
    rem = target % size  # 65: steps from S out to the grid edge
    # Sample the quadratic at x = 0, 1, 2 (i.e. rem, rem + size, rem + 2*size).
    y0 = reach(rem, grid, start)
    y1 = reach(rem + size, grid, start)
    y2 = reach(rem + 2 * size, grid, start)
    # Recover f(x) = a*x^2 + b*x + c from those three samples via finite
    # differences: c = f(0); 2a = second difference (y2 - 2*y1 + y0); b = f(1) - c - a.
    a = (y2 - 2 * y1 + y0) // 2
    b = y1 - y0 - a
    c = y0
    return a * x * x + b * x + c


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
