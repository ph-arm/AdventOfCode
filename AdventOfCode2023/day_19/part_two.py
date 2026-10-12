"""Advent of Code 2023 - Day 19 - Part Two"""

import re

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().split("\n")))
SIZE = 4000


def eval_flow(workflow, xmax, entry, cv=100):
    c = workflow[entry]
    res = 0
    for cr in c:
        if cr == "A":
            r = 1
            for i in xmax:
                ct = 0
                for j in i:
                    if j == 0:
                        ct += 1
                r *= ct
            return r + res
        if cr == "R":
            return res
        if ":" not in cr:
            return res + eval_flow(workflow, [x[:] for x in xmax], cr)

        cond = cr.split(":")[0]
        cl = cr.split(":")[1]
        if "<" in cond:
            pos = "xmas".index(cond.split("<")[0])
            xmax_copy = xmax[pos][:]
            for c in range(int(cond.split("<")[1]), SIZE + 1):
                xmax_copy[c] = cv
            for c in range(1, int(cond.split("<")[1])):
                xmax[pos][c] = cv
        else:
            pos = "xmas".index(cond.split(">")[0])
            xmax_copy = xmax[pos][:]
            for c in range(1, int(cond.split(">")[1]) + 1):
                xmax_copy[c] = cv
            for c in range(int(cond.split(">")[1]) + 1, SIZE + 1):
                xmax[pos][c] = cv

        if cl == "A":
            r = 1
            for cd, i in enumerate(xmax):
                if cd == pos:
                    i = xmax_copy
                cvvv = 0
                for _, j in enumerate(i):
                    if j == 0:
                        cvvv += 1
                r *= cvvv
            res += r
            continue
        if cl == "R":
            continue
        al = [x[:] for x in xmax]
        al[pos] = xmax_copy
        cv += 1
        res += eval_flow(workflow, al, cl)
    return res


def process_flow(workflow, partsl):
    lres = eval_flow(
        workflow,
        [[-1] + [0] * SIZE, [-1] + [0] * SIZE, [-1] + [0] * SIZE, [-1] + [0] * SIZE],
        "in",
    )
    return lres


def process_input(data):
    workflows = {}
    for c, i in enumerate(data):
        if i.strip() == "":
            break
        f = i.split("{")
        name = f[0].strip()
        f = f[1].replace("}", "")
        f = f.split(",")
        workflows[name] = []
        for j in f:
            workflows[name].append(j)

    partsl = []
    for i in data[c + 1 :]:
        matches = re.findall(r"\d+", i)
        a = {}
        for ci, j in enumerate("xmas"):
            a[j] = int(matches[ci])
        partsl.append(a)
    return workflows, partsl


def main():
    workflow, partsl = process_input(data)
    # workflow = {"in": ["s<100:yolo", "A"], "yolo": ["s>98:R", "A"]}
    res = process_flow(workflow, partsl)
    print(res)
    return res


if __name__ == "__main__":
    main()
