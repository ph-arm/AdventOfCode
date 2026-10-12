"""Advent of Code 2022 - Day 11 - Part One"""

import os
import re

test_case = bool(int(os.getenv("AOC_TEST_CASE", "0")))


class Monkey:
    def __init__(self, monkey_content):
        self.items = list(map(int, re.findall("[0-9]+", monkey_content[0])))
        self.monkey_operation = monkey_content[1].split("=")[1]
        self.divisibility = int(re.findall("[0-9]+", monkey_content[2])[0])
        self.monkey_true = int(re.findall("[0-9]+", monkey_content[3])[0])
        self.monkey_false = int(re.findall("[0-9]+", monkey_content[4])[0])
        self.processed = 0

    def round(self, next_items):
        for item in self.items:
            old = item  # noqa: F841 — used inside eval(self.monkey_operation)
            self.processed += 1
            new = eval(self.monkey_operation) // 3
            if new % self.divisibility == 0:
                next_items[self.monkey_true].append(new)
            else:
                next_items[self.monkey_false].append(new)
        self.items = []
        return next_items


def main():
    file = open("./input.txt")
    if test_case:
        file = open("./test_input.txt")

    content = file.read().split("\n")
    monkeys = []
    current_monkey = []
    for line in content[1:]:
        if not line:
            continue
        if line[0] == "M":
            monkeys.append(Monkey(current_monkey))
            current_monkey = []
            continue
        current_monkey.append(line)
    monkeys.append(Monkey(current_monkey))
    number_monkeys = len(monkeys)
    for _round in range(20):
        for monkey in monkeys:
            next_items = [[] for n in range(number_monkeys)]
            next_items = monkey.round(next_items)
            for index, items in enumerate(next_items):
                monkeys[index].items += items
    processed = [monkey.processed for monkey in monkeys]
    processed.sort()
    max_2_processed = processed[-2:]
    print(
        f"the two most active monkey have : {max_2_processed[0]},{max_2_processed[1]}"
    )
    print(max_2_processed[0] * max_2_processed[1])
    return max_2_processed[0] * max_2_processed[1]


if __name__ == "__main__":
    main()
