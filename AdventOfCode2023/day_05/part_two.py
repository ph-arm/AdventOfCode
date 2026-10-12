"""Advent of Code 2023 - Day 05 - Part Two"""


def main():
    INPUT = "./input.txt"
    f = open(INPUT)
    data = f.read().split("\n")
    sdata = data.pop(0)
    seed = list(map(int, sdata.split(":")[1].strip().split(" ")))
    seeds = []
    for i in range(len(seed)):
        if i % 2 == 0:
            seeds.append([seed[i], seed[i + 1]])
    seed = seeds

    mappings = {}

    def process(data):
        processed = []
        for i in data:
            c = i.split(" ")
            processed.append([int(c[0]), int(c[1]), int(c[2])])
        processed = sorted(processed, key=lambda value: value[1])
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
        for pairs in current:
            vtop = pairs[0] + pairs[1]
            vmin = pairs[0]
            for lmap in cmap:
                # 3 cases:
                max_lmap = lmap[1] + lmap[2]
                if vtop < lmap[1]:
                    cproc.append([vmin, vtop - vmin])
                    break
                if vmin < lmap[1] and vtop > lmap[1]:
                    npair_vmin = vmin
                    npair_vtop = lmap[1]
                    cproc.append([npair_vmin, npair_vtop - npair_vmin])
                    vmin = lmap[1]

                if lmap[1] <= vmin < lmap[1] + lmap[2]:
                    npair_vmin = vmin - lmap[1] + lmap[0]
                    if vtop <= lmap[1] + lmap[2]:
                        npair_vtop = vtop - lmap[1] + lmap[0]
                        cproc.append([npair_vmin, npair_vtop - npair_vmin])
                        break
                    else:
                        cproc.append([npair_vmin, lmap[0] + lmap[2] - npair_vmin])
                        vmin = lmap[1] + lmap[2]
            if vtop > max_lmap:
                cproc.append([max_lmap, vtop - max_lmap])
        start = destination
        current = cproc
    res = []
    for i in current:
        res.append(i[0])
    return min(res)


if __name__ == "__main__":
    print(main())
