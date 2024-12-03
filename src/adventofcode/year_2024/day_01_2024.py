from collections import Counter
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2024, 1, 1)
def part_one(input_data: List[str]):
    l1, l2 = [], []
    for line in input_data:
        vals = list(map(int, line.split()))
        l1.append(vals[0])
        l2.append(vals[1])

    l1 = sorted(l1)
    l2 = sorted(l2)
    assert len(l1) == len(l2)
    answer = sum([abs(l1[i] - l2[i]) for i in range(len(l1))])

    if not answer:
        raise SolutionNotFoundException(2024, 1, 1)

    return answer


@solution_timer(2024, 1, 2)
def part_two(input_data: List[str]):
    l1, l2 = [], []
    for line in input_data:
        vals = list(map(int, line.split()))
        l1.append(vals[0])
        l2.append(vals[1])

    c = Counter(l2)

    answer = sum([l1[i]*c[l1[i]] for i in range(len(l1))])

    if not answer:
        raise SolutionNotFoundException(2024, 1, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2024, 1)
    part_one(data)
    part_two(data)
