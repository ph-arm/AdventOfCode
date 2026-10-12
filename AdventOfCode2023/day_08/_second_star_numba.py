import re
from functools import lru_cache
from time import perf_counter

from numba import jit

f = open("./input.txt")
data = list(map(str.strip, f.read().split("\n")))
pattern = data.pop(0)
data.pop(0)  # remove empty line in input.


def process_nodes(data):
    nodes = {}
    for line in data:
        content = re.findall("[A-Z]+", line)
        nodes[content[0]] = content[1:]
    return nodes


nodes = process_nodes(data)


def profiler(s: str):
    def decorator(method):
        print(s)

        def wrapper_method(*arg, **kw):
            t = perf_counter()
            ret = method(*arg, **kw)
            print(
                "Method "
                + method.__name__
                + " took : "
                + f"{perf_counter() - t:2.5f}"
                + " sec"
            )
            return ret

        return wrapper_method

    return decorator


@lru_cache(maxsize=1000)
def process_run2(start):
    current = start
    steps = []
    step = 0
    for i in pattern:
        step += 1
        if i == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]
        if current[-1] == "Z":
            steps.append(step)
    return steps, current, step


@lru_cache(maxsize=1000)
def process_run(start):
    current = start
    ends = []
    steps = {}
    step = 307 * 30000
    for j in range(30000):
        stepsi, current, stepi = process_run2(current)
        for k in stepsi:
            steps[k + j * 307] = 1
    return ends, steps, current, step


@jit
def check(next_nodes):
    r = len(next_nodes[0])
    if r == 0:
        return False
    for step in next_nodes[0].keys():
        found = True
        for node in next_nodes[1:]:
            if node.get(step, 0) == 0:
                found = False
                break
        if r and found:
            return True


def check2(next_nodes):
    r = len(next_nodes[0])
    if r == 0:
        return False
    for step in next_nodes[0].keys():
        found = True
        for node in next_nodes[1:]:
            if node.get(step, 0) == 0:
                found = False
                break
        if r and found:
            return step


@profiler("starting the recording")
def main():
    node_start = []
    for node in nodes.keys():
        if node[-1] == "A":
            node_start.append([[], [], node, 0])
    total_steps = 0
    rotation = 0
    while 1:
        next_nodes = []
        nodes_steps = []
        for node in node_start:
            ends, steps, end, step = process_run(node[-2])
            next_nodes.append([ends, steps, end, step])
            nodes_steps.append(steps)
        if check(nodes_steps):
            break
        node_start = next_nodes
        if rotation % 100000 == 0:
            print(rotation, total_steps)
        rotation += 1
        total_steps += step
    print(check2(nodes_steps) + total_steps)


if __name__ == "__main__":
    main()
