"""Advent of Code 2023 - Day 14 - Part One"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().split("\n")))


def process_input(data):
    res = []
    for i in data:
        res.append(list(i.strip()))
    return res


def process_plate(plate):
    plate_len = len(plate)
    p = plate[::-1]
    p.append(len(plate[0]) * "#")
    for c, line in enumerate(p[:-1]):
        for i in range(len(line)):
            if line[i] == "O":
                for ci in range(c + 1, plate_len):
                    if p[ci][i] == ".":
                        p[ci][i] = "O"
                        p[c][i] = "."
                        break
                    if p[ci][i] == "#":
                        break
    return p


def main():
    plate = process_input(data)
    res = 0
    transformed = process_plate(plate)

    for c, line in enumerate(transformed):
        for item in line:
            if item == "O":
                res += c + 1
    for i in transformed:
        print(i)
    print(res)
    return res


if __name__ == "__main__":
    main()
