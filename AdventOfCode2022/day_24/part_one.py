"""Advent of Code 2022 - Day 24 - Part One"""

import os
from collections import deque

test_case = bool(int(os.getenv("AOC_TEST_CASE", "0")))


def parse(path):
    with open(path) as file:
        grid = [list(line) for line in file.read().split("\n") if line]
    return [row for row in grid if any(c != "#" for c in row)]


def solve(grid, trips):
    height = len(grid)
    width = len(grid[0])
    inner_h = height - 2
    inner_w = width - 2
    start = (0, grid[0].index("."))
    end = (height - 1, grid[height - 1].index("."))

    def blocked(r, c, t):
        if grid[1 + (r - 1 + t) % inner_h][c] == "^":
            return True
        if grid[1 + (r - 1 - t) % inner_h][c] == "v":
            return True
        if grid[r][1 + (c - 1 + t) % inner_w] == "<":
            return True
        if grid[r][1 + (c - 1 - t) % inner_w] == ">":
            return True
        return False

    def bfs(begin, goal, start_time):
        seen = {(begin, start_time)}
        queue = deque([(begin, start_time)])
        while queue:
            (r, c), t = queue.popleft()
            nt = t + 1
            for dr, dc in ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)):
                pos = (r + dr, c + dc)
                nr, nc = pos
                if pos == goal:
                    return nt
                if not (0 <= nr < height and 0 <= nc < width):
                    continue
                if grid[nr][nc] == "#":
                    continue
                if 0 < nr < height - 1 and blocked(nr, nc, nt):
                    continue
                if (pos, nt) in seen:
                    continue
                seen.add((pos, nt))
                queue.append((pos, nt))
        return -1

    points = [start, end, start, end, start]
    t = 0
    for i in range(trips):
        t = bfs(points[i], points[i + 1], t)
    return t


def main():
    path = "./test_input.txt" if test_case else "./input.txt"
    grid = parse(path)
    return solve(grid, 1)


if __name__ == "__main__":
    print(main())
