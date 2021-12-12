from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_12_2021 import part_two, part_one, can_be_added_to_path

input_1 = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end"
]


def test_random():
    assert ["ab", "ba", "fd"] == ["ab", "ba", "fd"]
    assert ["ab", "fd", "ba"] != ["ab", "ba", "fd"]
    path = ["a", "b", "C", "C"]
    assert can_be_added_to_path(path, "C")
    assert can_be_added_to_path(path, "b")
    path.append("b")
    assert not can_be_added_to_path(path, "b")


def test_part_one():
    answer = part_one(input_1)
    assert answer == 10


def test_part_two():
    answer = part_two(input_1)
    assert answer == 36
