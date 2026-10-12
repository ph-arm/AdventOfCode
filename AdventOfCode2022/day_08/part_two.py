"""Advent of Code 2022 - Day 08 - Part Two"""

import numpy as np

test_case = False

"""
30373
25512
65332
33549
35390
"""


def mocked_content():
    temp = """30373
25512
65332
33549
35390""".split("\n")
    return temp


def main():
    result = []
    file = open("./input.txt")
    content = file.read().split("\n")
    if test_case:
        content = mocked_content()

    def format_to_int(content):
        result = list(map(int, list(content)))
        return result

    array_content = list(map(format_to_int, content))
    np_content = np.array(array_content)
    truth_array = np.zeros((len(content), len(content[0])))

    def calculate_view(row_index, column_index):
        res = 1
        local_res = 0
        max_tree = np_content[row_index, column_index]
        # vertical :
        for tree in np_content[row_index + 1 :, column_index]:
            local_res += 1
            if tree >= max_tree:
                break
        res *= local_res
        local_res = 0
        for tree in np_content[row_index - 1 :: -1, column_index]:
            local_res += 1
            if tree >= max_tree:
                break
        res *= local_res
        # horizontal :
        local_res = 0
        for tree in np_content[row_index, column_index + 1 :]:
            local_res += 1
            if tree >= max_tree:
                break
        res *= local_res

        local_res = 0
        for tree in np_content[row_index, column_index - 1 :: -1]:
            local_res += 1
            if tree >= max_tree:
                break
        res *= local_res
        return res

    view = 0
    for iy, ix in np.ndindex(len(content) - 2, len(content[0]) - 2):
        result = calculate_view(iy + 1, ix + 1)
        truth_array[iy + 1, ix + 1] = result
        view = max(view, result)
    if test_case:
        print(truth_array)
    return int(view)


if __name__ == "__main__":
    print(main())

# answer 410400
