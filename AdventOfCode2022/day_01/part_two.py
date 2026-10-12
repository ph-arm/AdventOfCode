"""Advent of Code 2022 - Day 01 - Part Two"""


def main():
    file = open("./input.txt")
    content = file.read()
    max_carriers = [0] * 3
    current_elf = 0
    for line in content.split("\n"):
        if line:
            current_elf += int(line)
        elif current_elf > max_carriers[0]:
            max_carriers[0] = current_elf
            max_carriers.sort()
            current_elf = 0
        else:
            current_elf = 0
    print(f"total calory carried by top 3 is {sum(max_carriers)}")
    return sum(max_carriers)


if __name__ == "__main__":
    main()
