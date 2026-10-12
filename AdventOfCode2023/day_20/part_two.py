"""Advent of Code 2023 - Day 20 - Part Two"""

from collections import deque
from math import lcm

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
with open(INPUT) as fh:
    data = [line.strip() for line in fh if line.strip()]


def parse(lines):
    """Build the module graph plus flip-flop and conjunction state."""
    modules = {}
    for line in lines:
        left, right = line.split(" -> ")
        dest = right.split(", ")
        if left == "broadcaster":
            modules["broadcaster"] = {"kind": "b", "dest": dest}
        else:
            modules[left[1:]] = {"kind": left[0], "dest": dest}

    state = {name: False for name, m in modules.items() if m["kind"] == "%"}
    memory = {name: {} for name, m in modules.items() if m["kind"] == "&"}
    for name, mod in modules.items():
        for d in mod["dest"]:
            if d in memory:
                memory[d][name] = False
    return modules, state, memory


def main():
    modules, state, memory = parse(data)

    # rx is fed by one conjunction that emits low only when all of its own
    # inputs are high on the same press; each input cycles independently, so
    # the answer is the LCM of each input's first high-pulse press count.
    feeder = next(n for n, m in modules.items() if "rx" in m["dest"])
    watched = set(memory[feeder])
    cycles = {}

    presses = 0
    while len(cycles) < len(watched):
        presses += 1
        queue = deque([("button", "broadcaster", False)])
        while queue:
            source, target, pulse = queue.popleft()
            if target == feeder and pulse and source not in cycles:
                cycles[source] = presses

            mod = modules.get(target)
            if mod is None:
                continue
            kind = mod["kind"]
            if kind == "b":
                out = pulse
            elif kind == "%":
                if pulse:
                    continue
                state[target] = not state[target]
                out = state[target]
            else:  # "&" conjunction
                memory[target][source] = pulse
                out = not all(memory[target].values())

            for d in mod["dest"]:
                queue.append((target, d, out))

    return lcm(*cycles.values())


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
