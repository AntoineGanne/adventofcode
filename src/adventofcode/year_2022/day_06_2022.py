from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 6, 1)
def part_one(input_data: List[str]):
    signal = input_data[0]
    len_marker = 4
    answer = find_marker(len_marker, signal)

    if not answer:
        raise SolutionNotFoundException(2022, 6, 1)

    return answer


def find_marker(len_marker, signal):
    chars = []
    answer = float('inf')
    for i, c in enumerate(signal):
        chars.append(c)
        if len(set(chars)) == len_marker:
            answer = i + 1
            break
        if len(chars) >= len_marker:
            chars.pop(0)
    return answer


@solution_timer(2022, 6, 2)
def part_two(input_data: List[str]):
    signal = input_data[0]
    len_marker = 14
    answer = find_marker(len_marker, signal)

    if not answer:
        raise SolutionNotFoundException(2022, 6, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 6)
    part_one(data)
    part_two(data)
