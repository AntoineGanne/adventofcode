import re
from collections import Counter
from itertools import permutations
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 8, 1)
def part_one(input_data: List[str]):
    number_of_1_4_7_8 = 0
    for line in input_data:
        output_values = re.findall(r"(\w+)", line.split('|')[1])
        output_values = list(filter(lambda v: len(v) == 2 or len(v) == 3 or len(v) == 4 or len(v) == 7, output_values))
        number_of_1_4_7_8 += len(output_values)

    answer = number_of_1_4_7_8

    if not answer:
        raise SolutionNotFoundException(2021, 8, 1)

    return answer


@solution_timer(2021, 8, 2)
def part_two(input_data: List[str]):
    one = "0010010"
    two = "1011101"
    for line in input_data:
        separated_line = line.split('|')
        signal_patterns, output_patterns = re.findall(r"(\w+)", separated_line[0]), re.findall(r"(\w+)",
                                                                                               separated_line[1])
        all_patterns = signal_patterns + output_patterns
        all_patterns = list(map(lambda s: "".join(sorted(s)), all_patterns))
        all_patterns = list(dict.fromkeys(all_patterns))  # remove duplicates
        segments = [{'a', 'b', 'c', 'd', 'e', 'f', 'g'} for _ in range(7)]

        lengths_of_patterns = list(map(lambda s: len(s), all_patterns))

        # one
        if 2 in lengths_of_patterns:
            index = lengths_of_patterns.index(2)
            pattern = all_patterns[index]
            segments = update_segments({2, 5}, pattern, segments)

        # four
        if 4 in lengths_of_patterns:
            index = lengths_of_patterns.index(4)
            pattern = all_patterns[index]
            segments = update_segments({1, 2, 3, 5}, pattern, segments)

        # seven
        if 3 in lengths_of_patterns:
            index = lengths_of_patterns.index(3)
            pattern = all_patterns[index]
            segments = update_segments({0, 2, 5}, pattern, segments)

        # eight
        if 7 in lengths_of_patterns:
            pass

        print(segments)

        # start backtracking ? 🙈

        for i in range(7):

        all_possible_solutions = permutations(segments)

        solution = []
        taken_segments = {}

    answer = ...

    if not answer:
        raise SolutionNotFoundException(2021, 8, 2)

    return answer


def update_segments(indexes, pattern, segments):
    for index in indexes:
        segments[index] = {c for c in list(set(pattern) & set(segments[index]))}

    return segments


def check_if_solution_is_valid(segments: List[chr], patterns: List[str]):
    for p in patterns:
        output = output_number_under_solution(segments, p)
        if p == 'x':
            return False
    return True


valid_outputs = {
    "1110111": '0',
    "0010010": '1',
    "1011101": '2',
    "1011011": '3',
    "0111010": '4',
    "1101011": '5',
    "1101111": '6',
    "1010010": '7',
    "1111111": '8',
    "1111011": '9'
}


def output_number_under_solution(segments: List[chr], pattern: str):
    out = ["0" for _ in range(len(segments))]
    for i, seg in enumerate(segments):
        if seg in pattern:
            out[i] = "1"
    output = "".join(out)
    if output in valid_outputs.keys():
        return valid_outputs[output]
    else:
        return 'x'


if __name__ == '__main__':
    data = get_input_for_day(2021, 8)
    part_one(data)
    part_two(data)
