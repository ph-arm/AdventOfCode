"""Advent of Code 2022 - Day 10 - Part Two"""

import numpy as np

test_case = False


def main():
    file = open("./input.txt")
    if test_case:
        file = open("./test_input.txt")

    content = file.read().split("\n")

    def format_to_int(content):
        if content[0] == "n":
            return ["noop"]
        cl = content.split(" ")
        return [cl[0], int(cl[1])]

    moves = list(map(format_to_int, content))
    max_cycle = len(moves) * 2
    value_cycle = np.zeros(max_cycle)
    drawing = np.zeros((6, 40))
    index = 1
    for move in moves:
        if move[0] == "noop":
            index += 1
        else:
            value_cycle[index + 2] = move[1]
            index += 2

    position = 1
    for cycle_index in range(1, 240):
        row = (cycle_index) // 40
        position += value_cycle[cycle_index]
        pixel_position = (cycle_index - 1) % 40
        if abs(pixel_position - position) <= 1:
            drawing[row, pixel_position] = 1
    return _ocr(drawing)


# Standard Advent of Code 4x6 pixel font (columns 5 apart: 4 lit + 1 gap).
_LETTERS_4X6 = {
    (".##.", "#..#", "#..#", "####", "#..#", "#..#"): "A",
    ("###.", "#..#", "###.", "#..#", "#..#", "###."): "B",
    (".##.", "#..#", "#...", "#...", "#..#", ".##."): "C",
    ("####", "#...", "###.", "#...", "#...", "####"): "E",
    ("####", "#...", "###.", "#...", "#...", "#..."): "F",
    (".##.", "#..#", "#...", "#.##", "#..#", ".###"): "G",
    ("#..#", "#..#", "####", "#..#", "#..#", "#..#"): "H",
    ("..##", "...#", "...#", "...#", "#..#", ".##."): "J",
    ("#..#", "#.#.", "##..", "#.#.", "#.#.", "#..#"): "K",
    ("#...", "#...", "#...", "#...", "#...", "####"): "L",
    (".##.", "#..#", "#..#", "#..#", "#..#", ".##."): "O",
    ("###.", "#..#", "#..#", "###.", "#...", "#..."): "P",
    ("###.", "#..#", "#..#", "###.", "#.#.", "#..#"): "R",
    (".###", "#...", "#...", ".##.", "...#", "###."): "S",
    ("#..#", "#..#", "#..#", "#..#", "#..#", ".##."): "U",
    ("#..#", "#..#", ".##.", "..#.", "..#.", "..#."): "Y",
    ("####", "...#", "..#.", ".#..", "#...", "####"): "Z",
}


def _ocr(drawing):
    result = ""
    for col in range(0, drawing.shape[1], 5):
        glyph = tuple(
            "".join("#" if drawing[row, col + k] else "." for k in range(4))
            for row in range(6)
        )
        result += _LETTERS_4X6.get(glyph, "?")
    return result


if __name__ == "__main__":
    print(main())
