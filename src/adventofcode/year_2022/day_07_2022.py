from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2022, 7, 1)
def part_one(input_data: List[str]):
    dir_size = read_input(input_data)

    answer = sum(filter(lambda x: x < 100000, dir_size.values()))

    if not answer:
        raise SolutionNotFoundException(2022, 7, 1)

    return answer


def read_input(input_data):
    current_dir = "/"
    dir_size = {current_dir: 0}
    parent = {current_dir: "root"}
    for line in input_data[2:]:
        if line[0] == '$':
            command = line[2:4]
            if command == "cd":
                directory = line.split()[-1]
                if directory == "..":
                    current_dir = parent[current_dir]
                else:
                    current_dir = current_dir + "/" + directory
            else:
                continue
        else:
            line = line.split()
            if line[0] == "dir":
                child_dir = current_dir + "/" + line[1]
                parent[child_dir] = current_dir
            else:
                size = int(line[0])
                dir_size.setdefault(current_dir, 0)
                dir_size[current_dir] += size
                d = parent[current_dir]
                while d != "root":
                    dir_size.setdefault(d, 0)
                    dir_size[d] += size
                    d = parent[d]
    return dir_size


@solution_timer(2022, 7, 2)
def part_two(input_data: List[str]):
    dir_size = read_input(input_data)
    total_size = dir_size['/']
    size_to_delete = 30000000 - (70000000 - total_size)

    answer = min([s for s in dir_size.values() if s > size_to_delete])

    if not answer:
        raise SolutionNotFoundException(2022, 7, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 7)
    part_one(data)
    part_two(data)
