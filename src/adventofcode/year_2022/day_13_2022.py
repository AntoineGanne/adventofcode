from __future__ import annotations

import math
from functools import cmp_to_key
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


# -1: invalid , 0: can't say , 1: is_valid
def is_in_right_order(first: List[int] | int, second: List[int] | int) -> int:
    if type(first) != type(second):
        return is_in_right_order([first], second) if type(first) == int else is_in_right_order(first, [second])

    if type(first) == int:
        if first == second:
            return 0
        else:
            return 1 if first < second else -1
    else:
        n, m = len(first), len(second)
        if n == m == 0: return 0
        if n == 0: return 1
        if m == 0: return -1
        rest = is_in_right_order(first[0], second[0])
    return rest if rest != 0 else is_in_right_order(first[1:], second[1:])


@solution_timer(2022, 13, 1)
def part_one(input_data: List[str]):
    nb_pairs = len(input_data) // 3
    answer = 0
    for i in range(0, len(input_data), 3):
        first, second = eval(input_data[i]), eval(input_data[i + 1])
        index = (i // 3) + 1
        if is_in_right_order(first, second) == 1:
            answer += index

    if not answer:
        raise SolutionNotFoundException(2022, 13, 1)

    return answer


def compare(a, b):
    return -is_in_right_order(a, b)


@solution_timer(2022, 13, 2)
def part_two(input_data: List[str]):
    packets = []
    for packet in input_data:
        if packet == "": continue
        packets.append(eval(packet))
    packets.extend([[[2]], [[6]]])
    packets = sorted(packets, key=cmp_to_key(compare))
    answer = math.prod([packets.index([[2]]) + 1, packets.index([[6]]) + 1])

    if not answer:
        raise SolutionNotFoundException(2022, 13, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 13)
    part_one(data)
    part_two(data)
