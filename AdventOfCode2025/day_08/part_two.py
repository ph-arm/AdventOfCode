"""Advent of Code 2025 - Day 08 - Part Two"""

import heapq
import math


def main():
    def solve_part2(input_file):
        """
        Connect junction boxes until they're all in one circuit.
        Return the product of X coordinates of the last connection.
        """
        with open(input_file) as f:
            lines = [line.strip() for line in f if line.strip()]

        # Parse coordinates
        boxes = []
        for line in lines:
            x, y, z = map(int, line.split(","))
            boxes.append((x, y, z))

        n = len(boxes)

        # Calculate all pairwise distances and store in a min heap
        distances = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, z1 = boxes[i]
                x2, y2, z2 = boxes[j]
                dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
                dist = math.sqrt(dist_sq)
                heapq.heappush(distances, (dist, i, j))

        # Union-Find data structure
        parent = list(range(n))
        rank = [0] * n
        num_circuits = n  # Start with n separate circuits

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            nonlocal num_circuits
            px, py = find(x), find(y)
            if px == py:
                return False  # Already connected
            # Union by rank
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            num_circuits -= 1  # Merged two circuits into one
            return True

        # Connect pairs until all are in one circuit
        last_i, last_j = None, None

        while num_circuits > 1 and distances:
            dist, i, j = heapq.heappop(distances)
            if union(i, j):
                last_i, last_j = i, j
                if num_circuits == 1:
                    break

        # Get X coordinates of the last connection
        if last_i is not None and last_j is not None:
            x1 = boxes[last_i][0]
            x2 = boxes[last_j][0]
            return x1 * x2

        return 0

    def test_example():
        """Test with the example from the problem."""
        example = """162,817,812
    57,618,57
    906,360,560
    592,479,940
    352,342,300
    466,668,158
    542,29,236
    431,825,988
    739,650,466
    52,470,668
    216,146,977
    819,987,18
    117,168,530
    805,96,715
    346,949,466
    970,615,88
    941,993,340
    862,61,35
    984,92,344
    425,690,689"""

        # Write example to temp file
        test_file = "test_input2.txt"
        with open(test_file, "w") as f:
            f.write(example)

        print("Testing example (Part 2):")
        print("-" * 60)

        result = solve_part2(test_file)
        print(f"Product of X coordinates: {result}")
        print("Expected: 25272 (216 * 117)")

        import os

        os.remove(test_file)

        return result == 25272

    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
