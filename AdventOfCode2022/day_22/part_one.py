"""Advent of Code 2022 - Day 22 - Part One"""

import numpy as np

test_case = False


def main():
    result = []
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().split("\n")
    lmax = max(map(len, content))
    content_array = []
    for line in content:
        if not line:
            break
        line_array = np.array(list(line))
        line_array.resize((lmax), refcheck=False)
        content_array.append(line_array)
    res = np.array(content_array)
    start_point = []
    for index, x in np.ndenumerate(res):
        if x == ".":
            start_point = index
            break

    print(f"start point : {start_point}")
    current_point = list(start_point)
    current_direction = [0]

    def move_right():
        move_offset = 1
        while 1:
            if res[current_point[0], (current_point[1] + move_offset) % lmax] == "":
                move_offset += 1
                continue
            if res[current_point[0], (current_point[1] + move_offset) % lmax] == ".":
                current_point[1] = (current_point[1] + move_offset) % lmax
            move_offset = 0

            break
        return move_offset

    def move_left():
        move_offset = 1
        while 1:
            if res[current_point[0], (current_point[1] - move_offset) % lmax] == "":
                move_offset += 1
                continue
            if res[current_point[0], (current_point[1] - move_offset) % lmax] == ".":
                current_point[1] = (current_point[1] - move_offset) % lmax

            move_offset = 0
            break
        return move_offset

    def move_up():
        move_offset = 1
        while 1:
            if (
                res[
                    (current_point[0] - move_offset) % res.shape[0],
                    (current_point[1]),
                ]
                == ""
            ):
                move_offset += 1
                continue
            if (
                res[
                    (current_point[0] - move_offset) % res.shape[0],
                    (current_point[1]),
                ]
                == "."
            ):
                current_point[0] = (current_point[0] - move_offset) % res.shape[0]
            move_offset = 0
            break
        return move_offset

    def move_down():
        move_offset = 1
        while 1:
            if (
                res[(current_point[0] + move_offset) % res.shape[0], current_point[1]]
                == ""
            ):
                move_offset += 1
                continue
            if (
                res[(current_point[0] + move_offset) % res.shape[0], (current_point[1])]
                == "."
            ):
                current_point[0] = (current_point[0] + move_offset) % res.shape[0]
            move_offset = 0
            break
        return move_offset

    move_transition = {
        "U": move_up,
        "D": move_down,
        "R": move_right,
        "L": move_left,
    }
    transition = ["R", "D", "L", "U"]
    direction = ""
    steps = 0

    def process_instruction():
        # print(f"steps: {steps}")
        for _ in range(steps):
            tr = transition[current_direction[0] % 4]
            move_transition[tr]()
        if direction == "R":
            current_direction[0] += 1
        else:
            current_direction[0] -= 1

    instructions = content[-1]
    index = 0
    steps = ""
    while index < len(instructions):
        if instructions[index].isnumeric():
            steps += instructions[index]
        else:
            direction = instructions[index]
            steps = int(steps)
            process_instruction()
            if test_case:
                print(
                    f"current p : {current_point} - current d : {transition[current_direction[0] % 4]} - {steps}"
                )

            steps = ""
        index += 1
    last_direction = current_direction[0] % 4
    if steps:
        steps = int(steps)
        process_instruction()
    result = (
        (current_point[0] + 1) * 1000 + (current_point[1] + 1) * 4 + last_direction % 4
    )
    return result


if __name__ == "__main__":
    print(main())
