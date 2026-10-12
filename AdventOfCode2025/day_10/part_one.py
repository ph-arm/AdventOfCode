"""Advent of Code 2025 - Day 10 - Part One"""

import re


def main():
    def solve_part1(input_file):
        """
        Solve the factory machine initialization problem.

        This is a system of linear equations over GF(2) (binary field).
        Each button toggles certain lights, and we need to find which buttons
        to press (each 0 or 1 times) to achieve the target configuration.

        We use Gaussian elimination to solve the system.
        """
        with open(input_file) as f:
            lines = [line.strip() for line in f if line.strip()]

        total_presses = 0

        for line in lines:
            # Parse the line
            # Extract indicator lights pattern [.##.]
            lights_match = re.search(r"\[([.#]+)\]", line)
            if not lights_match:
                continue

            lights_pattern = lights_match.group(1)
            num_lights = len(lights_pattern)

            # Target state: 1 for #, 0 for .
            target = [1 if c == "#" else 0 for c in lights_pattern]

            # Extract button configurations (0,1,2) (3,4) etc.
            buttons = []
            for match in re.finditer(r"\(([0-9,]+)\)", line):
                button_str = match.group(1)
                button_lights = list(map(int, button_str.split(",")))
                buttons.append(button_lights)

            # Solve using Gaussian elimination over GF(2)
            min_presses = solve_lights_gf2(num_lights, buttons, target)
            total_presses += min_presses

        return total_presses

    def solve_lights_gf2(num_lights, buttons, target):
        """
        Solve the system of linear equations over GF(2).

        We have num_lights equations (one per light) and len(buttons) variables (button presses).
        Each button[i] defines which lights it toggles.

        Returns the minimum number of button presses needed.
        """
        num_buttons = len(buttons)

        # Create augmented matrix [A | b] where A is the coefficient matrix
        # and b is the target vector
        # A[i][j] = 1 if button j toggles light i, 0 otherwise
        matrix = []
        for light_idx in range(num_lights):
            row = [0] * num_buttons
            for button_idx, button in enumerate(buttons):
                if light_idx in button:
                    row[button_idx] = 1
            row.append(target[light_idx])  # Augmented part
            matrix.append(row)

        # Gaussian elimination in GF(2) - reduced row echelon form
        pivot_rows = []
        pivot_cols = []

        current_row = 0
        for col in range(num_buttons):
            # Find pivot in this column
            pivot_row = None
            for row in range(current_row, num_lights):
                if matrix[row][col] == 1:
                    pivot_row = row
                    break

            if pivot_row is None:
                continue  # No pivot in this column, it's a free variable

            # Swap rows
            if pivot_row != current_row:
                matrix[current_row], matrix[pivot_row] = (
                    matrix[pivot_row],
                    matrix[current_row],
                )

            pivot_rows.append(current_row)
            pivot_cols.append(col)

            # Eliminate all other 1s in this column (both above and below)
            for row in range(num_lights):
                if row != current_row and matrix[row][col] == 1:
                    # XOR this row with the pivot row
                    for c in range(num_buttons + 1):
                        matrix[row][c] ^= matrix[current_row][c]

            current_row += 1

        # Check for inconsistent system
        for row in range(current_row, num_lights):
            if matrix[row][num_buttons] == 1:
                # Inconsistent: 0 = 1
                return float("inf")

        # Identify free variables (columns without pivots)
        free_vars = []
        for col in range(num_buttons):
            if col not in pivot_cols:
                free_vars.append(col)

        # Try all combinations of free variables to minimize button presses
        min_presses = float("inf")

        for mask in range(1 << len(free_vars)):
            solution = [0] * num_buttons

            # Set free variables according to mask
            for i, var_col in enumerate(free_vars):
                solution[var_col] = (mask >> i) & 1

            # Determine pivot variables from free variables
            for _, (pivot_row, pivot_col) in enumerate(
                zip(pivot_rows, pivot_cols, strict=False)
            ):
                # The pivot variable is determined by the RHS and free variables in this row
                val = matrix[pivot_row][num_buttons]
                for col in range(num_buttons):
                    if col != pivot_col:
                        val ^= matrix[pivot_row][col] * solution[col]
                solution[pivot_col] = val

            # Count button presses
            presses = sum(solution)
            min_presses = min(min_presses, presses)

        return min_presses

    def test_examples():
        """Test with the examples from the problem."""
        examples = [
            "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
            "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
            "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
        ]

        test_file = "test_input.txt"
        with open(test_file, "w") as f:
            f.write("\n".join(examples))

        result = solve_part1(test_file)
        print(f"Test result: {result}")
        print("Expected: 7")

        # Test individual machines
        for i, example in enumerate(examples, 1):
            with open(test_file, "w") as f:
                f.write(example)
            result = solve_part1(test_file)
            print(f"Machine {i}: {result} presses")

    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
