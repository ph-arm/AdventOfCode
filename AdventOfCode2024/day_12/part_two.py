"""Advent of Code 2024 - Day 12 - Part Two"""

from shared import *


def main():
    mappings = [[0 for i in mt[0]] for j in mt]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    count = 0

    def find_region_2(xs, ys):
        if mappings[ys][xs] != 0:
            return 0, 0, ""
        nonlocal count
        rv = str(mt[ys][xs]) + str(count)
        r = mt[ys][xs]
        count += 1
        mappings[ys][xs] = rv
        queue = [(xs, ys)]
        a = 1
        p = 0
        ymim, xmin = ys, xs
        ymax, xmax = ys, xs
        while len(queue):
            x, y = queue.pop(0)
            for move in moves:
                if (
                    x + move[0] >= 0
                    and x + move[0] < len(mt[0])
                    and y + move[1] >= 0
                    and y + move[1] < len(mt)
                ):
                    if (
                        mappings[y + move[1]][x + move[0]] == 0
                        and mt[y + move[1]][x + move[0]] == r
                    ):
                        mappings[y + move[1]][x + move[0]] = rv
                        xmin = min(xmin, x + move[0])
                        xmax = max(xmax, x + move[0])
                        ymim = min(ymim, y + move[1])
                        ymax = max(ymax, y + move[1])
                        a += 1
                        queue.append((x + move[0], y + move[1]))
        # calc faces :
        # scaning horizontal faces:
        prec_up = 0
        prec_down = 0
        for i in range(ymim, ymax + 1):
            prec_up = 0
            prec_down = 0
            for j in range(xmin, xmax + 1):
                if mappings[i][j] == rv:
                    if i == ymim or mappings[i - 1][j] != rv:
                        # check if the case up is a frontier else increment p if not already done
                        if not prec_up:
                            p += 1
                            prec_up = 1

                    else:
                        prec_up = 0

                    if i == ymax or mappings[i + 1][j] != rv:
                        # check if the case up is a frontier else increment p if not already done
                        if not prec_down:
                            p += 1
                            prec_down = 1
                    else:
                        prec_down = 0
                else:
                    prec_up = 0
                    prec_down = 0
        # calc faces :
        # scaning vertical faces:
        for j in range(xmin, xmax + 1):
            prec_right = 0
            prec_left = 0
            for i in range(ymim, ymax + 1):
                if mappings[i][j] == rv:
                    if j == xmin or mappings[i][j - 1] != rv:
                        # check if the case up is a frontier else increment p if not already done
                        if not prec_left:
                            p += 1
                            prec_left = 1

                    else:
                        prec_left = 0

                    if j == xmax or mappings[i][j + 1] != rv:
                        # check if the case up is a frontier else increment p if not already done
                        if not prec_right:
                            p += 1
                            prec_right = 1
                    else:
                        prec_right = 0
                else:
                    prec_right = 0
                    prec_left = 0
        return p, a, rv

    a = 0
    r = 0
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            # print(i, j)
            pl, al, reg = find_region_2(i, j)
            if al:
                print(f"reg: {reg},al: {al},pl: {pl},")
            r += pl * al
            a += al
    return r


if __name__ == "__main__":
    print(main())
