"""Advent of Code 2023 - Day 03 - Part One"""


def main():
    test = 0
    INPUT = "input.txt"
    if test:
        INPUT = "input_sample.txt"
    f = open(INPUT)
    data = f.readlines()
    data = [item.strip() for item in data]
    not_char = "0123456789."
    ll = len(data[0]) - 1
    print(ll)

    def process(word, item, c):
        ym = max(min(item) - 1, 0)
        ymax = min(max(item) + 1, ll)
        for i in range(ym, ymax + 1):
            lines = data[max(c - 1, 0) : min(c + 2, len(data))]
            for line in lines:
                if line[i] not in not_char:
                    return True
        return False

    total = 0
    for c, line in enumerate(data):
        line.strip()
        items = []
        current = False
        word = ""
        for c2, char in enumerate(line):
            if char.isdigit():
                if current:
                    word += char
                else:
                    current = True
                    word = char
                items.append(c2)
                if c2 != len(line) - 1:
                    continue
            if current:
                if process(word, items, c):
                    total += int(word)
                    # print(total)
                current = False
                items = []
    return total


if __name__ == "__main__":
    print(main())
