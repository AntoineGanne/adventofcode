from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 2, 1)
def part_one(input_data: List[str]):
    vals = {'X': 1, 'Y': 2, 'Z': 3}
    beats = {'AY': 6, 'BZ': 6, 'CX': 6, 'AX': 3, 'BY': 3, 'CZ': 3}
    beats.setdefault(0)
    input_data = list(map(str.split, input_data))
    print(input_data)
    print(list(map(lambda m: vals[m[1]] + beats.get(m[0] + m[1], 0), input_data)))
    answer = sum(map(lambda m: vals[m[1]] + beats.get(m[0] + m[1], 0), input_data))

    if not answer:
        raise SolutionNotFoundException(2022, 2, 1)

    return answer


@solution_timer(2022, 2, 2)
def part_two(input_data: List[str]):
    vals = {'X': 0, 'Y': 1, 'Z': 2}
    link = {'A': [3, 1, 2],
            'B': [1, 2, 3],
            'C': [2, 3, 1]}

    input_data = list(map(str.split, input_data))
    print(input_data)
    print(list(map(lambda m: vals[m[1]] * 3 + link[m[0]][vals[m[1]]], input_data)))
    answer = sum(map(lambda m: vals[m[1]] * 3 + link[m[0]][vals[m[1]]], input_data))

    if not answer:
        raise SolutionNotFoundException(2022, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 2)
    part_one(data)
    part_two(data)
