"""Advent of Code 2022 - Day 08 - Part One"""

import numpy as np

test_case = False


def mocked_content():
    temp = """30373
25512
65332
33549
35390""".split("\n")
    return temp


def main():
    file = open("./input.txt")
    content = file.read().split("\n")
    if test_case:
        content = mocked_content()

    def format_to_int(content):
        result = list(map(int, list(content)))
        return result

    array_content = list(map(format_to_int, content))
    np_content = np.array(array_content)
    # vertical :
    truth_array = np.zeros((len(content), len(content[0])))
    for column_index in range(len(content[0])):
        max_tree = -1
        for index, tree in enumerate(np_content[:, column_index]):
            if tree > max_tree:
                truth_array[index, column_index] = 1
                max_tree = tree
        max_tree = -1
        for index, tree in enumerate(np_content[::-1, column_index]):
            if tree > max_tree:
                truth_array[-1 - index, column_index] = 1
                max_tree = tree

    # horizontal :
    for row_index in range(len(content)):
        max_tree = -1
        for index, tree in enumerate(np_content[row_index, :]):
            if tree > max_tree:
                truth_array[row_index, index] = 1
                max_tree = tree
        max_tree = -1
        for index, tree in enumerate(np_content[row_index, ::-1]):
            if tree > max_tree:
                truth_array[row_index, -1 - index] = 1
                max_tree = tree

    result = int(sum(sum(truth_array)))
    if test_case:
        print(truth_array)
    return result


if __name__ == "__main__":
    print(main())

# answer 1688
