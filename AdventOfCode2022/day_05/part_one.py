"""Advent of Code 2022 - Day 05 - Part One"""

import re

test_set = False


def test_content():
    fake = """    [D]
[N] [C]
[Z] [M] [P]""".split("\n")
    return fake


def test_moves_content():
    fake = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split("\n")
    return fake


def main():
    file = open("./input.txt")
    content = file.read().split("\n")
    # read the setup :
    tab = [[] for item_placeholder in range(9)]
    setup = content[:9]
    if test_set:
        setup = test_content()
    for line in setup:
        line += " "
        plates = map(lambda *x: x, *([iter(line)] * 4))
        for index, plate in enumerate(plates):
            plate = "".join(plate).strip()
            if plate:
                tab[index] = [plate] + tab[index]
    if test_set:
        print(tab)

    moves_content = content[10:]
    if test_set:
        moves_content = test_moves_content()
    moves = []

    def define_moves(move_content):
        return re.findall("[0-9]+", move_content)

    moves = map(define_moves, moves_content)
    for move in moves:
        number_of_move = int(move[0])
        from_pile = int(move[1])
        to_pile = int(move[2])
        for _move_number in range(number_of_move):
            if not tab[from_pile - 1]:
                break
            tab[to_pile - 1].append(tab[from_pile - 1].pop(-1))
            if test_set:
                print(f"tab:{tab}\n")
    result = ""
    for pile in tab:
        if pile:
            result += pile[-1][1]
    return result


if __name__ == "__main__":
    print(main())
