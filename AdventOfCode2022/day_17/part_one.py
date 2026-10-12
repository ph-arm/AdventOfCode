"""Advent of Code 2022 - Day 17 - Part One"""

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
    index = 0
    while 1:
        piece = np.zeros((7, 8))
        for x, y in pieces[index % 5]:
            piece[x, y] = 1
        index += 1
        yield piece


def solidify(current):
    for index, x in np.ndenumerate(current):
        if x:
            current[index] = 2


def check_left(current):
    for index, x in np.ndenumerate(current):
        if x == 1:
            if index[0] == 0:
                return 0
            if current[index[0] - 1, index[1]] == 2:
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


def check_down(current):
    for index, x in np.ndenumerate(current):
        if x == 1:
            if index[1] == 0:
                return 0
            if current[index[0], index[1] - 1] == 2:
                return 0
    return 1


def make_move(current, move):
    to_1 = []
    for index, x in np.ndenumerate(current):
        if x == 1:
            current[index] = 0
            to_1.append((index[0] + move[0], index[1] + move[1]))
    for index in to_1:
        current[index] = 1
    return 0


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
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().strip()
    moves = get_moves(content)
    print(f"{len(moves)} moves loaded")
    zone = np.array([[2], [2], [2], [2], [2], [2], [2]])
    visualization(zone)
    index = 0
    current_height = 0
    for c, i in enumerate(init_pieces()):
        zone = np.column_stack((zone, i))
        # visualization(zone)
        advance = True
        while advance:
            move = moves[index % len(moves)]
            index += 1
            if move[0] == 1:
                validation = check_right(zone)
            else:
                validation = check_left(zone)
            if validation:
                make_move(zone, move)
            if check_down(zone):
                make_move(zone, (0, -1))
            else:
                solidify(zone)
                advance = False
        # cleanning the top:
        while not sum(zone[:, -1]):
            zone = zone[:, :-1]
        if c == 2022:
            break
        if c % 100 == 0 and c:
            target = 0
            for row in range(1, zone.shape[1] - 3):
                if sum(zone[:, row : row + 3].max(axis=1)) == 14:
                    # print("shorting the tower")
                    target = max(row, target)
            zone = zone[:, target:]
            current_height += target
            print(c)
    print(len(zone[0]) - 1 + current_height)
    return len(zone[0]) - 1 + current_height


if __name__ == "__main__":
    main()
