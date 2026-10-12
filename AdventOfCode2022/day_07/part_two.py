"""Advent of Code 2022 - Day 07 - Part Two"""

import bisect


class Directory:
    directory = ""
    result = []

    def __init__(self, name="", parent=None) -> None:
        self.directory = name
        self.parent = parent
        self.files = []
        self.size_count = -1
        self.children = []

    def size(self):
        if self.size_count < 0:
            total_size = sum(self.files)
            for child in self.children:
                total_size += child.size()
            self.result.append(total_size)
        self.size_count = total_size
        return self.size_count


def process_command(cdr, input, output):
    input_array = input.split(" ")
    current_directory = cdr[0]
    if input_array[1] == "ls":
        for line in output:
            prefix, name = line.split(" ")
            if prefix == "dir":
                current_directory.children.append(Directory(name, current_directory))
            else:
                current_directory.files.append(int(prefix))
    if input_array[1] == "cd":
        if input_array[2] == "..":
            cdr[0] = current_directory.parent
        else:
            for children in current_directory.children:
                if children.directory == input_array[2]:
                    cdr[0] = children


def main():
    result = []
    file = open("./input.txt")
    content = file.read().split("\n")
    root = Directory()
    current_directory_reference = [root]
    input_command = content[1]
    output = []
    for line in content[2:]:
        if line[0] == "$":
            process_command(current_directory_reference, input_command, output)
            input_command = line
            output = []
            continue
        output.append(line)
    process_command(current_directory_reference, input_command, output)
    root.size()
    total_space = 70000000
    target_space = 30000000
    free = total_space - root.size_count
    minimum_to_free = target_space - free
    result = root.result
    result.sort()
    print(result)
    print(result[bisect.bisect_right(result, minimum_to_free)])
    return result[bisect.bisect_right(result, minimum_to_free)]


if __name__ == "__main__":
    main()


# answer 2195372
