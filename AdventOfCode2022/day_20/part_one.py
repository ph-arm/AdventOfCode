"""Advent of Code 2022 - Day 20 - Part One"""

test_case = False


class node:
    def __init__(self, value, position, next=None):
        self.value = value
        self.position = position
        self.placed = False
        self.next = next


def mix_numbers(node_list):
    node_length = len(node_list)
    current_node = node(0, -1, node_list[0])
    while current_node.next:
        current_node = current_node.next
        local_index = node_list.index(current_node)
        if current_node.value == 0:
            continue
        if current_node.value > 0:
            cursor = local_index + current_node.value % (node_length - 1)
            if cursor > node_length:
                cursor = cursor % (node_length) + 1
        if current_node.value < 0:
            cursor = local_index - ((-current_node.value) % (node_length - 1))
            if cursor == 0:
                cursor = node_length
        node_list.pop(local_index)
        node_list.insert(cursor, current_node)
        if test_case:
            print([n.value for n in node_list])
            print("end swap cycle")


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
        current_node = node(item, index, current_node)
        node_list.insert(0, current_node)
    mix_numbers(node_list)
    zero_index = node_list.index(zero_node)
    node_length = len(node_list)
    print(f"1000th :{node_list[(zero_index + 1000) % node_length].value}")
    print(f"2000th :{node_list[(zero_index + 2000) % node_length].value}")
    print(f"3000th :{node_list[(zero_index + 3000) % node_length].value}")
    sum_nodes = (
        node_list[(zero_index + 1000) % node_length].value
        + node_list[(zero_index + 2000) % node_length].value
        + node_list[(zero_index + 3000) % node_length].value
    )
    print(f"total value : {sum_nodes}")
    return sum_nodes


# target test case : 1, 2, -3, 4, 0, 3, -2
"""Initial arrangement:
1, 2, -3, 3, -2, 0, 4

1 moves between 2 and -3:
2, 1, -3, 3, -2, 0, 4

2 moves between -3 and 3:
1, -3, 2, 3, -2, 0, 4

-3 moves between -2 and 0:
1, 2, 3, -2, -3, 0, 4

3 moves between 0 and 4:
1, 2, -2, -3, 0, 3, 4

-2 moves between 4 and 1:
1, 2, -3, 0, 3, 4, -2

0 does not move:
1, 2, -3, 0, 3, 4, -2

4 moves between -3 and 0:
1, 2, -3, 4, 0, 3, -2"""


if __name__ == "__main__":
    main()


"""
0 -2 0
--> -2 0 0
--> 0 -2 0
reality check :
pop(1) --> 0 0 // len 2
--> value 1-2 --> -1



0 -3 0 0
--> -3 0 0 0
-->  0 0 -3 0
-->  0 -3 0 0
reality check :
pop(1) --> 0 0 0 // len 3
--> value 1-3 --> -2

//(n-1)

0 3 0 0
-->  0 0 3 0
-->  0 0 0 3
-->  0 3 0 0
reality check :
pop(1) --> 0 0 0 // len 3
--> value 1+3 --> 4 4%3 ==>1

//(n-1)

0 0 3 0 0
-->  0 0 0 3 0
-->  0 0 0 0 3
-->  0 3 0 0 0
reality check :
pop(1) --> 0 0 0 0// len 3
--> value 2+3 --> 5 5%5 ==>1


"""
