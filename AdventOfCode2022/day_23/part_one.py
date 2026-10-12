"""Advent of Code 2022 - Day 23 - Part One"""

import numpy as np

test_case = 0


class Elf:
    directions = [
        [(-1, -1), (0, -1), (1, -1)],  # north
        [(-1, 1), (0, 1), (1, 1)],  # south
        [(-1, -1), (-1, 0), (-1, 1)],  # west
        [(1, 1), (1, 0), (1, -1)],  # est
    ]
    if test_case == 2:
        truth = np.zeros((10, 10))
        positions = np.zeros((10, 10))

    elif test_case == 1:
        truth = np.zeros((40, 40))
        positions = np.zeros((40, 40))
    else:
        truth = np.zeros((150, 150))
        positions = np.zeros((150, 150))

    def __init__(self, position, offset, next=None):
        self.position = position
        self.positions[position] = 1
        self.placed = False
        self.next = next
        self.offset = offset
        self.move = None

    def check_position(self):
        self.move = None
        has_to_move = False
        for index in range(len(self.directions)):
            current_direction = self.directions[(self.offset + index) % 4]
            for item in current_direction:
                if self.positions[tuple(np.add(self.position, item))]:
                    has_to_move = True
                    break
        if not has_to_move:
            return 0
        for index in range(len(self.directions)):
            current_direction = self.directions[(self.offset + index) % 4]
            found = False
            for item in current_direction:
                pos = tuple(np.add(self.position, item))
                if self.positions[pos]:
                    found = True
            if not found:
                self.move = tuple(np.add(self.position, current_direction[1]))
                break
        return 0

    def mark_position(self):
        if self.move:
            self.truth[self.move] -= 1

    def travel(self):
        self.offset += 1
        if self.move:
            if self.truth[self.move] == -1:
                self.truth[self.move] = 0
                self.positions[self.position] = 0
                self.position = self.move
                self.positions[self.position] = 1
            else:
                self.truth[self.move] = 0

        return 0

    def visualize(self):
        start = False
        for c, line in enumerate(np.swapaxes(self.positions, 0, 1)):
            if sum(line) == 0 and not start:
                continue
            start = True
            line_str = f"{c:02d}"
            for item in line:
                if item:
                    line_str += "#"
                else:
                    line_str += "."
            print(line_str)


def main():
    result = []
    file = open("./input.txt")
    r = 15
    if test_case == 1:
        file.close()
        file = open("./test_input.txt")
    elif test_case == 2:
        r = 2
        file.close()
        file = open("./test_input_2.txt")

    content = file.read().split("\n")
    elves = []
    for y, line in enumerate(content):
        for x, item in enumerate(line):
            if item == "#":
                elves.append(Elf((x + r, y + r), 0))
                continue
            elif item == ".":
                continue
            print(f"what char?{item}")
    elves[0].visualize()
    print(sum(sum(elves[0].positions)))

    for _cycle in range(10):
        print("start of cycle")
        elves[0].visualize()
        for elf in elves:
            elf.check_position()

        for elf in elves:
            elf.mark_position()

        for elf in elves:
            elf.travel()
            # elves[0].visualize()

        print("end of cycle")
        elves[0].visualize()

    print("travel finished")
    elves[0].visualize()
    print("finding result")
    current_result = elves[0].positions[:, :]
    while sum(current_result[0]) == 0:
        current_result = current_result[1:, :]
    while sum(current_result[-1, :]) == 0:
        current_result = current_result[:-1, :]
    current_result = np.swapaxes(current_result, 0, 1)
    while sum(current_result[0]) == 0:
        current_result = current_result[1:, :]
    while sum(current_result[-1, :]) == 0:
        current_result = current_result[:-1, :]

    result = current_result.shape[0] * current_result.shape[1] - sum(
        sum(current_result)
    )
    return int(result)


if __name__ == "__main__":
    main()
