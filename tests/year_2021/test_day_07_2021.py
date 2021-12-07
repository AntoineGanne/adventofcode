from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_07_2021 import part_two, part_one, calculate_fuel_consumption

test_input = ["16, 1, 2, 0, 4, 2, 7, 1, 2, 14"]
test_input_splitted = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_calcul():
    assert calculate_fuel_consumption(2, test_input_splitted, False) == 37
    assert calculate_fuel_consumption(1, test_input_splitted, False) == 41
    assert calculate_fuel_consumption(3, test_input_splitted, False) == 39
    assert calculate_fuel_consumption(10, test_input_splitted, False) == 71
    assert calculate_fuel_consumption(5, test_input_splitted, True) == 168
    assert calculate_fuel_consumption(2, test_input_splitted, True) == 206


def test_part_one():
    answer = part_one(test_input)
    assert answer == 37


def test_part_two():
    answer = part_two(test_input)
    assert answer == 168
