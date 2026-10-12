"""Advent of Code 2024 - Day 24 - Shared input & utilities"""

import re

test = 1
f = open("./input.txt")
# f = open("./input_test.txt", "r")

content = f.read()
mt = content.split("\n")
init_values = {}
process_lines = []
pattern = re.compile(r"\b\w{3}\b|XOR|OR|AND")

for line in mt:
    if ":" in line:
        key, value = line.split(":")
        init_values[key.strip()] = int(value.strip())
    if ">" in line:
        matches = pattern.findall(line)
        process_lines.append(matches)
