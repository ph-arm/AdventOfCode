"""Advent of Code 2025 - Day 04 - Part One"""


def count_adjacent_rolls(grid, row, col):
    """
    Count the number of rolls (@) in the 8 adjacent positions.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Check all 8 directions
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == "@":
                count += 1

    return count


def solve_part1(input_file):
    """
    Count how many rolls of paper can be accessed by a forklift.
    A roll can be accessed if it has fewer than 4 adjacent rolls.
    """
    with open(input_file) as f:
        grid = [line.strip() for line in f if line.strip()]

    accessible_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "@":
                adjacent_rolls = count_adjacent_rolls(grid, row, col)
                if adjacent_rolls < 4:
                    accessible_count += 1

    return accessible_count


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

    grid = example.strip().split("\n")
    accessible_count = 0

    print("Testing example grid:")
    print("-" * 60)

    # Create a visualization
    result_grid = []
    for row in range(len(grid)):
        result_row = []
        for col in range(len(grid[row])):
            if grid[row][col] == "@":
                adjacent_rolls = count_adjacent_rolls(grid, row, col)
                if adjacent_rolls < 4:
                    accessible_count += 1
                    result_row.append("x")
                else:
                    result_row.append("@")
            else:
                result_row.append(".")
        result_grid.append("".join(result_row))

    print("Accessible rolls marked with x:")
    for line in result_grid:
        print(line)

    print("-" * 60)
    print(f"Total accessible: {accessible_count}")
    print("Expected: 13")


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
