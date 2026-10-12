"""Advent of Code 2022 - Day 16 - first star"""

import re

test_case = False


def mocked_content():
    pass


def main():
    file = open("./day_16/input.txt")
    if test_case:
        file.close()
        file = open("./day_16/test_input.txt")
    content = file.read().split("\n")
    tubes = []

    def format_line(line):
        value = int(re.findall("[-0-9]+", line)[0])
        c_line = line.split(" ")
        res = []
        res.append(value)
        res.append(c_line[1])
        moves = []
        for item in c_line[::-1]:
            if len(item) > 3:
                break
            moves.append([0, item.replace(",", ""), 1])
        res.append(moves)
        return res

    tubes = list(map(format_line, content))
    translation = {}
    for index, tube in enumerate(tubes):
        translation[tube[1]] = index
    for tube in tubes:
        for move in tube[2]:
            move[0] = tubes[translation[move[1]]][0]
    count = 15
    while count:
        count -= 1
        for tube in tubes:
            if tube[0] == 0 and tube[1] != "AA":
                continue
            moves = tube[2]
            new_moves = []
            for move in moves:
                if move[0] > 0:
                    new_moves.append(move)
            for move in moves:
                dest = tubes[translation[move[1]]]
                for dest_move in dest[2]:
                    if dest_move[1] not in [tube[1], move[1]]:
                        found = False
                        for lmove in new_moves:
                            if (
                                lmove[1] == dest_move[1]
                                and dest_move[2] + move[2] < lmove[2]
                            ):
                                lmove[2] = dest_move[2] + move[2]
                                found = True
                            elif lmove[1] == dest_move[1]:
                                found = True
                        if found:
                            continue
                        new_moves.append(
                            [dest_move[0], dest_move[1], dest_move[2] + move[2]]
                        )
            new_moves.sort()
            tube[2] = new_moves
    ml_open = 0
    for i in tubes:
        if i[0] > 0:
            ml_open += 1
    count_nodes = [0]
    print("finish shortening graph")

    def scenario(position, minutes, opened, v_opened, pression, best_pression):
        count_nodes[0] += 1
        if count_nodes[0] % 1000 == 0:
            print(count_nodes[0])
        if len(opened) == ml_open:
            # print("open all")
            return pression + v_opened * minutes
        if minutes == 1:
            return pression + v_opened
        if minutes == 0:
            return pression
        l_pression = v_opened + pression
        l_best_pression = best_pression
        # stay here and open, if not already open :
        if position not in opened and tubes[position][0] > 0:
            l_minute = minutes - 1
            l_opened = opened.copy()
            l_opened.append(position)
            if l_opened in [
                [3],
                [3, 1],
                [3, 1, 9],
                [3, 1, 9, 7],
                [3, 1, 9, 7, 4],
                [3, 1, 9, 7, 4, 2],
            ]:
                print("in the path")
            temp = scenario(
                position,
                l_minute,
                l_opened,
                v_opened + tubes[position][0],
                l_pression,
                best_pression,
            )
            l_best_pression = max(l_best_pression, temp)
        else:
            for move in tubes[position][2]:
                if move[0] == 0:
                    continue
                if minutes - move[2] < 0:
                    continue
                if translation[move[1]] in opened:
                    continue
                l_position = translation[move[1]]
                temp = scenario(
                    l_position,
                    minutes - move[2],
                    opened,
                    v_opened,
                    l_pression + (move[2] - 1) * v_opened,
                    best_pression,
                )
                l_best_pression = max(l_best_pression, temp)
        l_best_pression = max(l_best_pression, v_opened * minutes + pression)
        return l_best_pression

    a = scenario(28, 30, [], 0, 0, 0)
    print(a)


if __name__ == "__main__":
    main()
