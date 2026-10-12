"""Advent of Code 2025 - Day 10 - Part Two"""

import re


def main():
    def solve_part2(input_file):
        """
        Solve the factory machine joltage configuration problem.

        Each button increments certain counters, and we need to reach target values.
        This is a system of linear equations: A * x = b, where x >= 0.
        """
        with open(input_file) as f:
            lines = [line.strip() for line in f if line.strip()]

        total_presses = 0

        for line in lines:
            # Extract joltage requirements {3,5,4,7}
            joltage_match = re.search(r"\{([0-9,]+)\}", line)
            if not joltage_match:
                continue

            joltage_str = joltage_match.group(1)
            targets = list(map(int, joltage_str.split(",")))
            num_counters = len(targets)

            # Extract button configurations (0,1,2) (3,4) etc.
            buttons = []
            for match in re.finditer(r"\(([0-9,]+)\)", line):
                button_str = match.group(1)
                button_counters = list(map(int, button_str.split(",")))
                buttons.append(button_counters)

            # Solve using Gaussian elimination
            min_presses = solve_joltage(num_counters, buttons, targets)
            total_presses += min_presses

        return total_presses

    def solve_joltage(num_counters, buttons, targets):
        """
        Solve the joltage configuration using Gaussian elimination.

        We have: A * x = b
        where:
        - A[i][j] = 1 if button j increments counter i, else 0
        - x[j] = number of times to press button j (what we solve for)
        - b[i] = target value for counter i

        Handle underdetermined systems by trying different free variable values.
        """
        num_buttons = len(buttons)

        # Build augmented matrix [A | b]
        matrix = []
        for counter_idx in range(num_counters):
            row = [0.0] * num_buttons
            for button_idx, button in enumerate(buttons):
                if counter_idx in button:
                    row[button_idx] = 1.0
            row.append(float(targets[counter_idx]))
            matrix.append(row)

        # Keep track of original matrix
        [row[:] for row in matrix]

        # Gaussian elimination to reduced row echelon form
        pivot_rows = []
        pivot_cols = []

        current_row = 0
        for col in range(num_buttons):
            # Find pivot
            pivot_row = None
            max_val = 0
            for row in range(current_row, num_counters):
                if abs(matrix[row][col]) > max_val:
                    max_val = abs(matrix[row][col])
                    pivot_row = row

            if max_val < 1e-10:
                continue  # No pivot, this is a free variable

            # Swap rows
            matrix[current_row], matrix[pivot_row] = (
                matrix[pivot_row],
                matrix[current_row],
            )

            pivot_rows.append(current_row)
            pivot_cols.append(col)

            # Scale pivot row
            pivot_val = matrix[current_row][col]
            for c in range(num_buttons + 1):
                matrix[current_row][c] /= pivot_val

            # Eliminate all other rows in this column
            for row in range(num_counters):
                if row != current_row and abs(matrix[row][col]) > 1e-10:
                    factor = matrix[row][col]
                    for c in range(num_buttons + 1):
                        matrix[row][c] -= factor * matrix[current_row][c]

            current_row += 1

        # Identify free variables
        free_vars = []
        for col in range(num_buttons):
            if col not in pivot_cols:
                free_vars.append(col)

        # If no free variables, extract solution directly
        if not free_vars:
            solution = [0.0] * num_buttons
            for pivot_row, pivot_col in zip(pivot_rows, pivot_cols, strict=False):
                solution[pivot_col] = matrix[pivot_row][num_buttons]
            solution = [max(0, round(s)) for s in solution]
            return sum(solution)

        # Try different values for free variables to minimize total presses
        max_target = max(targets)

        best_total = float("inf")

        # Precompute which counters each button affects for faster verification
        button_to_counters = buttons  # Already in this format

        # For each free variable, search up to the max target value
        # Use adaptive search range
        if len(free_vars) == 0:
            # No free variables - unique solution
            solution = [0.0] * num_buttons
            for pivot_row, pivot_col in zip(pivot_rows, pivot_cols, strict=False):
                solution[pivot_col] = matrix[pivot_row][num_buttons]
            solution = [max(0, round(s)) for s in solution]
            return sum(solution)

        # Calculate upper bound for free variables based on maximum target
        # Use original working ranges
        if len(free_vars) <= 2:
            search_range = max_target + 1
        elif len(free_vars) == 3:
            search_range = min(30, max_target + 1)
        elif len(free_vars) == 4:
            search_range = min(25, max_target + 1)
        else:
            search_range = min(15, max_target + 1)

        # Try smaller values first for better pruning
        from itertools import product

        for free_vals in product(range(search_range), repeat=len(free_vars)):
            solution = [0.0] * num_buttons

            # Set free variables
            for i, var_col in enumerate(free_vars):
                solution[var_col] = free_vals[i]

            # Determine pivot variables from RREF
            valid = True
            for pivot_row, pivot_col in zip(pivot_rows, pivot_cols, strict=False):
                val = matrix[pivot_row][num_buttons]
                for col in range(num_buttons):
                    if col != pivot_col:
                        val -= matrix[pivot_row][col] * solution[col]
                solution[pivot_col] = val

                # Early check: if any pivot variable is negative, skip
                if val < -0.5:
                    valid = False
                    break

            if not valid:
                continue

            # Round solution
            solution = [max(0, round(s)) for s in solution]

            # Verify solution (fast)
            achieved = [0] * num_counters
            for button_idx in range(num_buttons):
                if solution[button_idx] > 0:
                    for counter_idx in button_to_counters[button_idx]:
                        achieved[counter_idx] += solution[button_idx]

            if achieved == targets:
                total = sum(solution)
                if total < best_total:
                    best_total = total

        if best_total != float("inf"):
            return best_total

        # Fallback: use basic solution
        solution = [0.0] * num_buttons
        for pivot_row, pivot_col in zip(pivot_rows, pivot_cols, strict=False):
            solution[pivot_col] = matrix[pivot_row][num_buttons]
        solution = [max(0, round(s)) for s in solution]
        return sum(solution)

    def test_examples():
        """Test with the examples from the problem."""
        examples = [
            "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
            "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
            "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
        ]

        test_file = "test_input2.txt"
        with open(test_file, "w") as f:
            f.write("\n".join(examples))

        result = solve_part2(test_file)
        print(f"Test result: {result}")
        print("Expected: 33")

        # Test individual machines
        for i, example in enumerate(examples, 1):
            with open(test_file, "w") as f:
                f.write(example)
            result = solve_part2(test_file)
            expected = [10, 12, 11][i - 1]
            print(f"Machine {i}: {result} presses (expected {expected})")

    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
