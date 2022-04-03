from math import floor
from typing import List, Tuple

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, (int, int)]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: (int, int), priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> (int, int):
        return heapq.heappop(self.elements)[1]


def get_neighbors(cave: List[List[int]], size: (int, int), i: int, j: int, mode_part_2: bool = False):
    og_size = size
    if mode_part_2:
        size = (size[0] * 5, size[1] * 5)
    assert 0 <= i < size[0]
    assert 0 <= j < size[1]
    neighbor_indexes = []
    if i > 0:
        neighbor_indexes.append((i - 1, j))
    if i < size[0] - 1:
        neighbor_indexes.append((i + 1, j))
    if j > 0:
        neighbor_indexes.append((i, j - 1))
    if j < size[1] - 1:
        neighbor_indexes.append((i, j + 1))

    if mode_part_2:
        result = []
        for i, j in neighbor_indexes:
            risk_score = cave[i % og_size[0]][j % og_size[1]]
            offset = floor(i / og_size[0]) + floor(j / og_size[1])
            risk_score = (risk_score + offset) % 9
            if risk_score == 0:
                risk_score = 9
            result.append(((i, j), risk_score))
        return result
    else:
        return [(e, cave[e[0]][e[1]]) for e in neighbor_indexes]


@solution_timer(2021, 15, 1)
def part_one(input_data: List[str]):
    size = (len(input_data[0]), len(input_data))
    cave = [[int(input_data[i][j]) for j in range(size[0])] for i in range(size[1])]
    start = (0, 0)
    cost_so_far = dict()
    cost_so_far[(0, 0)] = 0
    came_from = dict()
    came_from[(0, 0)] = None
    frontier = PriorityQueue()
    frontier.put(start, 0)
    while not frontier.empty():
        current_node = frontier.get()
        if current_node[0] == (size[0] - 1, size[1] - 1):
            break

        neighbors = get_neighbors(cave, size, current_node[0], current_node[1])
        for n in neighbors:
            pos_n = n[0]
            new_cost = cost_so_far[current_node] + n[1]
            if pos_n not in cost_so_far.keys() or new_cost < cost_so_far[pos_n]:
                cost_so_far[pos_n] = new_cost
                priority = new_cost + (size[0] - pos_n[0]) + (size[1] - pos_n[1])
                frontier.put(pos_n, priority)

    answer = cost_so_far[(size[0] - 1, size[1] - 1)]

    if not answer:
        raise SolutionNotFoundException(2021, 15, 1)

    return answer


@solution_timer(2021, 15, 2)
def part_two(input_data: List[str]):
    size = (len(input_data[0]), len(input_data))
    cave = [[int(input_data[i][j]) for j in range(size[0])] for i in range(size[1])]
    start = (0, 0)
    cost_so_far = dict()
    cost_so_far[(0, 0)] = 0
    came_from = dict()
    came_from[(0, 0)] = None
    frontier = PriorityQueue()
    frontier.put(start, 0)
    while not frontier.empty():
        current_node = frontier.get()
        if current_node[0] == (size[0] * 5 - 1, size[1] * 5 - 1):
            break

        neighbors = get_neighbors(cave, size, current_node[0], current_node[1], True)
        for n in neighbors:
            pos_n = n[0]
            new_cost = cost_so_far[current_node] + n[1]
            if pos_n not in cost_so_far.keys() or new_cost < cost_so_far[pos_n]:
                cost_so_far[pos_n] = new_cost
                priority = new_cost + (size[0] - pos_n[0]) + (size[1] - pos_n[1])
                frontier.put(pos_n, priority)

    answer = cost_so_far[(size[0] * 5 - 1, size[1] * 5 - 1)]

    if not answer:
        raise SolutionNotFoundException(2021, 15, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 15)
    part_one(data)
    part_two(data)
