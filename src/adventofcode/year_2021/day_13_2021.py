from functools import reduce
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day
import re


@solution_timer(2021, 13, 1)
def part_one(input_data: List[str]):
    dots = set()
    input_dots = list(filter(lambda string: not string.startswith("fold along") and ',' in string, input_data))
    input_folds = list(filter(lambda string: string.startswith("fold along"), input_data))

    for line in input_dots:
        x, y = map(int, line.split(','))
        if x > 655:
            x = (2 * 655) - x
        dots.add((x, y))

    answer = len(dots)

    if not answer:
        raise SolutionNotFoundException(2021, 13, 1)

    return answer


@solution_timer(2021, 13, 2)
def part_two(input_data: List[str]):
    dots = set()
    input_dots = list(filter(lambda string: not string.startswith("fold along") and ',' in string, input_data))
    input_folds = list(filter(lambda string: string.startswith("fold along"), input_data))

    folds = []
    for line in input_folds:
        # print("fold:", line)
        (direction, value) = re.findall(r"fold along ([xy])=(\d+)", line)[0]
        folds.append((direction, int(value)))

    for line in input_dots:
        x, y = map(int, line.split(','))
        for (direction, val) in folds:
            if direction == 'x' and x > val:
                x = 2 * val - x
            if direction == 'y' and y > val:
                y = 2 * val - y
        dots.add((x, y))

    # print(dots)

    size = reduce(lambda a, b: (max(a[0], b[0]), max(a[1], b[1])), dots)

    for j in range(size[1]*2):
        line = ""
        for i in range(size[0]*2):
            if (i,j) in dots:
                char = '#'
            else:
                char = '.'
            line += char
        print(line)

    answer = 'ZKAUCFUC' #input("number:")

    if not answer:
        raise SolutionNotFoundException(2021, 13, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 13)
    part_one(data)
    part_two(data)
