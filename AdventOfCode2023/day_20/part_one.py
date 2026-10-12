"""Advent of Code 2023 - Day 20 - Part One"""

from collections import deque

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
    # A conjunction remembers a low pulse for every module that feeds it.
    for name, mod in modules.items():
        for d in mod["dest"]:
            if d in memory:
                memory[d][name] = False
    return modules, state, memory


def push_button(modules, state, memory):
    """Simulate one button press; return (low_count, high_count)."""
    low = high = 0
    queue = deque([("button", "broadcaster", False)])
    while queue:
        source, target, pulse = queue.popleft()
        if pulse:
            high += 1
        else:
            low += 1

        mod = modules.get(target)
        if mod is None:  # untyped sink module (e.g. output/rx)
            continue

        kind = mod["kind"]
        if kind == "b":
            out = pulse
        elif kind == "%":
            if pulse:  # flip-flops ignore high pulses
                continue
            state[target] = not state[target]
            out = state[target]
        else:  # "&" conjunction
            memory[target][source] = pulse
            out = not all(memory[target].values())

        for d in mod["dest"]:
            queue.append((target, d, out))
    return low, high


def main():
    modules, state, memory = parse(data)
    total_low = total_high = 0
    for _ in range(1000):
        low, high = push_button(modules, state, memory)
        total_low += low
        total_high += high
    return total_low * total_high


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
