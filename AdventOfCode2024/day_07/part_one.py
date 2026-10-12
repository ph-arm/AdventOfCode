"""Advent of Code 2024 - Day 07 - Part One"""

import itertools

from shared import *


def main():
    def testing(res, nums):
        nums = list(map(int, nums))
        n = len(nums) - 1
        for perm in itertools.product(["+", "x"], repeat=n):
            ans = nums[0]
            for c, item in enumerate(perm):
                if item == "+":
                    ans += nums[c + 1]
                else:
                    ans *= nums[c + 1]
            if res == ans:
                return ans
        return 0

    total = 0
    for line in mt:
        line = line.split(" ")
        res = int(line[0][:-1])
        total += testing(res, line[1:])
    return total


if __name__ == "__main__":
    print(main())
