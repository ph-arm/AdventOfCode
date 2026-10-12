"""Advent of Code 2025 - Day 09 - Part Two"""


def solve_part2(input_file):
    """
    Find the largest rectangle using two red tiles as opposite corners,
    where all tiles in the rectangle must be red or green (inside/on the polygon loop).

    The red tiles form a polygon loop in the order they appear in the input.
    Green tiles are on the edges and inside the polygon.
    """
    with open(input_file) as f:
        lines = [line.strip() for line in f if line.strip()]

    # Parse coordinates (these form a polygon in order)
    tiles = []
    for line in lines:
        x, y = map(int, line.split(","))
        tiles.append((x, y))

    # Use line segment intersection for fast validation
    polygon_set = set(tiles)
    pip_cache = {}  # Cache point-in-polygon results

    # Pre-compute polygon edges once
    n = len(tiles)
    polygon_edges = [(tiles[i], tiles[(i + 1) % n]) for i in range(n)]

    def point_in_polygon_winding(x, y):
        """Winding number algorithm for point-in-polygon test."""
        key = (x, y)
        if key in pip_cache:
            return pip_cache[key]

        if key in polygon_set:
            pip_cache[key] = True
            return True

        n = len(tiles)
        winding_num = 0

        for i in range(n):
            p1 = tiles[i]
            p2 = tiles[(i + 1) % n]

            if p1[1] <= y:
                if p2[1] > y:
                    # Upward crossing - check if point is left of edge
                    if (p2[0] - p1[0]) * (y - p1[1]) - (x - p1[0]) * (
                        p2[1] - p1[1]
                    ) > 0:
                        winding_num += 1
            else:
                if p2[1] <= y:
                    # Downward crossing - check if point is right of edge
                    if (p2[0] - p1[0]) * (y - p1[1]) - (x - p1[0]) * (
                        p2[1] - p1[1]
                    ) < 0:
                        winding_num -= 1

        result = winding_num != 0
        pip_cache[key] = result
        return result

    def segments_intersect_interior(seg1_start, seg1_end, seg2_start, seg2_end):
        """Check if two line segments intersect in their interiors using integer math."""
        x1, y1 = seg1_start
        x2, y2 = seg1_end
        x3, y3 = seg2_start
        x4, y4 = seg2_end

        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return False  # Parallel or collinear

        # Use integer arithmetic to avoid floating point
        t_num = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        u_num = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))

        # Interior intersection only: 0 < t < 1 and 0 < u < 1
        # For 0 < t_num/denom < 1: check if t_num and denom have same sign and |t_num| < |denom|
        if denom > 0:
            t_valid = 0 < t_num < denom
            u_valid = 0 < u_num < denom
        else:
            t_valid = denom < t_num < 0
            u_valid = denom < u_num < 0

        return t_valid and u_valid

    def is_rectangle_valid(x1, y1, x2, y2):
        """Check if rectangle is valid using edge intersection tests."""
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        # Check if all 4 corners are inside or on the polygon
        # Corners are already red tiles (in polygon_set), so just verify they're vertices
        corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]

        # Only need to check corners that aren't already polygon vertices
        for cx, cy in corners:
            if (cx, cy) not in polygon_set:
                if not point_in_polygon_winding(cx, cy):
                    return False

        # Check if center point is inside (helps catch concave cases)
        mid_x = (min_x + max_x) // 2
        mid_y = (min_y + max_y) // 2
        if (mid_x, mid_y) not in polygon_set and not point_in_polygon_winding(
            mid_x, mid_y
        ):
            return False

        # Check if any polygon edge crosses through the rectangle interior
        rect_edges = [
            ((min_x, min_y), (max_x, min_y)),  # bottom
            ((max_x, min_y), (max_x, max_y)),  # right
            ((max_x, max_y), (min_x, max_y)),  # top
            ((min_x, max_y), (min_x, min_y)),  # left
        ]

        # Use pre-computed polygon edges with bounding box check
        for poly_edge in polygon_edges:
            # Quick bounding box rejection - skip edges that can't intersect rectangle
            (px1, py1), (px2, py2) = poly_edge
            edge_min_x, edge_max_x = min(px1, px2), max(px1, px2)
            edge_min_y, edge_max_y = min(py1, py2), max(py1, py2)

            # Skip if bounding boxes don't overlap
            if (
                edge_max_x < min_x
                or edge_min_x > max_x
                or edge_max_y < min_y
                or edge_min_y > max_y
            ):
                continue

            # Check if polygon edge crosses through rectangle interior
            for rect_edge in rect_edges:
                if segments_intersect_interior(
                    rect_edge[0], rect_edge[1], poly_edge[0], poly_edge[1]
                ):
                    return False

        return True

    max_area = 0

    # Sort tile pairs by potential area (largest first) for better pruning
    tile_pairs = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            tile_pairs.append((area, i, j))

    tile_pairs.sort(reverse=True)

    for area, i, j in tile_pairs:
        # Early termination - if remaining pairs can't beat max_area, stop
        if area <= max_area:
            break

        x1, y1 = tiles[i]
        x2, y2 = tiles[j]

        # Both corners are red tiles, check if rectangle is valid
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        if is_rectangle_valid(min_x, min_y, max_x, max_y):
            max_area = area

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
    test_file = "test_input2.txt"
    with open(test_file, "w") as f:
        f.write(example)

    print("Testing example (Part 2):")
    print("-" * 60)

    result = solve_part2(test_file)
    print(f"Largest valid rectangle area: {result}")
    print("Expected: 24")

    import os

    os.remove(test_file)


def main():
    return solve_part2("input.txt")


if __name__ == "__main__":
    print(main())
