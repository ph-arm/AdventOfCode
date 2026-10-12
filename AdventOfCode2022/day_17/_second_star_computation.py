"""Advent of Code 2022 - Day 17 - second star"""

import time

import numpy as np

test_case = False


def mocked_content():
    pass


def init_pieces():
    pieces = []
    description = [[2, 3], [3, 3], [4, 3], [5, 3]]  # |..####.|
    pieces.append(description)
    description = [
        [2, 4],
        [3, 4],
        [4, 4],
        [3, 5],
        [3, 3],
    ]  # |...#...||..###..||...#...|
    pieces.append(description)
    description = [
        [2, 3],
        [3, 3],
        [4, 3],
        [4, 4],
        [4, 5],
    ]  # |..###..||....#..||....#..|
    pieces.append(description)
    description = [
        [2, 3],
        [2, 4],
        [2, 5],
        [2, 6],
    ]  # |..#....||..#....||..#....||..#....|
    pieces.append(description)
    description = [
        [2, 3],
        [3, 3],
        [2, 4],
        [3, 4],
    ]  # |..##...||..##...|
    pieces.append(description)
    ans = []
    for items in pieces:
        piece = np.zeros((7, 8))
        for x, y in items:
            piece[x, y] = 1
        ans.append(piece)
    return ans


def solidify(current):
    for index, x in np.ndenumerate(current):
        if x:
            current[index] = 2


def solidify2(current, points):
    for index in points:
        current[index] = 2


def check_left(current):
    for index, x in np.ndenumerate(current):
        if x == 1:
            if index[0] == 0:
                return 0
            if current[index[0] - 1, index[1]] == 2:
                return 0
    return 1


def check_right2(current, points):
    for point in points:
        if point[0] == current.shape[0] - 1:
            return 0
        if current[point[0] + 1, point[1]] == 2:
            return 0
    return 1


def check_left2(current, points):
    for point in points:
        if point[0] == 0:
            return 0
        if current[point[0] - 1, point[1]] == 2:
            return 0
    return 1


def check_right(current):
    for index, x in np.ndenumerate(current):
        if x == 1:
            if index[0] == current.shape[0] - 1:
                return 0
            if current[index[0] + 1, index[1]] == 2:
                return 0
    return 1


def check_down(current, p=None):
    if not p:
        for index, x in np.ndenumerate(current):
            if x == 1:
                if index[1] == 0:
                    return 0
                if current[index[0], index[1] - 1] == 2:
                    return 0
    else:
        for point in p:
            if point[1] == 0:
                return 0
            if current[point[0], point[1] - 1] == 2:
                return 0
    return 1


def make_move(current, move, p=None):
    to_1 = []
    if not p:
        for index, x in np.ndenumerate(current):
            if x == 1:
                current[index] = 0
                to_1.append((index[0] + move[0], index[1] + move[1]))
        for index in to_1:
            current[index] = 1
        return to_1
    else:
        for index in p:
            current[index] = 0
            to_1.append((index[0] + move[0], index[1] + move[1]))
        for index in to_1:
            current[index] = 1
        return to_1


def get_moves(content):
    res = []
    translation = {"<": (-1, 0), ">": (1, 0)}
    for item in content:
        res.append(translation[item])
    return res


def visualization(current):
    d = np.swapaxes(current, 0, 1)
    result = ""
    for line in d:
        local = "|"
        for item in line:
            if item:
                local += "#"
            else:
                local += "."
        local += "|"
        result = local + "\n" + result
    print(result)
    return 0


def main():
    result = []
    file = open("./day_17/input.txt")
    if test_case:
        file.close()
        file = open("./day_17/test_input.txt")
    content = file.read().strip()
    moves = get_moves(content)
    print(f"{len(moves)} moves loaded")
    l_moves = len(moves)
    zone = np.array([[2], [2], [2], [2], [2], [2], [2]], dtype=np.int8)
    visualization(zone)
    goal = 1000000000000
    goal % (l_moves * 5)
    result = []
    result_rest = []
    time.perf_counter()
    init_pieces()

    f = open("./day_17/lmove.txt")
    result = []
    result = list(map(int, f.read()[:-1].split("\n")))
    f.close()
    f = open("./day_17/lrest.txt")
    result_rest = []
    result_rest = list(map(int, f.read()[:-1].split("\n")))
    f.close()
    start_cycle = 1
    cycle_length = 348 - start_cycle
    res = sum(result[:start_cycle])
    goal -= (l_moves * 5) * start_cycle
    vcycle = sum(result[start_cycle : start_cycle + cycle_length])
    res += (goal // (cycle_length * l_moves * 5)) * vcycle
    goal = goal % (cycle_length * l_moves * 5)
    print(goal)
    index_v = goal // (l_moves * 5)
    print(index_v)
    res += sum(result[1 : 1 + index_v])
    res += result_rest[index_v + 2]
    print(res)


if __name__ == "__main__":
    main()
