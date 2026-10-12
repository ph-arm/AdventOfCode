"""Advent of Code 2023 - Day 04 - Part Two"""


def main():
    test = 0
    INPUT = "input.txt"
    if test:
        INPUT = "input_sample.txt"
    f = open(INPUT)
    data = f.readlines()
    data = [item.strip() for item in data]
    result = [1] * len(data)
    for c, line in enumerate(data):
        line = line.split(":")[1]
        win_nums = [int(item) for item in line.split("|")[0].strip().split(" ") if item]
        nums = [int(item) for item in line.split("|")[1].strip().split(" ") if item]
        indice = 1
        for num in nums:
            if num in win_nums:
                result[c + indice] += result[c]
                indice += 1
    return sum(result)


if __name__ == "__main__":
    print(main())
