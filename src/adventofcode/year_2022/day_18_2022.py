import re
from typing import List

import numpy as np

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 18, 1)
def part_one(input_data: List[str]):
    print(input_data)
    cubes = set()
    for x, y, z in [line.split(',') for line in input_data]:
        print("x", x, "y", y, "z", z)
        cubes.add((int(x), int(y), int(z)))
    print(cubes)
    answer = 0
    dirs = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    dirs = [np.asarray(d) for d in dirs]
    for c in cubes:
        c = np.asarray(c)
        for d in dirs:
            neighbor = tuple(c + d)

            if neighbor not in cubes:
                answer += 1
        print(answer)

    if not answer:
        raise SolutionNotFoundException(2022, 18, 1)

    return answer


@solution_timer(2022, 18, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 18, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 18)
    part_one(data)
    part_two(data)
