"""Advent of Code 2022 - Day 16 - first star"""

import re

test_case = False


def mocked_content():
    pass


def main():
    file = open("./day_16/input.txt")
    START = 28
    if test_case:
        START = 0
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
    count = 30
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

    def scenario(
        position_elf,
        position_elephant,
        minutes,
        opened,
        v_opened,
        pression,
        best_pression,
        elf_traveling,
        elephant_traveling,
        next_valve,
    ):
        if elf_traveling and elephant_traveling:
            if elf_traveling <= elephant_traveling:
                l_pression = (
                    pression
                    + elf_traveling * v_opened
                    + (elf_traveling - 1) * next_valve
                )
                temp = scenario(
                    position_elf,
                    position_elephant,
                    minutes - elf_traveling,
                    opened,
                    v_opened + next_valve,
                    l_pression,
                    best_pression,
                    0,
                    elephant_traveling - elf_traveling,
                    0,
                )
            else:
                l_pression = (
                    pression
                    + elephant_traveling * v_opened
                    + (elephant_traveling - 1) * next_valve
                )
                temp = scenario(
                    position_elf,
                    position_elephant,
                    minutes - elephant_traveling,
                    opened,
                    v_opened + next_valve,
                    l_pression,
                    best_pression,
                    elf_traveling - elephant_traveling,
                    0,
                    0,
                )
            return temp
        count_nodes[0] += 1
        if count_nodes[0] % 1000000 == 0:
            print(count_nodes[0])
        if len(opened) == ml_open:
            print("open all")
            return pression + v_opened * minutes + next_valve * (minutes - 1)
        if minutes == 1:
            return pression + v_opened
        if minutes == 0:
            return pression
        l_best_pression = best_pression
        # stay here and open, if not already open :
        is_elf_moving = True
        if (
            not elf_traveling
            and position_elf not in opened
            and tubes[position_elf][0] > 0
        ):
            l_opened = opened.copy()
            l_opened.append(position_elf)
            is_elf_moving = False
            return scenario(
                position_elf,
                position_elephant,
                minutes,
                l_opened,
                v_opened,
                pression,
                best_pression,
                elf_traveling,
                elephant_traveling,
                next_valve + tubes[position_elf][0],
            )

        is_elephant_moving = True
        if (
            not elephant_traveling
            and position_elephant not in opened
            and tubes[position_elephant][0] > 0
        ):
            l_opened = opened.copy()
            l_opened.append(position_elephant)
            is_elephant_moving = False
            return scenario(
                position_elf,
                position_elephant,
                minutes,
                l_opened,
                v_opened,
                pression,
                best_pression,
                elf_traveling,
                elephant_traveling,
                next_valve + tubes[position_elephant][0],
            )

        if (position_elf == START) or (is_elf_moving and not elf_traveling):
            l_best_pression = best_pression
            have_move = False
            for move in tubes[position_elf][2]:
                if move[0] == 0:
                    continue
                if minutes - move[2] < 0:
                    continue
                if (
                    translation[move[1]] in opened
                    or translation[move[1]] == position_elephant
                ):
                    continue
                elf_l_position = translation[move[1]]
                elf_l_traveling = move[2] + 1
                temp = scenario(
                    elf_l_position,
                    position_elephant,
                    minutes,
                    opened,
                    v_opened,
                    pression,
                    best_pression,
                    elf_l_traveling,
                    elephant_traveling,
                    next_valve,
                )
                have_move = True
                l_best_pression = max(l_best_pression, temp)
            if not have_move:
                temp = scenario(
                    99,
                    position_elephant,
                    minutes,
                    opened,
                    v_opened,
                    pression,
                    best_pression,
                    minutes,
                    elephant_traveling,
                    next_valve,
                )
                if temp > l_best_pression:
                    print(temp)
                l_best_pression = max(l_best_pression, temp)
            return l_best_pression

        if (position_elephant == START) or (
            is_elephant_moving and not elephant_traveling
        ):
            have_move = False
            for move in tubes[position_elephant][2]:
                if move[0] == 0:
                    continue
                if minutes - move[2] < 0:
                    continue
                if (
                    translation[move[1]] in opened
                    or translation[move[1]] == position_elf
                ):
                    continue
                elephant_l_position = translation[move[1]]
                elephant_l_traveling = move[2] + 1
                temp = scenario(
                    position_elf,
                    elephant_l_position,
                    minutes,
                    opened,
                    v_opened,
                    pression,
                    l_best_pression,
                    elf_traveling,
                    elephant_l_traveling,
                    next_valve,
                )
                l_best_pression = max(l_best_pression, temp)
            if not have_move:
                temp = scenario(
                    position_elf,
                    99,
                    minutes,
                    opened,
                    v_opened,
                    pression,
                    l_best_pression,
                    elf_traveling,
                    minutes,
                    next_valve,
                )
                if temp > l_best_pression:
                    print(temp)
                l_best_pression = max(l_best_pression, temp)
            return l_best_pression

        l_best_pression = max(l_best_pression, v_opened * minutes + pression)
        return l_best_pression

    a = scenario(START, START, 27, [], 0, 0, 0, 0, 0, 0)

    print(a)


"""        position_elf,
        position_elephant,
        minutes,
        opened,
        v_opened,
        pression,
        best_pression,
        elf_traveling,
        elephant_traveling,
        next_valve,"""

if __name__ == "__main__":
    main()
