import functools
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 8, 1)
def part_one(input_data: List[str]):
    n, m = len(input_data), len(input_data[0])

    @functools.lru_cache(maxsize=n * m)
    def get_max_height(i: int, j: int, direction: (int, int)):
        if i == 0 or j == 0 or i == n - 1 or j == m - 1:
            return input_data[i][j]
        tree_to_check = (i + direction[0], j + direction[1])
        return max(input_data[i][j], get_max_height(tree_to_check[0], tree_to_check[1], direction))

    nb_visible = 2 * n + 2 * m - 4
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            tree = input_data[i][j]
            check = [((i + d[0], j + d[1]), d) for d in dirs]
            for dir_to_check in check:
                x, y = dir_to_check[0]
                if get_max_height(x, y, dir_to_check[1]) < tree:
                    nb_visible += 1
                    break

    answer = nb_visible

    if not answer:
        raise SolutionNotFoundException(2022, 8, 1)

    return answer


@solution_timer(2022, 8, 2)
def part_two(input_data: List[str]):
    n, m = len(input_data), len(input_data[0])

    @functools.lru_cache(maxsize=n * m)
    def get_number_of_tree_visible(i: int, j: int, direction: (int, int), tree_size: int):
        if i < 0 or j < 0 or i >= n or j >= m:
            return 1
        if i == 0 or j == 0 or i == n - 1 or j == m - 1:
            return 1
        current_tree = input_data[i][j]
        if int(current_tree) >= tree_size:
            return 1
        tree_to_check = (i + direction[0], j + direction[1])
        return 1 + get_number_of_tree_visible(tree_to_check[0], tree_to_check[1], direction, tree_size)

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = -1
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            tree = input_data[i][j]
            check = [((i + d[0], j + d[1]), d) for d in dirs]
            score = 1
            for dir_to_check in check:
                x, y = dir_to_check[0]
                score *= get_number_of_tree_visible(x, y, dir_to_check[1], int(tree))
            answer = max(answer, score)

    if not answer:
        raise SolutionNotFoundException(2022, 8, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 8)
    part_one(data)
    part_two(data)
