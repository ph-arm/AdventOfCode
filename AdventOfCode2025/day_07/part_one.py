"""Advent of Code 2025 - Day 07 - Part One"""


def solve_part1(input_file):
    """
    Simulate tachyon beams through a manifold.

    - Beams start at 'S' and move downward
    - When a beam hits a splitter '^', it stops and creates two new beams
      that continue DOWNWARD from the positions immediately left and right of the splitter
    - Count how many times beams are split (how many splitters are hit)
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

    # Track beams: list of (row, col)
    # All beams move downward
    beams = [(start_row, start_col)]
    split_count = 0
    visited_splitters = set()  # Track (row, col) of splitters we've hit

    while beams:
        new_beams = []

        for row, col in beams:
            # Move beam downward until it hits a splitter or exits
            while True:
                row += 1  # Move down

                # Check bounds
                if row >= len(grid):
                    break  # Beam exits bottom
                if col < 0 or col >= len(grid[row]):
                    break  # Out of bounds horizontally

                # Check what's at this position
                char = grid[row][col]

                if char == "^":
                    # Hit a splitter!
                    if (row, col) not in visited_splitters:
                        visited_splitters.add((row, col))
                        split_count += 1
                        # Create two new beams that continue DOWNWARD
                        # from left and right of the splitter
                        if col - 1 >= 0:
                            new_beams.append((row, col - 1))
                        if col + 1 < len(grid[row]):
                            new_beams.append((row, col + 1))
                    break  # This beam stops
                elif char not in [".", "S"]:
                    # Unknown character
                    break
                # If char is '.' or 'S', continue moving down

        beams = new_beams

    return split_count


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
    test_file = "test_input.txt"
    with open(test_file, "w") as f:
        f.write(example)

    print("Testing example:")
    print("-" * 60)

    result = solve_part1(test_file)
    print(f"Splits: {result}")
    print("Expected: 21")

    import os

    os.remove(test_file)


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
