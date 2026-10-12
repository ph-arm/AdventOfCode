"""Advent of Code 2024 - Day 24 - Part Two"""

from shared import *


def main():
    wire_op = {}  # output -> (a, op, b)
    wire_uses = {}  # wire -> list of ops that consume it
    for a, op, b, out in [line for line in process_lines]:
        wire_op[out] = (a, op, b)
        wire_uses.setdefault(a, []).append(op)
        wire_uses.setdefault(b, []).append(op)

    swapped = set()
    num_bits = (
        sum(1 for line in process_lines if line[3][0] == "z") - 1
    )  # exclude final carry

    for out, (a, op, b) in wire_op.items():
        # Rule 1: z-wires (not the last carry) must come from XOR
        if out.startswith("z") and out != f"z{num_bits:02d}" and op != "XOR":
            swapped.add(out)

        # Rule 2: internal XOR gates (non-x/y inputs) must output a z-wire
        if (
            op == "XOR"
            and not (a[0] in "xy" or b[0] in "xy")
            and not out.startswith("z")
        ):
            swapped.add(out)

        # Rule 3: AND gates (except the first half-adder) must feed only into OR
        if op == "AND" and {a, b} != {"x00", "y00"}:
            uses = wire_uses.get(out, [])
            if uses and any(u != "OR" for u in uses):
                swapped.add(out)

        # Rule 4: XOR gates with x/y inputs must feed only into XOR or AND (not OR)
        if op == "XOR" and (a[0] in "xy" or b[0] in "xy") and not out.startswith("z"):
            uses = wire_uses.get(out, [])
            if uses and any(u == "OR" for u in uses):
                swapped.add(out)
    return ",".join(sorted(swapped))


if __name__ == "__main__":
    print(main())
