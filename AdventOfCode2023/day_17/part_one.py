"""Advent of Code 2023 - Day 17 - Part One"""

import heapq

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
with open(INPUT) as fh:
    grid = [[int(ch) for ch in line.strip()] for line in fh if line.strip()]


def least_heat_loss(lo, hi):
    """Dijkstra over (row, col, axis); axis records the last run's orientation so
    the next straight run is forced perpendicular. Each pop expands lo..hi steps."""
    rows, cols = len(grid), len(grid[0])
    goal = (rows - 1, cols - 1)
    best = {}
    pq = [
        (0, 0, 0, -1)
    ]  # (heat, row, col, axis): axis -1 start, 0 horizontal, 1 vertical
    while pq:
        heat, r, c, axis = heapq.heappop(pq)
        if (r, c) == goal:
            return heat
        if best.get((r, c, axis), heat + 1) < heat:
            continue
        for ax in (0, 1):
            if ax == axis:
                continue
            for sign in (-1, 1):
                cost = heat
                for step in range(1, hi + 1):
                    nr = r + sign * step if ax == 1 else r
                    nc = c + sign * step if ax == 0 else c
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        break
                    cost += grid[nr][nc]
                    if step < lo:
                        continue
                    key = (nr, nc, ax)
                    if cost < best.get(key, cost + 1):
                        best[key] = cost
                        heapq.heappush(pq, (cost, nr, nc, ax))
    return -1


def main():
    return least_heat_loss(1, 3)


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
