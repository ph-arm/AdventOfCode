"""Advent of Code 2022 - Day 13 - Part One"""

test_case = False


def mocked_content():
    pass


def main():
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().split("\n")
    list_of_pairs = []
    current_pair = []

    for line in content:
        if not line:
            list_of_pairs.append(current_pair)
            current_pair = []
            continue
        current_pair.append(line)
    list_of_pairs.append(current_pair)

    def comp(a, b):
        if isinstance(a, int) and not isinstance(b, int):
            return comp([a], b)
        if not isinstance(a, int) and isinstance(b, int):
            return comp(a, [b])
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return 1
            if a == b:
                return 0
            if a > b:
                return -1
        if len(a) > len(b):
            for index in range(len(b)):
                c = comp(a[index], b[index])
                if c == 0:
                    continue
                return c
            return -1
        if len(a) < len(b):
            for index in range(len(a)):
                c = comp(a[index], b[index])
                if c == 0:
                    continue
                return c
            return 1
        for index in range(len(a)):
            c = comp(a[index], b[index])
            if c == 0:
                continue
            return c
        return 0

    total = 0
    count = 1
    for pair in list_of_pairs:
        print("pair")
        print(pair)
        lp = eval(pair[0])
        rp = eval(pair[1])
        print(lp, rp)
        if comp(lp, rp) > 0:
            res = True
            total += count
        elif comp(lp, rp) < 0:
            res = False
        else:
            res = "errreur"
        count += 1
        print(res)
    return total


if __name__ == "__main__":
    print(main())
