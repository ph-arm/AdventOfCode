"""Advent of Code 2025 - Day 11 - Part Two"""
# part 2 rely on part 1.
# need to find all path from fft to dac, all path from dac to fft, all possible paths to each node, all path from those to to out.
# multiply each path's contribution


def build_graph(input_file):
    """Parse the device list into an adjacency map."""
    graph = {}
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            device, _, outputs = line.partition(": ")
            graph[device] = outputs.split()
    return graph


def count_paths(graph, start, target):
    """Count paths from start to target in the DAG (memoized)."""
    memo = {}

    def dfs(node):
        if node == target:
            return 1
        if node in memo:
            return memo[node]
        total = sum(dfs(nxt) for nxt in graph.get(node, ()))
        memo[node] = total
        return total

    return dfs(start)


def solve_part2(input_file):
    """
    Count paths from 'svr' to 'out' that visit both 'dac' and 'fft'.

    The graph is a DAG (data never flows backwards), so any valid path
    visits the two devices in exactly one order. The two orders are
    mutually exclusive, so the total is the sum of each order's paths,
    where each order's count is the product of its independent segments.
    """
    graph = build_graph(input_file)

    via_fft_then_dac = (
        count_paths(graph, "svr", "fft")
        * count_paths(graph, "fft", "dac")
        * count_paths(graph, "dac", "out")
    )
    via_dac_then_fft = (
        count_paths(graph, "svr", "dac")
        * count_paths(graph, "dac", "fft")
        * count_paths(graph, "fft", "out")
    )

    return via_fft_then_dac + via_dac_then_fft


def test_example():
    """Test with the example from the problem."""
    example = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

    test_file = "test_input2.txt"
    with open(test_file, "w") as f:
        f.write(example)

    result = solve_part2(test_file)
    print(f"Test result: {result}")
    print("Expected: 2")


def main():
    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
