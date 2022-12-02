from adventofcode.util.input_helpers import get_test_input_for_day
from adventofcode.year_2019.day_01_2019 import part_two, part_one


def test_part_one():
    answer = part_one(get_test_input_for_day(2019, 1))
    assert answer is not None


def test_part_two():
    answer = part_two(get_test_input_for_day(2019, 1))
    assert answer is not None
