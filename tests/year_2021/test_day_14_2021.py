from collections import Counter

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_14_2021 import part_two, part_one

test_input = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C"
]


def test_part_one():
    answer = part_one(test_input)
    assert answer == 1588


def test_part_two():
    answer = part_two(test_input)
    assert answer == 2188189693529
