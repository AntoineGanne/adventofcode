from adventofcode.util.input_helpers import get_test_input_for_day
from adventofcode.year_2022.day_13_2022 import part_two, part_one


def test_part_one():
    assert eval("[9]") == [9]
    assert eval("[[9,8],7]") == [[9, 8], 7]
    assert list(zip([], [1])) == []
    assert list(zip([1], [])) == []
    answer = part_one(get_test_input_for_day(2022, 13))
    assert answer == 13


def test_part_two():
    answer = part_two(get_test_input_for_day(2022, 13))
    assert answer == 140
