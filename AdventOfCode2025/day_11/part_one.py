"""Advent of Code 2025 - Day 11 - Part One"""


def solve_part1(input_file):
    """
    Count all paths from 'you' to 'out' in the device graph.

    Since the answer was "too low", maybe we need to count paths
    that can revisit nodes (as long as we don't have infinite loops).
    Let's use memoization but allow revisiting nodes.
    """
    with open(input_file) as f:
        lines = [line.strip() for line in f if line.strip()]

    # Build adjacency list graph
    graph = {}
    for line in lines:
        parts = line.split(": ")
        device = parts[0]
        if len(parts) > 1:
            outputs = parts[1].split()
            graph[device] = outputs
        else:
            graph[device] = []

    # Count paths with cycle detection per path
    def count_paths_dfs(current, target, visited):
        """Count all simple paths (no cycles) from current to target."""
        if current == target:
            return 1

        if current in visited:
            return 0  # Avoid cycles in this path

        if current not in graph:
            return 0

        visited.add(current)
        total_paths = 0
        for neighbor in graph[current]:
            total_paths += count_paths_dfs(neighbor, target, visited)
        visited.remove(current)

        return total_paths

    return count_paths_dfs("you", "out", set())


def test_example():
    """Test with the example from the problem."""
    example = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
ccc: ddd eee fff"""

    test_file = "test_input.txt"
    with open(test_file, "w") as f:
        f.write(example)

    result = solve_part1(test_file)
    print(f"Test result: {result}")
    print("Expected: 5")


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
