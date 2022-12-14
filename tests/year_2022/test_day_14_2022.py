from adventofcode.util.input_helpers import get_test_input_for_day
from adventofcode.year_2022.day_14_2022 import part_two, part_one


def test_part_one():
    assert [['.']*3 for _ in range(2)]== [['.', '.', '.'], ['.', '.', '.']]
    answer = part_one(get_test_input_for_day(2022, 14))
    assert answer ==24


def test_part_two():
    answer = part_two(get_test_input_for_day(2022, 14))
    assert answer ==93
