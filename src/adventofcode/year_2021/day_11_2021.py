from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


class dumbo_octopus:
    def __init__(self, coord: (int, int), energy_level: int, neighbors_coord: [(int, int)]):
        self.coord = coord
        self.energy_level = energy_level
        self.has_flashed = False
        self.neighbors_coord = neighbors_coord

    def reset_flash(self):
        self.has_flashed = False

    def increase_energy(self):
        if self.has_flashed:
            return
        self.energy_level += 1

    def will_flash(self):
        return self.energy_level > 9

    def flash(self):
        if self.energy_level <= 9:
            raise ValueError
        self.has_flashed = True
        self.energy_level = 0


def find_valid_neighbors(i: int, j: int, size: (int, int)):
    return [(x, y) for x in [i - 1, i, i + 1] for y in [j - 1, j, j + 1]
            if (x, y) != (i, j)
            and 0 <= x < size[0]
            and 0 <= y < size[1]]


def part_one_and_two(duration, input_data, is_part_1: bool = True):
    nb_flashes = 0
    octopodes = dict()
    step_of_first_synchronized_flash = -1
    size = (len(input_data), len(input_data[0]))
    for i, line in enumerate(input_data):
        for j, energy in enumerate(line):
            energy = int(energy)
            valid_coord_neighbors = find_valid_neighbors(i, j, size)
            new_octopus = dumbo_octopus((i, j), energy, valid_coord_neighbors)
            octopodes[(i, j)] = new_octopus
    for step in range(1,duration+1):
        nb_flash_this_step = 0
        flashing_octopodes = list()
        for octopus in octopodes.values():
            octopus.reset_flash()
            octopus.increase_energy()
            if octopus.will_flash():
                flashing_octopodes.append(octopus)

        while len(flashing_octopodes) > 0:
            octopus = flashing_octopodes.pop(0)
            nb_flashes += 1
            nb_flash_this_step += 1
            octopus.flash()
            for neighbor_coord in octopus.neighbors_coord:
                neighbor = octopodes[neighbor_coord]
                neighbor.increase_energy()
                if neighbor.will_flash() and neighbor not in flashing_octopodes:
                    flashing_octopodes.append(neighbor)

        print("step ", step, " -> number of flashes =", nb_flash_this_step)
        if nb_flash_this_step == size[0] * size[1] and step_of_first_synchronized_flash == -1:
            step_of_first_synchronized_flash = step
            if not is_part_1:
                return step_of_first_synchronized_flash

    if is_part_1:
        return nb_flashes
    else:
        return step_of_first_synchronized_flash


@solution_timer(2021, 11, 1)
def part_one(input_data: List[str], duration: int = 100):
    answer = part_one_and_two(duration, input_data)

    if not answer:
        raise SolutionNotFoundException(2021, 11, 1)

    return answer


@solution_timer(2021, 11, 2)
def part_two(input_data: List[str], duration: int = 1000):
    answer = part_one_and_two(duration, input_data, False)

    if not answer:
        raise SolutionNotFoundException(2021, 11, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 11)
    part_one(data)
    part_two(data)
