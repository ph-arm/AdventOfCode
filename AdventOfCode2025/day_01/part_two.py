"""Advent of Code 2025 - Day 01 - Part Two"""


def solve_part2(input_file):
    """
    Solve Day 1 Part 2: Count how many times the dial points at 0 during AND after rotations.

    Now we need to count every click that passes through 0, not just the final position.
    """
    with open(input_file) as f:
        lines = [line.strip() for line in f if line.strip()]

    position = 50
    zero_count = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        c = distance // 100
        r = distance % 100

        if direction == "L":
            new_position = (position - r) % 100
            if r >= position:
                times_at_zero = c + 1 - (position == 0)
            else:
                times_at_zero = c
            zero_count += times_at_zero
            position = new_position

        else:
            new_position = (position + r) % 100
            times_at_zero = 0
            if position + r >= 100:
                times_at_zero = 1 + c - (position == 0)
            else:
                times_at_zero = c
            zero_count += times_at_zero
            position = new_position

    return zero_count


def test_example():
    """Test with the example from the problem - Part 2 version."""
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
        c = distance // 100
        r = distance % 100

        if direction == "L":
            new_position = (position - r) % 100
            if r > position:
                times_at_zero = c + 1 - (position == 0)
            else:
                times_at_zero = c - (position == 0)
            zero_count += times_at_zero
            position = new_position

        else:
            new_position = (position + r) % 100
            times_at_zero = 0
            if position + r >= 100:
                times_at_zero = 1 + c - (position == 0)
            else:
                times_at_zero = c - (position == 0)
            zero_count += times_at_zero
            position = new_position

        if times_at_zero > 0:
            print(
                f"After {line}: position = {position} (hit 0 {times_at_zero} time(s))"
            )
        else:
            print(f"After {line}: position = {position}")

    print(f"\nTotal times at 0: {zero_count}")
    print("Expected: 6")


def main():
    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
