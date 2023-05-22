import re
from typing import List

from networkx import Graph, bfs_layers, bfs_tree

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import networkx as nx


@solution_timer(2022, 16, 1)
def part_one(input_data: List[str]):
    cave = Graph()
    flow_meters = []
    good_valves=set()

    N = 0
    node_id_map = dict()

    def gid(node):
        nonlocal N
        if node in node_id_map:
            return node_id_map[node]

        node_id_map[node] = N
        N += 1
        return node_id_map[node]


    for line in input_data:
        flow = int(re.findall(r'-?\d+', line).pop())

        valves = re.findall(r'[A-Z][A-Z]', line)
        source, destinations = valves[0], valves[1:]

        flow_meters

        if flow > 0 or source=='AA':
            good_valves.add(source)
            good_valves

        print(flow, source, destinations)



        cave.add_node(source)
        flow_meters[source] = flow
        cave.add_edges_from([(source, dest) for dest in destinations])

    all_pairs_shortest_path=nx.all_pairs_shortest_path(cave)

    # dp (current_node,time_left,subset_of_nodes_turned_on)
    dp = []

    bfs = bfs_tree(cave, "AA",depth_limit=30)
    print(bfs)

    def search(current_node:str, released:List[str],current_score:int):
        pass



    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 16, 1)

    return answer


@solution_timer(2022, 16, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2022, 16, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 16)
    part_one(data)
    part_two(data)
