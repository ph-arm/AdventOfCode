"""Advent of Code 2024 - Day 11 - Part Two"""

from collections import Counter


def blink(counts):
    nxt = Counter()
    for stone, n in counts.items():
        if stone == 0:
            nxt[1] += n
            continue
        s = str(stone)
        if len(s) % 2 == 0:  # even digit count splits into two stones
            half = len(s) // 2
            nxt[int(s[:half])] += n
            nxt[int(s[half:])] += n
        else:
            nxt[stone * 2024] += n
    return nxt


def count_after(counts, blinks):
    for _ in range(blinks):
        counts = blink(counts)
    return sum(counts.values())


def main():
    with open("input.txt") as f:
        stones = Counter(int(x) for x in f.read().split())
    return count_after(stones, 75)


if __name__ == "__main__":
    print(main())
