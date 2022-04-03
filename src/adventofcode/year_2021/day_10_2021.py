import math
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day



characters = {'(': ')', '[': ']', '{': '}', '<': '>'}


@solution_timer(2021, 10, 1)
def part_one(input_data: List[str]):
    score = extract_incorrect_and_incomplete_infos(input_data)[0]

    answer = score

    if not answer:
        raise SolutionNotFoundException(2021, 10, 1)

    return answer


def extract_incorrect_and_incomplete_infos(input_data):
    score_of_characters = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    score = 0
    rest_for_incomplete_lines = []
    for line in input_data:
        last_opening_chars = []
        for i, char in enumerate(line):
            if char in characters.keys():
                last_opening_chars.append(char)
            elif char in characters.values():
                if char != characters[last_opening_chars.pop(-1)]:
                    score += score_of_characters[char]
                    break
            else:
                print("character not supported: ", char)

            if i == len(line) - 1 and len(last_opening_chars) != 0:
                rest_for_incomplete_lines.append(last_opening_chars)
    return score, rest_for_incomplete_lines


@solution_timer(2021, 10, 2)
def part_two(input_data: List[str]):
    score_of_characters = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    rest_to_complete = extract_incorrect_and_incomplete_infos(input_data)[1]
    all_scores = []
    for rest in rest_to_complete:
        score = 0
        for c in rest[::-1]:
            score *= 5
            matching_char = characters[c]
            score += score_of_characters[matching_char]
        all_scores.append(score)

    answer = sorted(all_scores)[math.floor(len(rest_to_complete)/2)]

    if not answer:
        raise SolutionNotFoundException(2021, 10, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 10)
    part_one(data)
    part_two(data)
