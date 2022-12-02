from adventofcode.util.input_helpers import get_test_input_for_day
from adventofcode.year_2022.day_02_2022 import part_two, part_one


def test_part_one():
    answer = part_one(get_test_input_for_day(2022, 2))
    assert answer is not None


def test_part_two():
    answer = part_two(get_test_input_for_day(2022, 2))
    assert answer is not None
