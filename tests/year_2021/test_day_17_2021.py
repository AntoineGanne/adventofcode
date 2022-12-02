from adventofcode.util.input_helpers import get_test_input_for_day
from adventofcode.year_2021.day_17_2021 import part_two, part_one


def test_part_one():
    answer = part_one(get_test_input_for_day(2021, 17))
    assert answer == 45


def test_part_two():
    answer = part_two(get_test_input_for_day(2021, 17))
    assert answer == 112
