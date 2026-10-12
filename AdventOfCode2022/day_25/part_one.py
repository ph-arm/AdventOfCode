"""Advent of Code 2022 - Day 25 - Part One"""

test_case = 0


def main():
    result = []
    file = open("./input.txt")
    if test_case == 1:
        file.close()
        file = open("./test_input.txt")

    content = file.read()
    result = 0
    for line in content.split("\n"):
        ordered = line[::-1]

        def conv_from_elf(
            ordered,
        ):
            current = 0
            item = 1
            for ch in ordered:
                if ch == "-":
                    current -= item
                if ch == "=":
                    current -= 2 * item
                if ch == "1":
                    current += item
                if ch == "2":
                    current += 2 * item
                item *= 5
            print(f"line {line}\ncurrent: {current}\n")
            return current

        result += conv_from_elf(ordered)

    print(f"result is :{result}")

    # translated to:
    def conv_to_elf(result):
        transcript = ""
        while result:
            c = result % 5
            if c == 0:
                transcript += "0"
            if c == 1:
                transcript += "1"
            if c == 2:
                transcript += "2"
            if c == 3:
                transcript += "="
                result += 2
            if c == 4:
                transcript += "-"
                result += 1
            result = result // 5
            print(f"transcript: {transcript}, result:{result}")
        return transcript[::-1]

    return conv_to_elf(result)


# test : 2=-1=0.

if __name__ == "__main__":
    print(main())
