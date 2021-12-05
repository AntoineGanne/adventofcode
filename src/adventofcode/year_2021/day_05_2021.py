import os
import re
from functools import reduce
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 5, 1)
def part_one(input_data: List[str]):
    dots_of_lines = dict()
    for line in input_data:
        matches = re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", line)
        matches = matches[0]
        matches = list(map(int, matches))
        couple = ((matches[0], matches[1]), (matches[2], matches[3]))
        x1 = couple[0]
        x2 = couple[1]

        draw_line_when_row_or_column(dots_of_lines, x1, x2)
        print_board(dots_of_lines)

    dots_of_lines = list(filter(lambda d: d != 1, list(dots_of_lines.values())))

    answer = len(dots_of_lines)

    if not answer:
        raise SolutionNotFoundException(2021, 5, 1)

    return answer


def draw_line_when_row_or_column(dots_of_lines, x1, x2):
    positions = []
    if x1[0] == x2[0]:
        if x1[1] < x2[1]:
            a, b = x1[1], x2[1]
        else:
            a, b = x2[1], x1[1]
        for i in range(a, b + 1):
            positions.append((x1[0], i))
    if x1[1] == x2[1]:
        if x1[0] < x2[0]:
            a, b = x1[0], x2[0]
        else:
            a, b = x2[0], x1[0]
        positions = []
        for i in range(a, b + 1):
            positions.append((i, x1[1]))
    update_dict(dots_of_lines, positions)


def print_board(dots_of_lines):
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--**-*-*")
    for i in range(10):
        line = ""
        for j in range(10):
            if (j, i) in dots_of_lines:
                number = dots_of_lines[(j, i)]
                if number > 9:
                    number = '#'
                else:
                    number = str(number)
            else:
                number = "."
            line += number
        print(line)


def update_dict(dots_of_lines, positions):
    for p in positions:
        if p in dots_of_lines.keys():
            dots_of_lines[p] += 1
        else:
            dots_of_lines[p] = 1


@solution_timer(2021, 5, 2)
def part_two(input_data: List[str]):
    dots_of_lines = dict()
    for line in input_data:
        matches = re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", line)
        matches = matches[0]
        matches = list(map(int, matches))
        couple = ((matches[0], matches[1]), (matches[2], matches[3]))
        x1 = couple[0]
        x2 = couple[1]

        if x1[0] < x2[0]:
            inc1 = 1
        elif x1[0] == x2[0]:
            inc1 = 0
        else:
            inc1 = -1

        if x1[1] < x2[1]:
            inc2 = 1
        elif x1[1] == x2[1]:
            inc2 = 0
        else:
            inc2 = -1

        positions = [x1]
        i, j = x1[0], x1[1]
        while (i, j) != x2:
            i += inc1
            j += inc2
            positions.append((i, j))

        update_dict(dots_of_lines, positions)
        print_board(dots_of_lines)

    dots_of_lines = list(filter(lambda d: d != 1, list(dots_of_lines.values())))

    answer = len(dots_of_lines)

    if not answer:
        raise SolutionNotFoundException(2021, 5, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 5)

    part_one(data)
    part_two(data)
