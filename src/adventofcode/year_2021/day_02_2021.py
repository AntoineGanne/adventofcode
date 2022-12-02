from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 2, 1)
def part_one(input_data: List[str]):
    depth = 0
    horizontal_position = 0
    for line in input_data:
        instruction, value_str = line.split(" ")
        value = int(value_str)
        if instruction == "forward":
            horizontal_position += value
        elif instruction == "down":
            depth += value
        elif instruction == "up":
            depth -= value
        else:
            raise Exception("error when parsing input")
    answer = depth * horizontal_position

    if not answer:
        raise SolutionNotFoundException(2021, 2, 1)

    return answer


@solution_timer(2021, 2, 2)
def part_two(input_data: List[str]):
    aim = 0
    depth = 0
    horizontal_position = 0
    for line in input_data:
        instruction, value_str = line.split(" ")
        value = int(value_str)
        if instruction == "forward":
            horizontal_position += value
            depth += aim * value
        elif instruction == "down":
            aim += value
        elif instruction == "up":
            aim -= value
        else:
            raise Exception("error when parsing input")
    answer = depth * horizontal_position

    if not answer:
        raise SolutionNotFoundException(2021, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 2)
    part_one(data)
    part_two(data)
