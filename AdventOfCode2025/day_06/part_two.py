"""Advent of Code 2025 - Day 06 - Part Two"""


def solve_problem(file, debug=False):
    f = open(file)
    lines = [line.replace("\n", "") for line in f]
    if lines[-1] == "":
        lines = lines[:-1]
    columns = []
    for i in range(len(lines[-1])):
        found = True
        for line in lines[:-1]:
            if line[i] != " ":
                found = False
                break
        if found:
            columns.append(i)
    totals = 0
    probs = []
    p = 0
    for i in columns:
        cc = []
        for line in lines:
            cc.append(line[p : i + 1])
        p = i
        probs.append(cc)
    cc = []
    for line in lines:
        cc.append(line[p:])
    probs.append(cc)
    for prob in probs:
        cc = prob
        nums = []
        for c in range(len(cc[0])):
            cn = ""
            for row in cc[:-1]:
                if row[c] != " ":
                    cn = cn + row[c]
            if cn != "":
                nums.append(int(cn))
        op = cc[-1].strip()
        if debug:
            print(f"Numbers: {nums}, Operator: {op}")
        if op == "+":
            totals = totals + sum(nums)
        elif op == "*":
            prod = 1
            for n in nums:
                prod = prod * n
            totals = totals + prod
    return totals


def solve_part2(input_file):
    """
    Main entry point for part 2 solution.
    This function is called by run.py.
    """
    return solve_problem(input_file)


def test_example():
    """Test with the example from the problem."""
    example = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   + """

    # Write example to temp file
    test_file = "test_input2.txt"
    with open(test_file, "w") as f:
        f.write(example)

    print("Testing example (Part 2 - Right-to-Left):")
    print("-" * 60)

    # Use the main solution function
    total = solve_problem(test_file, debug=True)

    print(f"Grand total: {total}")
    print("Expected: 3263827")

    import os

    os.remove(test_file)


def main():
    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
