"""Advent of Code 2023 - Day 08 - Part One"""

import re

f = open("./input.txt")
data = list(map(str.strip, f.read().split("\n")))


def process_run(pattern, nodes, start):
    current = start
    step = 0
    for i in pattern:
        step += 1
        if i == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]
        if current == "ZZZ":
            return current, step
    return current, step


def process_nodes(data):
    nodes = {}
    for line in data:
        content = re.findall("[A-Z]+", line)
        nodes[content[0]] = content[1:]
    return nodes


def main():
    pattern = data.pop(0)
    data.pop(0)  # remove empty line in input.
    nodes = process_nodes(data)
    start = "AAA"
    steps = 0
    while 1:
        end, step = process_run(pattern, nodes, start)
        steps += step
        if end == "ZZZ":
            break
        start = end

    print(steps)
    return steps


if __name__ == "__main__":
    main()
