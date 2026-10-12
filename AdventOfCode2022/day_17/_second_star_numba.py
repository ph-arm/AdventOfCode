"""Advent of Code 2022 - Day 17 - second star"""
# 1602880798912 too low
# 1602881844396 nope
# --> 1602881844347
# 1602882621688 too high
# 1602882540808 too high

import time

import numpy as np
from numba import njit

test_case = False


@njit(fastmath=True)
def remove_empty(zone):
    r_off = -4
    while not np.any(zone[:, r_off]):
        r_off -= 1
    zone = zone[:, : r_off + 1]
    return zone


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
        piece = np.zeros((7, 7))
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


def check_down(current, p):
    for point in p:
        if point[1] == 0:
            return 0
        if current[point[0], point[1] - 1] == 2:
            return 0
    return 1


def make_move(current, move, p):
    to_1 = []
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


@njit(fastmath=True)
def scan_piece(current):
    y_offset = current.shape[1] - 6
    # y_offset = 0
    piece = []
    for index, x in np.ndenumerate(current[:, -6:]):
        if x == 1:
            piece.append((index[0], index[1] + y_offset))
    return piece


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
    index = 0
    current_height = 0
    goal = 1000000000000
    rest = goal % (l_moves * 5)
    r = 0
    result = []
    result_rest = []
    c = -1
    start_time = time.perf_counter()
    pieces = init_pieces()
    prev = 0
    while 1:
        if c % 50000 == 0:
            print(f"pieces : {c}  - time : {time.perf_counter()-start_time}")
        c += 1
        i = pieces[c % 5]
        # zone = np.column_stack((zone, i))
        zone = np.concatenate((zone, i), axis=1)
        # visualization(zone)
        advance = 1
        p = scan_piece(zone)
        lmove = len(moves)
        while advance:
            move = moves[index % lmove]
            if move[0] == 1:
                validation = check_right2(zone, p)
            else:
                validation = check_left2(zone, p)
            if validation:
                p = make_move(zone, move, p)

            if check_down(zone, p):
                p = make_move(zone, (0, -1), p)

            else:
                solidify2(zone, p)
                # visualization(zone)
                advance = 0
            index += 1

        # cleanning the top:
        zone = remove_empty(zone)
        if (c) % (l_moves * 5) == 0 and c:
            r += 1
            result.append(len(zone[0]) + current_height - prev)
            prev = len(zone[0]) + current_height
        if (c - 1) % (l_moves * 5) == rest and c:
            result_rest.append(len(zone[0]) + current_height - prev)
        if c % 100 == 0 and c:
            target = 0
            for row in range(1, zone.shape[1] - 3):
                if np.sum(zone[:, row : row + 3].max(axis=1)) == 14:
                    target = row
            zone = zone[:, target:]
            current_height += target
        if c == 2021:
            print(len(zone[0]) + current_height - 1)
        if r % 100 == 0 and r:
            for start in range(1, 30):
                found = False
                for index_item in range(10, len(result) - 60):
                    cycle = True
                    for i in range(20):
                        if result[start + i] != result[start + index_item + i]:
                            cycle = False
                            break
                    if cycle:
                        print(f"found : start {start} index {index_item}")
                        found = True
                        break
                if found:
                    break
            if found:
                start_cycle = start
                cycle_length = index_item
                print(f"cycle detected:{start_cycle} to {index_item}")
                break

    f = open("./day_17/lmove.txt", "w")
    for item in result:
        f.write(str(item) + "\n")
    f.close()
    f = open("./day_17/lrest.txt", "w")
    for item in result_rest:
        f.write(str(item) + "\n")
    f.close()

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
