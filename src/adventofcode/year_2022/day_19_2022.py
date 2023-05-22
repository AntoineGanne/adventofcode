import re
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day, get_test_input_for_day


@solution_timer(2022, 19, 1)
def part_one(input_data: List[str]):
    def simulate(blueprint: List[int], robots: List[int], ressources: List[int], time_left: int) -> int:
        assert len(robots) == len(ressources) == 4
        assert len(blueprint) == 6
        ressources = ressources.copy()
        for i, r in enumerate(robots):
            ressources[i] += r

        print("time", time_left)
        print("ressources", ressources, robots)

        if time_left == 0:
            return ressources[-1]
        else:
            best_result = 0

            if ressources[0] >= blueprint[4] and ressources[2] >= blueprint[5]:
                print("geode robot")
                ressources[0] -= blueprint[4]
                ressources[2] -= blueprint[5]
                robots[3] += 1
                return simulate(blueprint, robots, ressources, time_left - 1)

            if ressources[0] >= blueprint[0]:
                print("ore robot")
                ressources[0] -= blueprint[0]
                robots[0] += 1
                best_result = max(best_result, simulate(blueprint, robots, ressources, time_left - 1))
                ressources[0] += blueprint[0]
                robots[0] -= 1

            if ressources[0] >= blueprint[1]:
                print("clay robot")
                ressources[0] -= blueprint[1]
                robots[1] += 1
                best_result = max(best_result, simulate(blueprint, robots, ressources, time_left - 1))
                ressources[0] += blueprint[1]
                robots[1] -= 1

            if ressources[0] >= blueprint[2] and ressources[1] >= blueprint[3]:
                print("obsidian robot")
                ressources[0] -= blueprint[2]
                ressources[1] -= blueprint[3]
                robots[2] += 1
                best_result = max(best_result, simulate(blueprint, robots, ressources, time_left - 1))
                ressources[0] += blueprint[2]
                ressources[1] += blueprint[3]
                robots[2] -= 1

            best_result = max(best_result, simulate(blueprint, robots, ressources, time_left - 1))

            return best_result

    answer = 0
    for line in input_data:
        blueprint = list(map(int, re.findall(r'\d+', line)))
        max_number_of_geodes = simulate(blueprint[1:], [1, 0, 0, 0], [0, 0, 0, 0], 24)
        quality = max_number_of_geodes * blueprint[0]
        print(blueprint[0], "nb geodes", max_number_of_geodes, "quality", quality)
        answer += quality

    if not answer:
        raise SolutionNotFoundException(2022, 19, 1)

    return answer


@solution_timer(2022, 19, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 19, 2)

    return answer


if __name__ == '__main__':
    # data = get_input_for_day(2022, 19)
    data = get_test_input_for_day(2022, 19)
    part_one(data)
    part_two(data)
