"""Advent of Code 2023 - Day 19 - Part One"""

import re

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().split("\n")))


def eval_flow(workflow, x, m, a, s, entry):
    c = workflow[entry]
    for cr in c:
        if cr == "A":
            return 1
        if cr == "R":
            return -1
        if ":" not in cr:
            return eval_flow(workflow, x, m, a, s, cr)
        cond = cr.split(":")[0]
        if eval(cond):
            cl = cr.split(":")[1]
            if cl == "A":
                return 1
            if cl == "R":
                return -1
            return eval_flow(workflow, x, m, a, s, cl)
    return -1


def process_flow(workflow, partsl):
    score = 0
    for i in partsl:
        lres = eval_flow(workflow, i["x"], i["m"], i["a"], i["s"], "in")
        if lres == 1:
            score += sum(i.values())
    return score


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
    res = process_flow(workflow, partsl)
    print(res)
    return res


if __name__ == "__main__":
    main()
