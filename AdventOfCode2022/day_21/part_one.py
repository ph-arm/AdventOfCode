"""Advent of Code 2022 - Day 21 - Part One"""

import os

test_case = bool(int(os.getenv("AOC_TEST_CASE", "0")))


def main():
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().split("\n")
    monkeys = {}
    running = True
    while running:
        for line in content:
            line_items = line.split(" ")
            if len(line_items) == 2:
                item_key = line_items[0].replace(":", "")
                monkeys[item_key] = int(line_items[1])
            else:
                targets = [x for x in line_items if len(x) == 4]
                if all(item in monkeys.keys() for item in targets):
                    item_key = line_items[0].replace(":", "")
                    monkeys[item_key] = eval(line.split(":")[1], monkeys)

        if "root" in monkeys.keys():
            return int(monkeys["root"])


if __name__ == "__main__":
    print(main())
