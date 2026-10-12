"""Advent of Code 2025 - Day 06 - Part One"""


def parse_worksheet(input_file):
    """
    Parse the worksheet to extract vertical problems.
    Numbers are stacked vertically, operators at bottom.

    Example:
    123 328 51 64
    45 64 387 23
    6 98 215 314
    *   +  *  +

    Problem 1: 123, 45, 6, * (column 1)
    Problem 2: 328, 64, 98, + (column 2)
    Problem 3: 51, 387, 215, * (column 3)
    Problem 4: 64, 23, 314, + (column 4)

    Each line contains space-separated numbers/operators.
    Each position across the lines forms one problem.
    """
    with open(input_file) as f:
        lines = [line.rstrip("\n") for line in f]

    # Remove empty lines and separator lines
    lines = [
        line
        for line in lines
        if line.strip() and not all(c in ["-", " "] for c in line.strip())
    ]

    if not lines:
        return []

    # Split each line into tokens (numbers/operators)
    rows = []
    for line in lines:
        tokens = line.split()
        rows.append(tokens)

    # Last row has operators
    operator_row = rows[-1]
    number_rows = rows[:-1]

    # Transpose: each column becomes a problem
    num_problems = len(operator_row)
    problems = []

    for col_idx in range(num_problems):
        # Collect numbers from this column across all number rows
        numbers = []
        for row in number_rows:
            if col_idx < len(row):
                token = row[col_idx]
                if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                    numbers.append(int(token))

        # Get operator for this column
        if col_idx < len(operator_row):
            operator = operator_row[col_idx]
            if operator in ["+", "*"] and numbers:
                problems.append((numbers, operator))

    return problems


def solve_problem(numbers, operator):
    """
    Solve a single problem by applying the operator to all numbers.
    """
    if operator == "+":
        return sum(numbers)
    elif operator == "*":
        result = 1
        for num in numbers:
            result *= num
        return result
    return 0


def solve_part1(input_file):
    """
    Solve all problems and return the grand total.
    """
    problems = parse_worksheet(input_file)

    total = 0
    for numbers, operator in problems:
        answer = solve_problem(numbers, operator)
        total += answer

    return total


def test_example():
    """Test with the example from the problem."""
    example = """123 328 51 64
45 64 387 23
6 98 215 314
*   +   *   +"""

    # Write example to temp file
    with open("test_input.txt", "w") as f:
        f.write(example)

    print("Testing example:")
    print("-" * 60)

    problems = parse_worksheet("test_input.txt")

    print(f"Found {len(problems)} problems:")

    total = 0
    expected_answers = [33210, 490, 4243455, 401]
    for i, (numbers, operator) in enumerate(problems):
        answer = solve_problem(numbers, operator)
        expected = expected_answers[i] if i < len(expected_answers) else "?"
        status = "✓" if answer == expected else "✗"
        print(
            f"{status} Problem {i + 1}: {f' {operator} '.join(map(str, numbers))} = {answer} (expected {expected})"
        )
        total += answer

    print("-" * 60)
    print(f"Grand total: {total}")
    print("Expected: 4277556")

    import os

    os.remove("test_input.txt")


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
