"""Advent of Code 2025 - Day 07 - Part Two"""


def solve_part2(input_file):
    """
    Count the number of unique timelines (unique paths through splitters).

    Each time a particle hits a splitter, the timeline splits into two.
    We need to count the total number of distinct timelines (paths).

    Key insight: From any position (row, col), we can compute the number of
    distinct paths that emerge. Use memoization on just (row, col) without
    tracking history, since each position has a fixed number of paths forward.
    """
    with open(input_file) as f:
        grid = [line.rstrip("\n") for line in f]

    # Find starting position
    start_row, start_col = None, None
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "S":
                start_row, start_col = r, c
                break
        if start_row is not None:
            break

    # Memoization: (row, col) -> number of paths from this position
    memo = {}

    def count_paths_from(row, col):
        """
        Count the number of distinct timelines/paths from this position.
        """
        if (row, col) in memo:
            return memo[(row, col)]

        # Move downward until we hit a splitter or exit
        current_row = row

        while True:
            current_row += 1

            # Check if we exit
            if current_row >= len(grid):
                # Exited bottom - this is 1 timeline
                memo[(row, col)] = 1
                return 1
            if col < 0 or col >= len(grid[current_row]):
                # Exited sides - this is 1 timeline
                memo[(row, col)] = 1
                return 1

            char = grid[current_row][col]

            if char == "^":
                # Hit a splitter - timeline splits into left and right
                total_paths = 0

                # Left path
                if col - 1 >= 0:
                    left_paths = count_paths_from(current_row, col - 1)
                    total_paths += left_paths

                # Right path
                if col + 1 < len(grid[current_row]):
                    right_paths = count_paths_from(current_row, col + 1)
                    total_paths += right_paths

                memo[(row, col)] = total_paths
                return total_paths

            elif char not in [".", "S"]:
                # Unknown character - exit (1 timeline)
                memo[(row, col)] = 1
                return 1
            # Continue moving down if char is '.' or 'S'

    # Count paths from starting position
    return count_paths_from(start_row, start_col)


def test_example():
    """Test with the example from the problem."""
    example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

    # Write example to temp file
    test_file = "test_input2.txt"
    with open(test_file, "w") as f:
        f.write(example)

    print("Testing example (Part 2):")
    print("-" * 60)

    # Debug version
    with open(test_file) as f:
        grid = [line.rstrip("\n") for line in f]

    print(f"Grid has {len(grid)} rows")

    result = solve_part2(test_file)
    print(f"Timelines: {result}")
    print("Expected: 40")

    import os

    os.remove(test_file)


def main():
    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
