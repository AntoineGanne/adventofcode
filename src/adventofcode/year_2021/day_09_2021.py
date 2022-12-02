import os
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 9, 1)
def part_one(input_data: List[str]):
    n1, n2 = len(input_data), len(input_data[0])
    z = [[0 for _ in range(n2)] for _ in range(n1)]
    for i, line in enumerate(input_data):
        for j, c in enumerate(line):
            z[i][j] = int(c)

    # z = np.array(z)
    # x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))
    #
    # # show height map in 3d
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(x, y, z)
    # plt.title('z as 3d height map')
    # plt.show()
    #
    # # show hight map in 2d
    # plt.figure()
    # plt.title('z as 2d heat map')
    # p = plt.imshow(z)
    # plt.colorbar(p)
    # plt.show()

    nb_local_minimum = 0
    local_minimum = dict()
    count_risk = 0
    for i in range(n1):
        for j in range(n2):
            c = z[i][j]
            neighbors = []
            if i != 0:
                neighbors.append(z[i - 1][j])
            if i != n1 - 1:
                neighbors.append(z[i + 1][j])
            if j != 0:
                neighbors.append(z[i][j - 1])
            if j != n2 - 1:
                neighbors.append(z[i][j + 1])

            lower_neighbors = list(filter(lambda cell: cell <= c, neighbors))
            if len(lower_neighbors) == 0:
                nb_local_minimum += 1
                local_minimum[(i, j)] = c
                count_risk += c + 1

    print(local_minimum)
    answer = count_risk
    # answer = sum(list(map(lambda f: f + 1, local_minimum.values())))
    if not answer:
        raise SolutionNotFoundException(2021, 9, 1)

    return answer


@solution_timer(2021, 9, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2021, 9, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 9)

    part_one(data)
    part_two(data)
