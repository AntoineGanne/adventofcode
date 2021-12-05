from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_05_2021 import part_two, part_one

test_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2"
]


def test_part_one():
    answer = part_one(test_input)
    assert answer == 5


def test_part_two():
    answer = part_two(get_input_for_day(2021, 5))
    assert False
