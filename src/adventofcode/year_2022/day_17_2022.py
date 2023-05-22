from typing import List, Tuple

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 2),
     (0, 1), (1, 1), (2, 1),
     (1, 0)
     ],
    [(2, 2),
     (2, 1),
     (0, 0), (1, 0), (2, 0),
     ],
    [(0, 0),
     (0, 1),
     (0, 2),
     (0, 3)],
    [(0, 0), (1, 0),
     (0, 1), (1, 1)]
]

shapes_heights = [1, 3, 3, 4, 2]


@solution_timer(2022, 17, 1)
def part_one(input_data: List[str]):
    id_rock = 0
    n = len(shapes)
    i_jet = 0
    jet_streams = [1 if c == '>' else -1 for c in input_data[0]]
    m = len(jet_streams)
    obstacles = set()
    highest_rock_y = 0

    def pos_is_invalid(pos: (int, int)) -> bool:
        return not 0 <= pos[0] < 7 or pos[1] <= 0 or pos in obstacles

    def is_down_movement_possible(rock: List[Tuple[int, int]]) -> bool:
        new_pos = [(r[0], r[1] - 1) for r in rock]
        return not any(filter(pos_is_invalid, new_pos))

    def is_side_movement_possible(rock: List[Tuple[int, int]], direction: int) -> bool:
        new_pos = [(r[0] + direction, r[1]) for r in rock]
        return not any(filter(pos_is_invalid, new_pos))

    def print_obstacles():
        for i in range(1, highest_rock_y + 1)[::-1]:
            print("".join(["█" if (j, i) in obstacles else "." for j in range(7)]))

    while id_rock < 2022:
        rock = shapes[id_rock % n]
        pr = (2, highest_rock_y + 4)
        rock = [(r[0] + pr[0], r[1] + pr[1]) for r in rock]
        is_falling = True
        while is_falling:
            jet_dir = jet_streams[i_jet]
            # print(id_rock, "jet", jet_dir)
            if is_side_movement_possible(rock, jet_dir):
                rock = [(r[0] + jet_dir, r[1]) for r in rock]
            if is_down_movement_possible(rock):
                rock = [(r[0], r[1] - 1) for r in rock]
            else:
                is_falling = False
                for p in rock:
                    highest_rock_y = max(highest_rock_y, p[1])
                    obstacles.add(p)

            i_jet = (i_jet + 1) % m
        # print(id_rock, "high", highest_rock_y)
        # print(obstacles)
        # if id_rock%1000==0:
        #     print_obstacles()
        id_rock += 1

    answer = highest_rock_y

    if not answer:
        raise SolutionNotFoundException(2022, 17, 1)

    return answer


@solution_timer(2022, 17, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 17, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 17)
    part_one(data)
    part_two(data)
