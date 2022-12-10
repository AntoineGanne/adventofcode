from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 10, 1)
def part_one(input_data: List[str]):
    signal = read_signal(input_data)

    answer = sum([signal[cycle - 1] * cycle for cycle in range(20, 221, 40)])

    if not answer:
        raise SolutionNotFoundException(2022, 10, 1)

    return answer


def read_signal(input_data):
    signal = [1]
    for line in input_data:
        signal.append(signal[-1])
        if line != 'noop':
            signal.append(signal[-1] + int(line.split(' ')[-1]))
    return signal


@solution_timer(2022, 10, 2)
def part_two(input_data: List[str]):
    signal = read_signal(input_data)
    crt =[[' '] * 40 for _ in range(6)]
    for cycle, sprite in enumerate(signal):
        row = cycle // 40
        col = cycle % 40
        if abs(sprite - col) <= 1:
            crt[row][col] = '#'
    print("***** Solution day 10,part 2,2022 ***** ")
    print('\n'.join([''.join(row) for row in crt]))
    answer = "RZEKEFKA"

    if not answer:
        raise SolutionNotFoundException(2022, 10, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 10)
    part_one(data)
    part_two(data)
