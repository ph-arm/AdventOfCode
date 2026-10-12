"""Advent of Code 2023 - Day 11 - Part One"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
data = list(map(str.strip, f.read().split("\n")))


def main():
    empty_lines = []
    for row_idx, i in enumerate(data):
        if "#" not in i:
            empty_lines.append(row_idx)

    empty_col = []
    for col_idx in range(len(data[0])):
        to_happend = 1
        for i in data:
            if i[col_idx] == "#":
                to_happend = 0
                break
        if to_happend:
            empty_col.append(col_idx)

    galaxies = []
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))
    distances = 0
    for c, gal in enumerate(galaxies):
        for gal2 in galaxies[c + 1 :]:
            dis = 0
            dis += abs(gal[0] - gal2[0]) + abs(gal[1] - gal2[1])
            dis += sum(
                [
                    1
                    for i in range(min(gal[0], gal2[0]), max(gal[0], gal2[0]))
                    if i in empty_lines
                ]
            )
            dis += sum(
                [
                    1
                    for i in range(min(gal[1], gal2[1]), max(gal[1], gal2[1]))
                    if i in empty_col
                ]
            )
            distances += dis
    print(distances)
    return distances


if __name__ == "__main__":
    main()
