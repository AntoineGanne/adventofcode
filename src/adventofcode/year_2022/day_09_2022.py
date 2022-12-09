from typing import List

from numpy.core.records import ndarray

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day
import numpy as np

directions = {
    'R': np.array([0, 1]),
    'L': np.array([0, -1]),
    'U': np.array([1, 0]),
    'D': np.array([-1, 0])
}


def calculate_new_knot_pos(head, tail) -> ndarray:
    ht_dist = head - tail
    if max(abs(min(ht_dist)), max(ht_dist)) <= 1:
        return tail
    if ht_dist[0] != 0:
        if ht_dist[0] > 0:
            ht_dist[0] = 1
        else:
            ht_dist[0] = -1
    if ht_dist[1] != 0:
        if ht_dist[1] > 0:
            ht_dist[1] = 1
        else:
            ht_dist[1] = -1
    tail += ht_dist
    return tail


@solution_timer(2022, 9, 1)
def part_one(input_data: List[str]):
    visited = {(0, 0)}

    tpos = np.array([0, 0])
    hpos = np.array([0, 0])
    for line in input_data:
        d, nb_steps = line.split()
        nb_steps = int(nb_steps)
        direction = directions[d]
        for _ in range(nb_steps):
            hpos += direction
            ht_dist = hpos - tpos
            if max(abs(min(ht_dist)), max(ht_dist)) <= 1:
                continue
            if ht_dist[0] != 0:
                if ht_dist[0] > 0:
                    ht_dist[0] = 1
                else:
                    ht_dist[0] = -1
            if ht_dist[1] != 0:
                if ht_dist[1] > 0:
                    ht_dist[1] = 1
                else:
                    ht_dist[1] = -1
            tpos += ht_dist
            visited.add((tpos[0], tpos[1]))

    answer = len(visited)

    if not answer:
        raise SolutionNotFoundException(2022, 9, 1)

    return answer


@solution_timer(2022, 9, 2)
def part_two(input_data: List[str]):
    rope_len=10
    rope = [np.array([0, 0]) for _ in range(rope_len)]
    visited = {(0, 0)}
    for line in input_data:
        d, nb_steps = line.split()
        nb_steps = int(nb_steps)
        direction = directions[d]
        for _ in range(nb_steps):
            rope[0] += direction
            for i in range(1,rope_len):
                rope[i] = calculate_new_knot_pos(rope[i - 1], rope[i])
            visited.add((rope[-1][0], rope[-1][1]))

    answer = len(visited)

    if not answer:
        raise SolutionNotFoundException(2022, 9, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 9)
    part_one(data)
    part_two(data)
