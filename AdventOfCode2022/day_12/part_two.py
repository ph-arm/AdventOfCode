"""Advent of Code 2022 - Day 12 - Part Two"""

### seriously not my best day...
import numpy as np

test_case = False


def mocked_content():
    pass


def main():
    result = []
    file = open("./input.txt")
    content = file.read().split("\n")
    if test_case:
        content = mocked_content()

    def format_line(content_line):
        def convert_int(a):
            if a == "S":
                return 1
            if a == "E":
                return 27
            return ord(a) - 96

        result = list(map(convert_int, list(content_line)))
        return result

    array_content = list(map(format_line, content))
    np_content = np.array(array_content)
    dtype = [("steps", int), ("potential", int), ("x", int), ("y", int)]
    start_knot = np.empty(1, dtype=dtype)
    for line in range(len(np_content)):
        for row in range(len(np_content[0])):
            if np_content[line][row] == 1:
                values = [(0, 10**6, line, row)]
                knot = np.array(
                    values,
                    dtype=dtype,
                )
                start_knot = np.concatenate((start_knot, knot), axis=0)
            if np_content[line][row] == 27:
                xend = line
                yend = row

    def distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    result = 30000
    for init_knot in start_knot[1:]:
        visited = np.zeros(np_content.shape)
        knot_open = 0
        knots = np.array([init_knot], dtype=dtype)
        while 1:
            if len(knots) == 0:
                step = 100000
                break
            current_knot = knots[0]
            step, potential, x, y = current_knot
            step += 1
            knot_open += 1
            elevation = np_content[x, y]
            if (
                x > 0
                and elevation + 1 - np_content[x - 1, y] >= 0
                and not visited[x - 1, y]
            ):
                visited[x - 1, y] = step
                d = distance((x - 1, y), (xend, yend))
                if d == 0:
                    break
                potential = d + step
                knot = np.array([(step, potential, x - 1, y)], dtype=dtype)
                knots = np.concatenate((knots, knot), axis=0)

            if (
                y > 0
                and elevation + 1 - np_content[x, y - 1] >= 0
                and not visited[x, y - 1]
            ):
                visited[x, y - 1] = step
                d = distance((x, y - 1), (xend, yend))
                if d == 0:
                    break
                potential = d + step
                knot = np.array([(step, potential, x, y - 1)], dtype=dtype)
                knots = np.concatenate((knots, knot), axis=0)

            if x + 1 < np_content.shape[0] and (
                elevation + 1 - np_content[x + 1, y] >= 0 and not visited[x + 1, y]
            ):
                visited[x + 1, y] = step
                d = distance((x + 1, y), (xend, yend))
                if d == 0:
                    break
                potential = d + step
                knot = np.array([(step, potential, x + 1, y)], dtype=dtype)
                knots = np.concatenate((knots, knot), axis=0)

            if (
                y + 1 < np_content.shape[1]
                and elevation + 1 - np_content[x, y + 1] >= 0
                and not visited[x, y + 1]
            ):
                visited[x, y + 1] = step
                d = distance((x, y + 1), (xend, yend))
                if d == 0:
                    break
                potential = d + step
                knot = np.array([(step, potential, x, y + 1)], dtype=dtype)
                knots = np.concatenate((knots, knot), axis=0)
            knots = np.delete(knots, 0)
            knots = np.sort(knots, order="steps")
        result = min(result, step)
        print(f" total step: {result}\ntotal node opened:{knot_open}")
    return int(result)


if __name__ == "__main__":
    print(main())
