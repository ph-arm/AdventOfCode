"""Advent of Code 2024 - Day 03 - Shared input & utilities"""

import re

f = open("./input.txt")
# f = open("./input_test2.txt", "r")

lines = f.read()
f.close()

# Compile the regex pattern
pattern = re.compile(r"mul\([0-9]+,[0-9]+\)")
pattern2 = re.compile(r"[0-9]+")
# Example string to search
text = "Here are some examples: mul(2,3), mul(4,5), and mul(10,20)."

# Find all matches in the string
matches = pattern.findall(lines)
result = 0
# Print the matches
for match in matches:
    a, b = pattern2.findall(match)
    print(a, b)
    result += int(a) * int(b)
