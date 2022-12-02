from adventofcode.util.input_helpers import get_test_input_for_day
from adventofcode.year_2021.day_16_2021 import part_two, part_one, parse


def test_convert_to_binary():
    # Code to convert hex to binary
    res = "{0:08b}".format(int("0F", 16))
    print(res)
    assert res == "00001111"


def test_part_one():
    i, version, value = parse("110100101111111000101000", 0)
    assert value == 2021
    assert version == 6

    i, version, value = parse("00111000000000000110111101000101001010010001001000000000", 0)
    assert value == 30

    i, version, value = parse("11101110000000001101010000001100100000100011000001100000", 0)
    assert value == 6
    # assert version == 31

    i, version, value = parse(
        "100010100000000001001010100000000001101010000000000000101111010001111000", 0)
    # assert value == 6
    assert version == 16

    i, version, value = parse(
        "1100000000000001010100000000000000000001011000010001010110100010111000001000000000101111000110000010001101000000",
        0)
    # assert value == 6
    assert version == 23

    i, version, value = parse(
        "101000000000000101101100100010000000000101100010000000010111110000110110100001101011000110001010001111010100011110000000",
        0)
    # assert value == 6
    assert version == 31


def test_part_two():
    answer = part_two(["C200B40A82"])
    assert answer == 3

    answer = part_two(["04005AC33890"])
    assert answer == 54

    answer = part_two(["880086C3E88112"])
    assert answer == 7

    answer = part_two(["CE00C43D881120"])
    assert answer == 9

    answer = part_two(["D8005AC2A8F0"])
    assert answer == 1

    answer = part_two(["F600BC2D8F"])
    assert answer == 0

    answer = part_two(["9C005AC2F8F0"])
    assert answer == 0

    answer = part_two(["9C0141080250320F1802104A08"])
    assert answer == 1
