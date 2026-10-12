"""Advent of Code 2022 - Day 20 - Part Two"""

test_case = False


class node:
    def __init__(self, value, position, next=None):
        self.value = value
        self.position = position
        self.placed = False
        self.next = next


def mix_numbers(node_list, start):
    node_length = len(node_list)
    current_node = node(0, -1, start)
    while current_node.next:
        current_node = current_node.next
        local_index = node_list.index(current_node)
        target = (local_index + current_node.value) % (node_length - 1)
        node_list.insert(target, node_list.pop(local_index))


def main():
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = list(map(int, file.read().split("\n")))
    node_list = []
    current_node = None
    for index, item in enumerate(content[::-1]):
        if item == 0:
            zero_node = node(item, index, current_node)
            current_node = zero_node
            node_list.insert(0, zero_node)
            continue
        current_node = node(item * 811589153, index, current_node)
        node_list.insert(0, current_node)
    start = node_list[0]
    for i in range(10):
        mix_numbers(node_list, start)
        if test_case:
            print(f"mix {i + 1}")
            print([n.value for n in node_list])
    zero_index = node_list.index(zero_node)
    node_length = len(node_list)
    sum_nodes = 0
    for index in range(1, 4):
        print(
            f"{index}000th :{node_list[(zero_index + index * 1000) % node_length].value}"
        )
        sum_nodes += node_list[(zero_index + index * 1000) % node_length].value
    print(f"total value : {sum_nodes}")
    return sum_nodes


if __name__ == "__main__":
    main()
