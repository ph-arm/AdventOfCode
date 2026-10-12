"""Advent of Code 2025 - Day 01 - Part One"""


def solve_part1(input_file):
    """
    Solve Day 1 Part 1: Count how many times the dial points at 0 after rotations.

    The dial:
    - Has numbers 0-99 in a circle
    - Starts at 50
    - L means rotate left (toward lower numbers)
    - R means rotate right (toward higher numbers)
    """
    with open(input_file) as f:
        lines = [line.strip() for line in f if line.strip()]

    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            # Left means subtract (toward lower numbers)
            position = (position - distance) % 100
        else:  # direction == 'R'
            # Right means add (toward higher numbers)
            position = (position + distance) % 100

        # Count if we landed on 0
        if position == 0:
            zero_count += 1

    return zero_count


def test_example():
    """Test with the example from the problem."""
    example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    lines = example.strip().split("\n")
    position = 50
    zero_count = 0

    print(f"Starting position: {position}")

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100

        print(f"After {line}: position = {position}")

        if position == 0:
            zero_count += 1

    print(f"\nTotal times at 0: {zero_count}")
    print("Expected: 3")


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
