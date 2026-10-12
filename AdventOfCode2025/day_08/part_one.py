"""Advent of Code 2025 - Day 08 - Part One"""

import heapq
import math


def main():
    def solve_part1(input_file, num_connections=1000):
        """
        Connect junction boxes by their closest pairs and find the three largest circuits.

        - Parse 3D coordinates
        - Calculate all pairwise distances
        - Connect the closest pairs using Union-Find
        - Return product of three largest circuit sizes
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

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
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
            return True

        # Connect the closest pairs (num_connections pairs, even if already connected)
        for _ in range(min(num_connections, len(distances))):
            if not distances:
                break
            dist, i, j = heapq.heappop(distances)
            union(i, j)  # Try to connect, even if already connected

        # Find circuit sizes
        circuit_sizes = {}
        for i in range(n):
            root = find(i)
            circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

        # Get the three largest circuits
        sizes = sorted(circuit_sizes.values(), reverse=True)

        if len(sizes) >= 3:
            result = sizes[0] * sizes[1] * sizes[2]
        elif len(sizes) == 2:
            result = sizes[0] * sizes[1]
        elif len(sizes) == 1:
            result = sizes[0]
        else:
            result = 0

        return result

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
        test_file = "test_input.txt"
        with open(test_file, "w") as f:
            f.write(example)

        print("Testing example:")
        print("-" * 60)

        # Make 10 connections as stated in the problem
        result = solve_part1(test_file, num_connections=10)

        # Debug: check the circuit sizes
        with open(test_file) as f:
            lines = [line.strip() for line in f if line.strip()]
        boxes = []
        for line in lines:
            x, y, z = map(int, line.split(","))
            boxes.append((x, y, z))
        n = len(boxes)
        distances = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, z1 = boxes[i]
                x2, y2, z2 = boxes[j]
                dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
                dist = math.sqrt(dist_sq)
                heapq.heappush(distances, (dist, i, j))
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True

        connections_made = 0
        while connections_made < 10 and distances:
            dist, i, j = heapq.heappop(distances)
            if union(i, j):
                connections_made += 1
        circuit_sizes = {}
        for i in range(n):
            root = find(i)
            circuit_sizes[root] = circuit_sizes.get(root, 0) + 1
        sizes = sorted(circuit_sizes.values(), reverse=True)
        print(f"Circuit sizes: {sizes}")

        print(f"Product of three largest circuits: {result}")
        print("Expected: 40")

        import os

        os.remove(test_file)

        return result == 40

    return solve_part1("input.txt", num_connections=1000)


if __name__ == "__main__":
    print(main())
