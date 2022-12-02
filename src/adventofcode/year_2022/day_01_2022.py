from heapq import heappush, heappop
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 1, 1)
def part_one(input_data: List[str]):
    res = 0
    i = 0
    while i < len(input_data):
        amount = 0
        while i < len(input_data) and input_data[i] != "":
            amount += int(input_data[i])
            i += 1
        res = max(res, amount)
        i += 1
    answer = res
    if not answer:
        raise SolutionNotFoundException(2022, 1, 1)

    return answer


@solution_timer(2022, 1, 2)
def part_two(input_data: List[str]):
    answer = []
    i = 0
    while i < len(input_data):
        amount = 0
        while i < len(input_data) and input_data[i] != "":
            amount += int(input_data[i])
            i += 1
        heappush(answer, amount)
        if len(answer) > 3:
            heappop(answer)
        i += 1

    if not answer:
        raise SolutionNotFoundException(2022, 1, 2)

    return sum(answer)


if __name__ == '__main__':
    data = get_input_for_day(2022, 1)
    part_one(data)
    part_two(data)
