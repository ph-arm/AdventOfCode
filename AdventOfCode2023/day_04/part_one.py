"""Advent of Code 2023 - Day 04 - Part One"""


def main():
    test = 0
    INPUT = "input.txt"
    if test:
        INPUT = "input_sample.txt"
    f = open(INPUT)
    data = f.readlines()
    data = [item.strip() for item in data]
    total = 0
    for line in data:
        current = 0
        line = line.split(":")[1]
        win_nums = [int(item) for item in line.split("|")[0].strip().split(" ") if item]
        nums = [int(item) for item in line.split("|")[1].strip().split(" ") if item]
        print(nums)
        for num in nums:
            if num in win_nums:
                print("win")
                current = 2 * current if current else 1
        total += current
    return total


if __name__ == "__main__":
    print(main())
