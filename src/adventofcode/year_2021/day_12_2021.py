from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 12, 1)
def part_one(input_data: List[str]):
    connections, stack_paths = create_graph(input_data)
    nb_path = 0
    while len(stack_paths) > 0:
        current_path: List[str] = stack_paths.pop(0)
        current_cave = current_path[-1]
        connected_caves = connections[current_cave]
        neighbor_cave: str
        for neighbor_cave in connected_caves:
            if neighbor_cave == "end":
                nb_path += 1
                # print("".join(current_path), "end")
                continue
            if neighbor_cave.isupper() or \
                    (neighbor_cave.islower() and
                     neighbor_cave not in current_path):
                new_path = current_path.copy()
                new_path.append(neighbor_cave)
                stack_paths.append(new_path)

    answer = nb_path

    if not answer:
        raise SolutionNotFoundException(2021, 12, 1)

    return answer


def create_graph(input_data):
    connections = dict()
    for line in input_data:
        from_cave, to_cave = line.split('-')
        if from_cave not in connections.keys():
            connections[from_cave] = []
        if to_cave not in connections.keys():
            connections[to_cave] = []
        connections[from_cave].append(to_cave)
        connections[to_cave].append(from_cave)
    stack_paths: List[List[str]] = list()
    stack_paths.append(["start"])
    return connections, stack_paths


@solution_timer(2021, 12, 2)
def part_two(input_data: List[str]):
    connections, stack_paths = create_graph(input_data)
    nb_path = 0
    while len(stack_paths) > 0:
        current_path: List[str] = stack_paths.pop(0)
        current_cave = current_path[-1]
        connected_caves = connections[current_cave]
        neighbor_cave: str
        for neighbor_cave in connected_caves:
            if neighbor_cave == "end":
                nb_path += 1
                # print("".join(current_path), "end")
                continue
            if can_be_added_to_path(current_path, neighbor_cave):
                new_path = current_path.copy()
                new_path.append(neighbor_cave)
                stack_paths.append(new_path)

    answer = nb_path

    if not answer:
        raise SolutionNotFoundException(2021, 12, 2)

    return answer


def can_be_added_to_path(current_path, neighbor_cave):
    small_cave_duplicates = set([x for x in current_path if x.islower() and current_path.count(x) > 1])
    is_there_a_double_small_cave = len(small_cave_duplicates) >= 1
    if neighbor_cave == "start":
        return False
    return neighbor_cave.isupper() or \
           (neighbor_cave.islower() and
            (neighbor_cave not in current_path
             or not is_there_a_double_small_cave))


if __name__ == '__main__':
    data = get_input_for_day(2021, 12)
    part_one(data)
    part_two(data)
