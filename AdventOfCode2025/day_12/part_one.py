"""Advent of Code 2025 - Day 12 - Part One"""


def parse_input(input_file):
    """Parse the shape definitions and the region requests."""
    with open(input_file) as f:
        lines = f.read().split("\n")

    shapes = {}
    regions = []
    cur_idx = None
    cur_rows = []

    def flush():
        if cur_idx is not None:
            shapes[cur_idx] = cur_rows

    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        if _looks_like_region(s):
            flush()
            cur_idx, cur_rows = None, []
            dim, counts = s.split(":")
            w, length = (int(x) for x in dim.strip().split("x"))
            regions.append((w, length, [int(x) for x in counts.split()]))
        elif s.endswith(":") and s[:-1].isdigit():
            flush()
            cur_idx, cur_rows = int(s[:-1]), []
        elif cur_idx is not None:
            cur_rows.append(s)
    flush()
    return shapes, regions


def _looks_like_region(s):
    head = s.split(":", 1)[0].strip().split("x")
    return len(head) == 2 and all(p.isdigit() for p in head)


def _normalize(points):
    min_r = min(r for r, _ in points)
    min_c = min(c for _, c in points)
    return tuple(sorted((r - min_r, c - min_c) for r, c in points))


def shape_orientations(rows):
    """All unique rotations/reflections of a shape as normalized cell lists."""
    points = [
        (r, c) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == "#"
    ]
    results = []
    for _ in range(4):
        points = [(c, -r) for r, c in points]  # rotate 90 degrees
        for variant in (points, [(r, -c) for r, c in points]):  # and its mirror
            norm = _normalize(variant)
            if norm not in results:
                results.append(norm)
    return results


def can_fit(w, length, counts, shape_cells, shape_orients):
    """Decide whether all requested presents fit into a w x length region."""
    needed = sum(counts[i] * shape_cells[i] for i in range(len(counts)))
    if needed > w * length:
        return False  # not enough cells (necessary condition)
    if sum(counts) <= (w // 3) * (length // 3):
        return True  # each present gets its own disjoint 3x3 block (sufficient)
    return _pack(w, length, counts, shape_cells, shape_orients)


def _pack(w, length, counts, shape_cells, shape_orients):
    """Backtracking packer for the ambiguous zone (not reached by the real input)."""
    occupied = bytearray(w * length)
    remaining = list(counts)
    order = sorted(range(len(counts)), key=lambda i: -shape_cells[i])

    def dfs(start, slack):
        idx = start
        while idx < w * length and occupied[idx]:
            idx += 1
        if sum(remaining) == 0:
            return True
        if idx == w * length:
            return False
        r, c = divmod(idx, w)
        for s in order:
            if remaining[s] == 0:
                continue
            for orient in shape_orients[s]:
                for anchor_r, anchor_c in orient:
                    base_r, base_c = r - anchor_r, c - anchor_c
                    placed = []
                    for dr, dc in orient:
                        rr, cc = base_r + dr, base_c + dc
                        if (
                            not (0 <= rr < length and 0 <= cc < w)
                            or occupied[rr * w + cc]
                        ):
                            placed = None
                            break
                        placed.append(rr * w + cc)
                    if placed is None:
                        continue
                    for j in placed:
                        occupied[j] = 1
                    remaining[s] -= 1
                    if dfs(idx + 1, slack):
                        return True
                    remaining[s] += 1
                    for j in placed:
                        occupied[j] = 0
        if slack > 0:  # leave this cell empty
            occupied[idx] = 1
            if dfs(idx + 1, slack - 1):
                return True
            occupied[idx] = 0
        return False

    slack = w * length - sum(counts[i] * shape_cells[i] for i in range(len(counts)))
    return dfs(0, slack)


def solve_part1(input_file):
    """Count how many regions can fit all of their requested presents."""
    shapes, regions = parse_input(input_file)
    num_shapes = max(shapes) + 1
    shape_cells = [sum(row.count("#") for row in shapes[i]) for i in range(num_shapes)]
    shape_orients = [shape_orientations(shapes[i]) for i in range(num_shapes)]

    fit = 0
    for w, length, counts in regions:
        counts = counts + [0] * (num_shapes - len(counts))
        if can_fit(w, length, counts, shape_cells, shape_orients):
            fit += 1
    return fit


def test_example():
    """Test with the example from the problem."""
    example = (
        "0:\n###\n##.\n##.\n\n"
        "1:\n###\n##.\n.##\n\n"
        "2:\n.##\n###\n##.\n\n"
        "3:\n##.\n###\n##.\n\n"
        "4:\n###\n#..\n###\n\n"
        "5:\n###\n.#.\n###\n\n"
        "4x4: 0 0 0 0 2 0\n"
        "12x5: 1 0 1 0 2 2\n"
        "12x5: 1 0 1 0 3 2\n"
    )

    test_file = "test_input.txt"
    with open(test_file, "w") as f:
        f.write(example)

    result = solve_part1(test_file)
    print(f"Test result: {result}")
    print("Expected: 2")


def main():
    return solve_part1("input.txt")


if __name__ == "__main__":
    print(main())
