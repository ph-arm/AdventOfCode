"""Advent of Code 2025 - Day 04 - Part Two"""


def count_adjacent_rolls(grid, row, col):
    """
    Count the number of rolls (@) in the 8 adjacent positions.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # Check all 8 directions
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == "@":
                count += 1

    return count


def solve_part2(input_file):
    """
    Simulate removing accessible rolls iteratively until no more can be removed.
    A roll can be removed if it has fewer than 4 adjacent rolls.
    """
    with open(input_file) as f:
        lines = [line.strip() for line in f if line.strip()]

    # Convert to mutable grid
    grid = [list(line) for line in lines]

    total_removed = 0

    while True:
        # Find all accessible rolls in this iteration
        accessible = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    adjacent_rolls = count_adjacent_rolls(grid, row, col)
                    if adjacent_rolls < 4:
                        accessible.append((row, col))

        # If no rolls can be removed, we're done
        if not accessible:
            break

        # Remove all accessible rolls
        for row, col in accessible:
            grid[row][col] = "."

        total_removed += len(accessible)

    return total_removed


def test_example():
    """Test with the example from the problem."""
    example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    lines = example.strip().split("\n")
    grid = [list(line) for line in lines]

    print("Testing example grid (Part 2):")
    print("-" * 60)

    total_removed = 0
    iteration = 0

    while True:
        # Find all accessible rolls
        accessible = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    adjacent_rolls = count_adjacent_rolls(grid, row, col)
                    if adjacent_rolls < 4:
                        accessible.append((row, col))

        if not accessible:
            break

        iteration += 1
        print(f"Iteration {iteration}: Removing {len(accessible)} rolls")

        # Remove all accessible rolls
        for row, col in accessible:
            grid[row][col] = "."

        total_removed += len(accessible)

    print("-" * 60)
    print(f"Total removed: {total_removed}")
    print("Expected: 43")


def main():
    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
