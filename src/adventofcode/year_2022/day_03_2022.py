from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 3, 1)
def part_one(input_data: List[str]):
    def find_item(l: str):
        m = len(l) // 2
        s1, s2 = set(l[:m]), set(l[m:])
        common_element: chr = s1.intersection(s2).pop()
        if common_element.isupper():
            return ord(common_element) - 38
        else:
            return ord(common_element) - 96

    answer = sum(map(find_item, input_data))

    if not answer:
        raise SolutionNotFoundException(2022, 3, 1)

    return answer


@solution_timer(2022, 3, 2)
def part_two(input_data: List[str]):
    def find_badge(group: List[str]):
        group = map(set, group)
        badge = set.intersection(*group).pop()
        if badge.isupper():
            return ord(badge) - 38
        else:
            return ord(badge) - 96

    answer = sum([find_badge(input_data[i:i + 3]) for i in range(0, len(input_data), 3)])

    if not answer:
        raise SolutionNotFoundException(2022, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 3)
    part_one(data)
    part_two(data)
