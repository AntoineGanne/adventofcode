from adventofcode.year_2021.day_01_2021 import part_one,part_two

test_input = [
    "199",
    "200",
    "208",
    "210",
    "200",
    "207",
    "240",
    "269",
    "260",
    "263",
]


def test_sonar_sweep():
    assert part_one(test_input) == 7


def test_sonar_sweep_sliding_window():
    assert part_two(test_input) == 5


def test_sonar_sweep_sliding_window_reuse():
    assert part_two(test_input) == 5

