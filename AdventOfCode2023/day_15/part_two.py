"""Advent of Code 2023 - Day 15 - Part Two"""

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().strip().split(",")))


def hash_this(sl):
    c = 0
    for i in sl:
        e = ord(i)
        c += e
        c = c * 17
        c = c % 256
    return c


def add_item(cur, i, res):
    bin = res[cur]
    header = i.strip().split("=")[0]
    lens = i.strip().split("=")[1]
    if header not in bin[0]:
        bin[0].append(header)
        bin[1].append(lens)
    else:
        ind = bin[0].index(header)
        bin[1][ind] = lens


def remove_item(cur, i, res):
    bin = res[cur]
    header = i.replace("-", "").strip()
    if header in bin[0]:
        ind = bin[0].index(header)
        bin[0].pop(ind)
        bin[1].pop(ind)


def process_input(data):
    res = []
    for _ in range(256):
        a = [[], []]
        res.append(a)

    for i in data:
        if "-" in i:
            cur = hash_this(i.replace("-", "").strip())
            remove_item(cur, i, res)
        else:
            cur = hash_this(i.strip().split("=")[0])
            add_item(cur, i, res)
    return res


def process_score(res):
    score = 0
    for cb, box in enumerate(res):
        for cl, lens in enumerate(box[1]):
            score += int(lens) * (cb + 1) * (cl + 1)
    return score


def main():
    res = process_input(data)
    if test:
        print(res[:5])
    score = process_score(res)
    print(score)
    return score


if __name__ == "__main__":
    main()
