from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 3, 1)
def part_one(input_data: List[str]):
    weights = [0 for col in range(12)]
    counter_lines = 0
    gamma_rate = ['0' for col in range(12)]
    epsilon_rate = ['0' for col in range(12)]
    for line in input_data:
        for i, c in enumerate(line):
            if c == '0' or c == '1':
                weights[i] += int(c)
        counter_lines += 1

    for i in range(len(weights)):
        if weights[i] > (len(input_data) / 2):
            gamma_rate[i] = '1'
            epsilon_rate[i] = '0'
        else:
            gamma_rate[i] = '0'
            epsilon_rate[i] = '1'

    gamma_rate_str = "".join(gamma_rate)
    epsilon_rate_str = "".join(epsilon_rate)
    answer = int(gamma_rate_str, 2) * int(epsilon_rate_str, 2)

    if not answer:
        raise SolutionNotFoundException(2021, 3, 1)

    return answer


def recursion_part_2(bit_index: int, group_of_binary_numbers: List[str], most_common_bit_mode: bool):
    print(most_common_bit_mode, ", ", bit_index, ", ", group_of_binary_numbers)
    if group_of_binary_numbers is None or len(group_of_binary_numbers) == 0:
        return 0
    if len(group_of_binary_numbers) == 1:
        return group_of_binary_numbers[0]
    groups = [list(), list()]
    counter_of_ones = 0
    for binary_number in group_of_binary_numbers:
        bit = int(binary_number[bit_index])
        groups[bit].append(binary_number)
        counter_of_ones += bit

    bit_index += 1
    if counter_of_ones >= len(group_of_binary_numbers) / 2:
        most_common_bit = 1
        least_common_bit = 0
    else:
        most_common_bit = 0
        least_common_bit = 1

    if most_common_bit_mode:
        group = groups[most_common_bit]
    else:
        group = groups[least_common_bit]

    return recursion_part_2(bit_index, group, most_common_bit_mode)


@solution_timer(2021, 3, 2)
def part_two(input_data: List[str]):
    oxygen_generator_rating = recursion_part_2(0, input_data, True)
    CO2_scrubber_rating = recursion_part_2(0, input_data, False)
    print(oxygen_generator_rating, ";", CO2_scrubber_rating)
    print(int(oxygen_generator_rating, 2) ," ", int(CO2_scrubber_rating, 2))
    answer = int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)

    if not answer:
        raise SolutionNotFoundException(2021, 3, 2)

    return answer

@solution_timer(2021,3,3)
def part_two_with_binary_tree(input_data: List[str]):
    bin


test_data = {"00100",
             "11110",
             "10110",
             "10111",
             "10101",
             "01111",
             "00111",
             "11100",
             "10000",
             "11001",
             "00010",
             "01010"}

if __name__ == '__main__':
    data = get_input_for_day(2021, 3)
    part_one(data)
    part_two(data)
