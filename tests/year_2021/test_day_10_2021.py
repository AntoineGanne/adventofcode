from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_10_2021 import part_two, part_one

test_data = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]"
]


def test_part_one():
    answer = part_one(test_data)
    assert answer == 26397


def test_part_two():
    answer = part_two(test_data)
    assert answer == 288957
