from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_15_2021 import part_two, part_one, get_neighbors


def test_neighbors():
    cave = [[0, 1, 0],
            [9, 0, 9],
            [4, 4, 4]]
    size = (3, 3)
    ns = get_neighbors(cave, size, 0, 0, True)
    assert ((0, 1), 1) in ns
    assert ((1, 0), 9) in ns

    ns = get_neighbors(cave, size, 1, 7, True)
    assert ((1, 6), 2) in ns
    assert ((0, 7), 3) in ns


def test_part_one():
    answer = part_one(get_input_for_day(2021, 15))
    assert True


def test_part_two():
    answer = part_two(get_input_for_day(2021, 15))
    assert True
