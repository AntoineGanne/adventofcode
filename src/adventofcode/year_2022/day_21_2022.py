import re
from typing import List

import z3

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from z3 import Solver, Int, Abs


@solution_timer(2022, 21, 1)
def part_one(input_data: List[str]):
    monkeys = dict()
    referenced_by = dict()
    int_monkeys = []
    for line in input_data:
        monkey, op = line.split(": ")
        if re.match('\d+', op):
            monkeys[monkey] = int(op)
            int_monkeys.append(monkey)
        else:
            monkey1, op, monkey2 = op.split(' ')
            referenced_by[monkey1] = (monkey, 1)
            referenced_by[monkey2] = (monkey, 2)
            monkeys[monkey] = [op, None, None]
    print(monkeys)
    print(referenced_by)

    queue = int_monkeys
    while queue:
        monkey = queue.pop(0)
        state = monkeys[monkey]
        if type(state) == int:
            if monkey in referenced_by.keys():
                ref, place = referenced_by[monkey]
                if type(monkeys[ref])!=int:
                    monkeys[ref][place] = state
                    queue.append(ref)
        else:
            if state[1] is not None and state[2] is not None:
                val = None
                op = state[0]
                if op == '+':
                    val = state[1] + state[2]
                if op == '-':
                    val = state[1] - state[2]
                if op == '*':
                    val = state[1] * state[2]
                if op == '/':
                    val = state[1] // state[2]
                monkeys[monkey] = val
                if monkey in referenced_by.keys():
                    queue.append(referenced_by[monkey][0])

    answer = monkeys['root']

    if not answer:
        raise SolutionNotFoundException(2022, 21, 1)

    return answer


@solution_timer(2022, 21, 2)
def part_two(input_data: List[str]):
    humn = z3.Int()
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 21, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 21)
    part_one(data)
    part_two(data)
