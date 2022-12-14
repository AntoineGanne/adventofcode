from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 14, 1)
def part_one(input_data: List[str]):
    obstacles = set()
    maxy = read_walls(input_data, obstacles)

    def sand_falling(x: int, y: int, y_abyss: int) -> bool:
        if y > y_abyss: return True
        if (x, y + 1) not in obstacles:
            return sand_falling(x, y + 1, y_abyss)
        elif (x - 1, y + 1) not in obstacles:
            return sand_falling(x - 1, y + 1, y_abyss)
        elif (x + 1, y + 1) not in obstacles:
            return sand_falling(x + 1, y + 1, y_abyss)
        else:
            obstacles.add((x, y))
            return False

    answer = 0
    while not sand_falling(500, 0, maxy):
        answer += 1

    if not answer:
        raise SolutionNotFoundException(2022, 14, 1)

    return answer


def read_walls(input_data, obstacles: set):
    walls = []
    for line in input_data:
        dots = line.split('->')
        dots = [[int(x), int(y)] for x, y in [dot.split(',') for dot in dots]]
        walls.append(dots)
    ys = [d[1] for dots in walls for d in dots]
    miny, maxy = min(ys), max(ys)

    for w in walls:
        last_dot = w[0]
        for next_dot in w[1:]:

            if next_dot[0] == last_dot[0]:
                dimension = 1
            else:
                dimension = 0
            direction = 1 if next_dot[dimension] > last_dot[dimension] else -1
            d = last_dot
            while d != next_dot:
                obstacles.add(tuple(d))
                d[dimension] += direction
            last_dot = next_dot
        obstacles.add(tuple(w[-1]))
    return maxy


@solution_timer(2022, 14, 2)
def part_two(input_data: List[str]):
    obstacles = set()
    maxy = read_walls(input_data, obstacles) + 2

    def sand_falling(x: int, y: int, y_abyss: int) -> (int, int):
        if y == y_abyss - 1:
            obstacles.add((x, y))
            return x, y
        if (x, y + 1) not in obstacles:
            return sand_falling(x, y + 1, y_abyss)
        elif (x - 1, y + 1) not in obstacles:
            return sand_falling(x - 1, y + 1, y_abyss)
        elif (x + 1, y + 1) not in obstacles:
            return sand_falling(x + 1, y + 1, y_abyss)
        else:
            obstacles.add((x, y))
            return x, y

    answer = 1
    while sand_falling(500, 0, maxy) != (500, 0):
        answer += 1

    if not answer:
        raise SolutionNotFoundException(2022, 14, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 14)
    part_one(data)
    part_two(data)
