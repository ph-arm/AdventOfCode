"""Advent of Code 2023 - Day 05 - Part One"""


def main():
    INPUT = "./input.txt"
    f = open(INPUT)
    data = f.read().split("\n")
    sdata = data.pop(0)
    seed = list(map(int, sdata.split(":")[1].strip().split(" ")))
    mappings = {}

    def process(data):
        processed = []
        for i in data:
            c = i.split(" ")
            processed.append([int(c[0]), int(c[1]), int(c[2])])
        return processed

    filter_data = []
    started = 0
    for i in data:
        if ":" in i:
            name = i.split(":")[0].split(" ")[0]
            name1 = name.split("-")[0]
            name2 = name.split("-")[2]
            started = 1
            continue
        if started == 1:
            if len(i) > 0:
                filter_data.append(i)
            else:
                mappings[name1] = {name2: process(filter_data)}
                started = 0
                filter_data = []
                continue

    start = "seed"
    current = seed
    while True:
        if start == "location":
            break
        destination = list(mappings[start].keys())[0]
        cmap = mappings[start][destination]
        cproc = []
        for value in current:
            found = 0
            for lmap in cmap:
                if lmap[1] <= value < lmap[1] + lmap[2]:
                    cproc.append(value - lmap[1] + lmap[0])
                    found = 1
                    break
            if not found:
                cproc.append(value)
        start = destination
        current = cproc
    print(current)
    print(min(current))
    return min(current)


if __name__ == "__main__":
    print(main())
