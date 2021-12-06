from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def simulation_of_fishy_gloomy_fishes(input_data, nb_days):
    initial_state = list(map(int, input_data[0].split(',')))
    fishes = [0 for _ in range(9)]
    for fish in initial_state:
        fishes[fish] += 1
    # print(fishes)
    for day in range(nb_days):
        # print(f"day {day}")
        new_fishes_state = [0 for _ in range(9)]
        for i, nb_fishes in enumerate(fishes):
            if i == 0:
                new_fishes_state[8] = nb_fishes
                new_fishes_state[6] = nb_fishes
            if i <= 7:
                new_fishes_state[i] += fishes[i + 1]
        fishes = new_fishes_state.copy()
        # print(fishes)
    answer = sum(fishes)
    return answer


@solution_timer(2021, 6, 1)
def part_one(input_data: List[str], nb_days: int = 1):
    answer = simulation_of_fishy_gloomy_fishes(input_data, nb_days)

    if not answer:
        raise SolutionNotFoundException(2021, 6, 1)

    return answer


@solution_timer(2021, 6, 2)
def part_two(input_data: List[str], nb_days: int = 1):
    answer = simulation_of_fishy_gloomy_fishes(input_data, nb_days)

    if not answer:
        raise SolutionNotFoundException(2021, 6, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 6)
    part_one(data, 80)
    part_two(data,256)
