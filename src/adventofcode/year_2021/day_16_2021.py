import math
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

operations = [
    sum,
    math.prod,
    min,
    max,
    lambda vals: vals[0],
    lambda vals: 1 if vals[0] > vals[1] else 0,
    lambda vals: 1 if vals[0] < vals[1] else 0,
    lambda vals: 1 if vals[0] == vals[1] else 0,
]


def parse(input: str, istart: int) -> (int, int, int):
    i = istart
    version = int(input[i:i + 3], 2)
    id = int(input[i + 3:i + 6], 2)
    values = []
    i += 6
    if id == 4:
        str_value = ""
        while True:
            i += 5
            str_value += input[i - 4:i]
            if input[i - 5] == '0':
                break

        values.append(int(str_value, 2))
    else:
        if input[i] == '0':
            length = int(input[i + 1:i + 16], 2)
            i += 16
            iend = i + length
            while i < iend:
                i, vers_, val_ = parse(input, i)
                version += vers_
                values.append(val_)
        else:
            nb_packet = int(input[i + 1:i + 12], 2)
            i += 12
            for _ in range(nb_packet):
                i, vers_, val_ = parse(input, i)
                version += vers_
                values.append(val_)

    return i, version, operations[id](values)


@solution_timer(2021, 16, 1)
def part_one(input_data: List[str]):
    input: str = bin(int('1' + input_data[0], 16))[3:]
    i, version, value = parse(input, 0)
    answer = version
    if not answer:
        raise SolutionNotFoundException(2021, 16, 1)

    return answer


# hex2bin = {
#     '0': '0000',
#     '1': '0001',
#     '2': '0010',
#     '3': '0011',
#     '4': '0100',
#     '5': '0101',
#     '6': '0110',
#     '7': '0111',
#     '8': '1000',
#     '9': '1001',
#     'A': '1010',
#     'B': '1011',
#     'C': '1100',
#     'D': '1101',
#     'E': '1110',
#     'F': '1111',
# }

@solution_timer(2021, 16, 2)
def part_two(input_data: List[str]):
    input: str = bin(int('1' + input_data[0], 16))[3:]
    # input_ = "".join([hex2bin[c] for c in input_data[0]])
    i, version, value = parse(input, 0)
    answer = value

    # if not answer:
    #     raise SolutionNotFoundException(2021, 16, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 16)
    part_one(data)
    part_two(data)
