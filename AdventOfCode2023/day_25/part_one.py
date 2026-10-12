"""Advent of Code 2023 - Day 25 - Part One"""

from collections import defaultdict, deque

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
with open(INPUT) as fh:
    data = [line.strip() for line in fh if line.strip()]


def parse(lines):
    adj = defaultdict(set)
    for line in lines:
        name, rest = line.split(":")
        name = name.strip()
        for other in rest.split():
            adj[name].add(other)
            adj[other].add(name)
    return adj


def min_cut_component(adj, source, sink):
    """Edmonds-Karp on unit capacities; return the source side if the min cut
    is exactly 3, else None."""
    cap = {}
    for u in adj:
        for v in adj[u]:
            cap[(u, v)] = 1
    flow = 0
    while flow <= 3:
        parent = {source: None}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in parent and cap[(u, v)] > 0:
                    parent[v] = u
                    queue.append(v)
        if sink not in parent:  # no augmenting path left
            return set(parent) if flow == 3 else None
        node = sink
        while parent[node] is not None:
            prev = parent[node]
            cap[(prev, node)] -= 1
            cap[(node, prev)] += 1
            node = prev
        flow += 1
    return None


def main():
    adj = parse(data)
    nodes = list(adj)
    total = len(nodes)
    source = max(nodes, key=lambda n: len(adj[n]))
    for sink in nodes:
        if sink == source:
            continue
        side = min_cut_component(adj, source, sink)
        if side and 1 < len(side) < total:
            return len(side) * (total - len(side))
    return None


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
