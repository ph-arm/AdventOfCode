"""Advent of Code 2024 - Day 13 - Shared input & utilities"""

import re

f = open("./input.txt")
# f = open("./input_test.txt", "r")
# f = open("./par.txt", "r")
lines = f.read()
f.close()
mt = lines.split("\n")

_pattern = re.compile(r"[0-9]+")
problems = []
_cur = []
_count = 0
for _line in mt:
    _count += 1
    if _count % 4 == 0:
        problems.append(_cur)
        _cur = []
        _count = 0
        continue
    _matches = _pattern.findall(_line)
    if _matches:
        _cur.append([int(_matches[0]), int(_matches[1])])
if _cur:
    problems.append(_cur)
