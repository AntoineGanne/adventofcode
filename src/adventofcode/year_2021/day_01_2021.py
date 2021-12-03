from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 1, 1)
def part_one(input_data: List[str]):
    last_depth = 9999999
    depth_increase_counter = 0
    for line in open("D:/coding_perso/advent_of_code/aox/advent-of-code-2021/day 1/input.txt", "r"):
        depth = int(line)
        if depth > last_depth:
            depth_increase_counter += 1
        last_depth = depth

    answer = depth_increase_counter

    if not answer:
        raise SolutionNotFoundException(2021, 1, 1)

    return answer


@solution_timer(2021, 1, 2)
def part_two(input_data: List[str]):
    last_depth = 9999999
    depth_increase_counter = 0
    sliding_window = list()
    for i, line in enumerate(open("D:/coding_perso/advent_of_code/aox/advent-of-code-2021/day 1/input.txt", "r")):
        depth = int(line)
        sliding_window.append(depth)
        if i == 0 or i == 1:
            continue
        sum_depths = sum(sliding_window)
        if i < 10: print(str(i) + " sum:" + str(sum_depths))
        if sum_depths > last_depth:
            depth_increase_counter += 1
        last_depth = sum_depths
        sliding_window.pop(0)

    answer = depth_increase_counter

    if not answer:
        raise SolutionNotFoundException(2021, 1, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 1)
    part_one(data)
    part_two(data)
