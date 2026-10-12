"""Advent of Code 2025 - Day 09 - Part One"""


def solve_part1(input_file):
    """
    Find the largest rectangle area using two red tiles as opposite corners.

    The area of a rectangle with opposite corners at (x1, y1) and (x2, y2) is:
    (|x2 - x1| + 1) * (|y2 - y1| + 1)
    (We add 1 because the tiles at the corners are included)
    """
    with open(input_file) as f:
        lines = [line.strip() for line in f if line.strip()]

    # Parse coordinates
    tiles = []
    for line in lines:
        x, y = map(int, line.split(","))
        tiles.append((x, y))

    # Find maximum rectangle area
    max_area = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]

            # Calculate rectangle area (inclusive of corner tiles)
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            max_area = max(max_area, area)

    return max_area


def test_example():
    """Test with the example from the problem."""
    example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

    # Write example to temp file
    test_file = "test_input.txt"
    with open(test_file, "w") as f:
        f.write(example)

    print("Testing example:")
    print("-" * 60)

    result = solve_part1(test_file)
    print(f"Largest rectangle area: {result}")
    print("Expected: 50")

    import os

    os.remove(test_file)


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
