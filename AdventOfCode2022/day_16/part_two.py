"""Advent of Code 2022 - Day 16 - Part Two"""

import os
import re
from collections import deque

test_case = bool(int(os.getenv("AOC_TEST_CASE", "0")))


def parse(path):
    rates = {}
    tunnels = {}
    pattern = re.compile(
        r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)"
    )
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        match = pattern.match(line)
        rates[match.group(1)] = int(match.group(2))
        tunnels[match.group(1)] = match.group(3).split(", ")
    return rates, tunnels


def distances(tunnels):
    dist = {}
    for src in tunnels:
        seen = {src: 0}
        queue = deque([src])
        while queue:
            u = queue.popleft()
            for v in tunnels[u]:
                if v not in seen:
                    seen[v] = seen[u] + 1
                    queue.append(v)
        dist[src] = seen
    return dist


def best_pressures(path, total_time):
    rates, tunnels = parse(path)
    dist = distances(tunnels)
    useful = [v for v in rates if rates[v] > 0]
    idx = {v: i for i, v in enumerate(useful)}
    best = {}

    def dfs(cur, time_left, mask, released):
        if released > best.get(mask, -1):
            best[mask] = released
        for v in useful:
            bit = 1 << idx[v]
            if mask & bit:
                continue
            remaining = time_left - dist[cur][v] - 1
            if remaining <= 0:
                continue
            dfs(v, remaining, mask | bit, released + remaining * rates[v])

    dfs("AA", total_time, 0, 0)
    return best


def main():
    path = "./test_input.txt" if test_case else "./input.txt"
    best = best_pressures(path, 26)
    # You and the elephant open disjoint sets of valves.
    items = sorted(best.items(), key=lambda kv: kv[1], reverse=True)
    answer = 0
    for i, (mask1, pressure1) in enumerate(items):
        if pressure1 * 2 <= answer:
            break
        for mask2, pressure2 in items[i:]:
            if pressure1 + pressure2 <= answer:
                break
            if mask1 & mask2 == 0:
                answer = pressure1 + pressure2
    return answer


if __name__ == "__main__":
    print(main())
