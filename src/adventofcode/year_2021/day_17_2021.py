import math
import re
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 17, 1)
def part_one(input_data: List[str]):
    target_area = re.match(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", input_data[0])
    target_area = list(map(int, target_area.groups()))

    max_y = -1
    for y_velocity in range(5, 200):
        simulated_y_velocity = y_velocity
        max_y_for_run = -1
        y = 0
        while y >= target_area[2]:
            y += simulated_y_velocity
            if simulated_y_velocity == 0:
                max_y_for_run = y
            simulated_y_velocity -= 1

            if target_area[2] <= y <= target_area[3] and max_y_for_run > max_y:
                max_y = max_y_for_run
                break
    answer = max_y

    if not answer:
        raise SolutionNotFoundException(2021, 17, 1)

    return answer


def is_probe_getting_in_target_zone(velocity: (int, int), target: (int, int, int, int)) -> bool:
    x, y = 0, 0
    vx,vy = velocity[0],velocity[1]
    while x <= target[1] and y >= target[2]:
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        vy -= 1
        if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
            return True
    return False


@solution_timer(2021, 17, 2)
def part_two(input_data: List[str]):
    target_area = re.match(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", input_data[0])
    target_area = list(map(int, target_area.groups()))
    nb_possible_vel = 0
    for vel_x in range(200):
        for vel_y in range(-120, 150):
            if is_probe_getting_in_target_zone((vel_x, vel_y), target_area):
                nb_possible_vel += 1
    answer = nb_possible_vel

    if not answer:
        raise SolutionNotFoundException(2021, 17, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 17)
    part_one(data)
    part_two(data)
