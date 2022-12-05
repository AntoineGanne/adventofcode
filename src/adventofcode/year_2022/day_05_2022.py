import re
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 5, 1)
def part_one(input_data: List[str]):
    split = input_data.index("")
    stacks = read_initial_state(input_data, split)
    for l in input_data[split+1:]:
        instructions = list(map(int, re.findall(r'\d+', l)))
        nb, from_, to_ = instructions[0], instructions[1] - 1, instructions[2] - 1
        for _ in range(nb):
            c = stacks[from_].pop()
            stacks[to_].append(c)

    answer = "".join([r[-1] for r in stacks])

    if not answer:
        raise SolutionNotFoundException(2022, 5, 1)

    return answer


def read_initial_state(input_data, split):
    nb_stacks = int(input_data[split - 1][-1])
    stacks = [[] for _ in range(nb_stacks)]
    for l in input_data[:split - 1]:
        index = 1
        for i in range(nb_stacks):
            if l[index] != ' ':
                stacks[i].append(l[index])
            index += 4
    stacks = list(map(list, map(reversed, stacks)))
    return stacks


@solution_timer(2022, 5, 2)
def part_two(input_data: List[str]):
    split = input_data.index("")
    stacks = read_initial_state(input_data,split)
    for l in input_data[split+1:]:
        instructions = list(map(int, re.findall(r'\d+', l)))
        nb, from_, to_ = instructions[0], instructions[1] - 1, instructions[2] - 1
        temp = []
        for _ in range(nb):
            c = stacks[from_].pop()
            temp.append(c)
        stacks[to_].extend(temp[::-1])

    answer = "".join([r[-1] for r in stacks])

    if not answer:
        raise SolutionNotFoundException(2022, 5, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 5)
    part_one(data)
    part_two(data)
