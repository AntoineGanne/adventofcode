import re
from typing import List

from z3 import Solver, Int, Abs

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 15, 1)
def part_one(input_data: List[str], row: int = 2000000):
    impossible_pos_on_row = set()
    nb_beacons_at_row = 0
    for line in input_data:
        temp = re.findall(r'-?\d+', line)
        x_sensor, y_sensor, x_beacon, y_beacon = list(map(int, temp))
        distance_x_beacon = abs(x_sensor - x_beacon)
        distance_y_beacon = abs(y_sensor - y_beacon)
        distance_beacon = distance_x_beacon + distance_y_beacon
        dist_sensor_from_row = abs(row - y_sensor)
        dist_left = distance_beacon - dist_sensor_from_row
        dx = 0
        while dist_sensor_from_row + dx <= distance_beacon:
            impossible_pos_on_row.add(x_sensor + dx)
            impossible_pos_on_row.add(x_sensor - dx)
            dx += 1

    answer = len(impossible_pos_on_row) - 1

    if not answer:
        raise SolutionNotFoundException(2022, 15, 1)

    return answer


@solution_timer(2022, 15, 2)
def part_two(input_data: List[str], max_coord: int = 4000000):
    s = Solver()
    x = Int('x')
    y = Int('y')
    s.add(x >= 0, x <= max_coord)
    s.add(y >= 0, y <= max_coord)
    for line in input_data:
        temp = re.findall(r'-?\d+', line)
        x_sensor, y_sensor, x_beacon, y_beacon = list(map(int, temp))
        d = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)
        s.add(Abs(x_sensor - x) + Abs(y_sensor - y) > d)
    s.check()
    m = s.model()
    answer = m[x].as_long() * 4000000 + m[y].as_long()

    if not answer:
        raise SolutionNotFoundException(2022, 15, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 15)
    part_one(data)
    part_two(data)
