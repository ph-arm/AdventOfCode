"""Advent of Code 2022 - Day 21 - Part Two"""

from fractions import Fraction

test_case = False


def evaluate(content, humn_val):
    """Evaluate all monkeys with a given humn value; returns the monkeys dict."""
    monkeys = {"humn": humn_val}
    changed = True
    while changed:
        changed = False
        for line in content:
            if "humn:" in line:
                continue
            line_items = line.split(" ")
            key = line_items[0].replace(":", "")
            if key in monkeys:
                continue
            if len(line_items) == 2:
                monkeys[key] = Fraction(line_items[1])
                changed = True
            else:
                a, op, b = line_items[1], line_items[2], line_items[3]
                if a in monkeys and b in monkeys:
                    if op == "+":
                        monkeys[key] = monkeys[a] + monkeys[b]
                    elif op == "-":
                        monkeys[key] = monkeys[a] - monkeys[b]
                    elif op == "*":
                        monkeys[key] = monkeys[a] * monkeys[b]
                    elif op == "/":
                        monkeys[key] = monkeys[a] / monkeys[b]
                    changed = True
    return monkeys


def main():
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().split("\n")

    # Find the two children of root
    root_line = next(line for line in content if line.startswith("root:"))
    root_items = root_line.split()
    lhs_key, rhs_key = root_items[1], root_items[3]

    # The expression is linear in humn; evaluate at two points to solve
    m0 = evaluate(content, Fraction(0))
    m1 = evaluate(content, Fraction(1))

    diff0 = m0[lhs_key] - m0[rhs_key]  # f(0)
    diff1 = m1[lhs_key] - m1[rhs_key]  # f(1)
    slope = diff1 - diff0  # change per unit humn

    # Solve: diff0 + slope * humn = 0
    humn = -diff0 / slope
    print(int(humn))
    return int(humn)


if __name__ == "__main__":
    main()
