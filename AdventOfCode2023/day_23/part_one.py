"""Advent of Code 2023 - Day 23 - Part One"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
with open(INPUT) as fh:
    grid = [line.strip() for line in fh if line.strip()]

SLOPES = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def neighbours(r, c, slopes):
    rows, cols = len(grid), len(grid[0])
    tile = grid[r][c]
    if slopes and tile in SLOPES:
        dr, dc = SLOPES[tile]
        cand = [(r + dr, c + dc)]
    else:
        cand = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for nr, nc in cand:
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            yield nr, nc


def solve(slopes):
    rows, cols = len(grid), len(grid[0])
    start = (0, grid[0].index("."))
    end = (rows - 1, grid[-1].index("."))

    # Junctions: start, end and any cell with 3+ open neighbours.
    points = [start, end]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            if sum(1 for _ in neighbours(r, c, False)) >= 3:
                points.append((r, c))

    index = {p: i for i, p in enumerate(points)}
    adj = [[] for _ in points]
    for p in points:
        stack = [(p, 0)]
        seen = {p}
        while stack:
            cur, dist = stack.pop()
            if dist and cur in index:
                adj[index[p]].append((index[cur], dist))
                continue
            for nn in neighbours(cur[0], cur[1], slopes):
                if nn not in seen:
                    seen.add(nn)
                    stack.append((nn, dist + 1))

    start_i, end_i = index[start], index[end]
    best = -1
    stack = [(start_i, 0, 1 << start_i)]
    while stack:
        node, dist, mask = stack.pop()
        if node == end_i:
            best = max(best, dist)
            continue
        for nxt, w in adj[node]:
            if not (mask >> nxt) & 1:
                stack.append((nxt, dist + w, mask | (1 << nxt)))
    return best


def main():
    return solve(slopes=True)


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
