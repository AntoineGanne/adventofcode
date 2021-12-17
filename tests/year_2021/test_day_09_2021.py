from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_09_2021 import part_two, part_one

input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]


def test_part_one():
    answer = part_one(input)
    assert answer == 15


def test_part_two():
    answer = part_two(get_input_for_day(2021, 9))
    assert False
