"""Advent of Code 2022 - Day 21 - Part Two (optimized)"""

from sympy import solve, symbols

test_case = False


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
            if "humn:" in line:
                continue
            line_items = line.split(" ")
            if len(line_items) == 2:
                item_key = line_items[0].replace(":", "")
                monkeys[item_key] = int(line_items[1])
            else:
                targets = [x for x in line_items if len(x) == 4]
                if all(item in monkeys.keys() for item in targets):
                    item_key = line_items[0].replace(":", "")
                    monkeys[item_key] = eval(line.split(":")[1], monkeys)

        if "gqjg" in monkeys.keys() or "rpjv" in monkeys.keys():
            print(f"gqjg : {monkeys.get('gqjg', '')}")
            print(f"rpjv : {monkeys.get('rpjv', '')}")
            break

    if "gqjg" in monkeys.keys():
        target_key = "rpjv"
        target_value = monkeys["gqjg"]
    else:
        target_key = "gqjg"
        target_value = monkeys["rpjv"]

    running = True
    humn = symbols("humn")
    monkeys["humn"] = humn
    while running:
        for line in content:
            if "humn:" in line:
                continue
            line_items = line.split(" ")
            if len(line_items) == 2:
                item_key = line_items[0].replace(":", "")
                monkeys[item_key] = int(line_items[1])
            else:
                targets = [x for x in line_items if len(x) == 4]
                if all(item in monkeys.keys() for item in targets):
                    item_key = line_items[0].replace(":", "")
                    monkeys[item_key] = eval(line.split(":")[1], monkeys)

        if target_key in monkeys.keys():
            print(f"gqjg : {monkeys.get('gqjg', '')}")
            expr = monkeys[target_key] - target_value
            sol = solve(expr)
            print(sol)
            break


if __name__ == "__main__":
    main()
