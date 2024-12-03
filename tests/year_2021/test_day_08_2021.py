from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_08_2021 import part_two, part_one, output_number_under_solution

test_input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]


def test_part_one():
    answer = part_one(test_input)
    assert answer == 26


def test_part_two():
    answer = part_two(test_input)
    assert True


def test_output_number_under_solution():
    segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    pattern1 = "cf"
    assert output_number_under_solution(segments, pattern1) == '1'

    pattern3 = "acdfg"
    assert output_number_under_solution(segments, pattern3) == '3'

    invalid_pattern = "bcfe"
    assert output_number_under_solution(segments, invalid_pattern) == 'x'
