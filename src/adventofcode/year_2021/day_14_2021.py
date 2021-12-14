from collections import Counter
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 14, 1)
def part_one(input_data: List[str]):
    answer = whole_aoc(input_data, 10)

    if not answer:
        raise SolutionNotFoundException(2021, 14, 1)

    return answer


def whole_aoc(input_data, duration: int):
    initial_polymer = input_data[0]
    pair_insertion_rules = dict()
    for rule in input_data[2:]:
        pair, new_element = rule.split(" -> ")
        new_elements = (pair[0] + new_element, new_element + pair[1], new_element)
        pair_insertion_rules[pair] = new_elements
    polymer = {e: 0 for e in pair_insertion_rules.keys()}
    letter_count = Counter(initial_polymer)
    for i in range(len(initial_polymer) - 1):
        pair = initial_polymer[i:i + 2]
        polymer[pair] += 1
    for step in range(1, duration + 1):
        new_polymer = polymer.copy()
        for pair, current_nb in polymer.items():
            new_elements = pair_insertion_rules[pair]
            new_polymer[pair] -= current_nb
            new_polymer[new_elements[0]] += current_nb
            new_polymer[new_elements[1]] += current_nb
            letter_count[new_elements[2]] += current_nb
        polymer = new_polymer
        # print("step ", step, " :", polymer)
    count = letter_count.most_common()
    most_common_letters = count[0]
    least_common_letter = count[-1]
    print(most_common_letters, least_common_letter)
    answer = most_common_letters[1] - least_common_letter[1]
    return answer


@solution_timer(2021, 14, 2)
def part_two(input_data: List[str]):
    answer = whole_aoc(input_data, 40)

    if not answer:
        raise SolutionNotFoundException(2021, 14, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 14)
    part_one(data)
    part_two(data)
