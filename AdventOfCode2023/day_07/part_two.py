"""Advent of Code 2023 - Day 07 - Part Two"""

test = 0
INPUT = "./input.txt"
if test == 1:
    INPUT = "./input_sample.txt"
f = open(INPUT)
data = list(map(str.strip, f.read().split("\n")))
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
}


def process(heads):
    multiplier = 1
    hset = {}
    rv = [values[i] for i in heads]
    for i in rv:
        if i in hset:
            hset[i] += 1
        else:
            hset[i] = 1
    res = 0
    pair = 0
    if 1 in rv:
        n = hset[1]
        hset[1] = 0
        key_list = list(hset.keys())
        val_list = list(hset.values())
        position = val_list.index(max(val_list))
        hset[key_list[position]] = max(hset.values()) + n
    for _k, v in hset.items():
        if v == 2:
            multiplier = 100000000 * (10**pair)
            pair += 1
            res += multiplier
        if v == 3:
            multiplier = 10000000000
            res += multiplier
        if v == 4:
            multiplier = 100000000000
            res += multiplier
        if v == 5:
            multiplier = 1000000000000
            res += multiplier
    c = 0
    for i in rv[::-1]:
        res += (15**c) * i
        c += 1
    return res


def main():
    hands = {}
    results = []
    for line in data:
        hands[line.split(" ")[0]] = int(line.split(" ")[1])
    for key, value in hands.items():
        r = process(key)
        results.append([r, key, value])
    results.sort(key=lambda x: x[0])
    total = 0
    item = 1
    for i in results:
        total += item * i[2]
        item += 1
    print(total)
    return total


if __name__ == "__main__":
    main()

# ['2257A', 438]    ['22343', 845]
