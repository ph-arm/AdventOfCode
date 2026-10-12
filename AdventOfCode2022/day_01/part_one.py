"""Advent of Code 2022 - Day 01 - Part One"""


def main():
    file = open("./input.txt")
    content = file.read()
    max_carry = 0
    current_elf = 0
    for line in content.split("\n"):
        if line:
            current_elf += int(line)
        else:
            max_carry = max(current_elf, max_carry)
            current_elf = 0
    print(f"maximum calory carried is {max_carry}")
    return max_carry


if __name__ == "__main__":
    main()
