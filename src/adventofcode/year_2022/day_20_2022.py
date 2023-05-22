from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def move_node(self):
        abs_val = abs(self.val)
        node = self
        for _ in range(abs_val):
            if self.val > 0:
                node = node.right
            else:
                node = node.left

        self.left.right = self.right

        node.right, self.right = self, node.right

    def print(self):
        list = [str(self.val)]
        node = self.right
        while node and node != self:
            list.append(str(node.val))
            node = node.right
        print(",".join(list))


@solution_timer(2022, 20, 1)
def part_one(input_data: List[str]):
    input_data = list(map(int, input_data))
    left = Node(input_data[0])
    linked_list = left
    original_order = [left]
    for val in input_data[1:]:
        print(val)
        new_node = Node(val, left=left)
        left.right = new_node
        original_order.append(new_node)
        left = new_node
    linked_list.left = original_order[-1]

    for node in original_order:
        node.move_node()
        print(node)
        node.print()

    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 20, 1)

    return answer


@solution_timer(2022, 20, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 20, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 20)
    part_one(data)
    part_two(data)
