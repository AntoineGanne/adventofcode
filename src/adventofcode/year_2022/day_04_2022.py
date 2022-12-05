import re
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 4, 1)
def part_one(input_data: List[str]):
    input_data = list(map(lambda l: [int(s) for s in l], [re.findall(r'\d+', s) for s in input_data]))

    def find_overlap(a1: int, b1: int, a2: int, b2: int):
        return (a1 <= a2 and b2 <= b1) or (a2 <= a1 and b1 <= b2)

    answer = len(list(filter(lambda l: find_overlap(*l), input_data)))

    if not answer:
        raise SolutionNotFoundException(2022, 4, 1)

    return answer


@solution_timer(2022, 4, 2)
def part_two(input_data: List[str]):
    input_data = list(map(lambda l: [int(s) for s in l], [re.findall(r'\d+', s) for s in input_data]))

    def find_overlap(a1: int, b1: int, a2: int, b2: int):
        return (a1 <= a2 <= b1 or a1 <= b2 <= b1) or (a2 <= a1 <= b2 or a2 <= b1 <= b2)

    answer = len(list(filter(lambda l: find_overlap(*l), input_data)))
    if not answer:
        raise SolutionNotFoundException(2022, 4, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 4)
    part_one(data)
    part_two(data)
