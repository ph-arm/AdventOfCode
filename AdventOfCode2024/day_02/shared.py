"""Advent of Code 2024 - Day 02 - Shared input & utilities"""

# %%

f = open("./input.txt")
# f = open("./input_test.txt", "r")

lines = f.readlines()
f.close()
reports = []
for line in lines:
    if line.strip() == "":
        continue
    reports.append(line.strip())
safe = 0


def safe_up(report):
    for i in range(1, len(report)):
        if (report[i] - report[i - 1]) >= 1 and (report[i] - report[i - 1]) <= 3:
            continue
        return 0
    return 1


def safe_down(report):
    for i in range(1, len(report)):
        if (report[i] - report[i - 1]) >= -3 and (report[i] - report[i - 1]) <= -1:
            continue
        return 0
    return 1
