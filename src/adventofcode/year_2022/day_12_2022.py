from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import networkx as nx


@solution_timer(2022, 12, 1)
def part_one(input_data: List[str]):
    n, m = len(input_data), len(input_data[0])
    end_index, g, start_index = create_graph_from_input(input_data, m, n)

    answer = nx.dijkstra_path_length(g, start_index, end_index)
    if not answer:
        raise SolutionNotFoundException(2022, 12, 1)

    return answer


def create_graph_from_input(input_data, m, n):
    start_index = list([(i, input_data[i].find("S")) for i in range(n)])
    start_index = list(filter(lambda v: v[1] != -1, start_index))[0]
    print(start_index)
    input_data[start_index[0]].replace('S', 'a')
    end_index = list([(i, input_data[i].find("E")) for i in range(n)])
    end_index = list(filter(lambda v: v[1] != -1, end_index))[0]
    print(end_index)
    input_data[end_index[0]].replace('E', 'z')
    g = nx.DiGraph()
    nodes = [(i, j) for i in range(n) for j in range(m)]
    g.add_nodes_from(nodes)
    for i in range(n):
        for j in range(m):
            c = input_data[i][j]
            ic = ord(c)
            if c == 'E': ic = ord('z') + 1
            if c == 'S': ic = ord('a')
            valid_edges = [((i, j), (i + oi, j + oj)) for oi, oj in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                           if 0 <= i + oi < n and 0 <= j + oj < m
                           and (
                                   (c == 'z') or
                                   (input_data[i + oi][j + oj] != 'E' and ord(input_data[i + oi][j + oj]) <= ic + 1)
                           )
                           ]
            g.add_edges_from(valid_edges)
    return end_index, g, start_index


@solution_timer(2022, 12, 2)
def part_two(input_data: List[str]):
    n, m = len(input_data), len(input_data[0])
    end_index, g, start_index = create_graph_from_input(input_data, m, n)
    g = nx.reverse(g)
    layers = dict(enumerate(nx.bfs_layers(g, end_index)))
    print(layers)

    answer = ...
    for length, layer in layers.items():
        elevations = [input_data[x][y] for x, y in layer]
        print(length, elevations)
        if 'a' in elevations:
            answer = length
            break

    if not answer:
        raise SolutionNotFoundException(2022, 12, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 12)
    part_one(data)
    part_two(data)
