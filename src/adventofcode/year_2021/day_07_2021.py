import math
import statistics
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def calculate_fuel_consumption(position: int, submarine_crabs: List[int], mode_part_two: bool):
    if mode_part_two:
        fuel = 0
        for crab in submarine_crabs:
            N = abs(crab - position)
            fuel += math.floor((N * (N + 1)) / 2)
        return fuel
    else:
        return sum(abs(crab - position) for crab in submarine_crabs)


@solution_timer(2021, 7, 1)
def part_one(input_data: List[str]):
    sub_crabs = list(map(int, input_data[0].split(',')))
    median = statistics.median(sub_crabs)

    answer = calculate_fuel_consumption(median, sub_crabs, False)

    if not answer:
        raise SolutionNotFoundException(2021, 7, 1)

    return answer


@solution_timer(2021, 7, 2)
def part_two(input_data: List[str]):
    sub_crabs = list(map(int, input_data[0].split(',')))
    mean = math.floor(statistics.mean(sub_crabs))
    answer = calculate_fuel_consumption(math.floor(mean), sub_crabs, True)

    if not answer:
        raise SolutionNotFoundException(2021, 7, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 7)
    part_one(data)
    part_two(data)
