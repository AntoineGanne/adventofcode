from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_11_2021 import part_two, part_one, find_valid_neighbors

input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526"
]


def test_neighbors():
    neighbors = find_valid_neighbors(0, 0, (5, 5))
    for (i, j) in [(0, 1), (1, 0), (1, 1)]:
        assert (i, j) in neighbors

    neighbors = find_valid_neighbors(2, 2, (5, 5))
    assert (1, 1) in neighbors
    assert (2, 2) not in neighbors
    assert (2, 1) in neighbors


def test_part_one():
    answer = part_one(input)
    assert answer == 1656


def test_part_two():
    answer = part_two(input)
    assert answer == 195
