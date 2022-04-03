import dataclasses
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day, get_test_input_for_day


# @dataclasses.dataclass
# class Pixel:
#         x:int
#         y:int


def get_enhanced_pixel(p: List[int, int], image: dict, enhancer: List[int], board_size: List[List[int, int], List[int, int]],
                       infinity_bit: int) -> int:
    ns = [(i, j) for j in range(p[1] - 1, p[1] + 2) for i in range(p[0] - 1, p[0] + 2)]
    ns2 = []
    for pos in ns:
        if board_size[0][0] <= pos[0] <= board_size[0][1] and board_size[1][0] <= pos[1] <= board_size[1][1]:
            ns2.append(1 if pos in image.keys() else 0)
        else:
            ns2.append(infinity_bit)

    index = int("".join(map(str, ns2)), 2)
    return enhancer[index]


# def get_index(p: (int, int), image: dict):
#     # lit_pixel = 0 if inverted else 1
#     # unlit_pixel = 1 if inverted else 1
#     ns = [1 if (i, j) in image.keys() else 0 for j in range(p[1] - 1, p[1] + 2) for i in
#           range(p[0] - 1, p[0] + 2)]
#     index = int("".join(map(str, ns)), 2)
#     return index


def enhance_image(image_enhancer, input_image, infinity_bit: int):
    output_image = dict()
    # visited = set(input_image.keys())
    # nodes_to_visit = list(input_image.keys())

    min_i, max_i = min(p[0] for p in input_image) - 1, max(p[0] for p in input_image) + 2
    min_j, max_j = min(p[1] for p in input_image) - 1, max(p[1] for p in input_image) + 2

    for i in range(min_i, max_i):
        for j in range(min_j, max_j):
            p = get_enhanced_pixel((i, j), input_image, image_enhancer, ((min_i, max_i), (min_j, max_j)), infinity_bit)
            if p:
                output_image[(i, j)] = 1

    # for v in input_image:
    #     for n in [(i, j) for j in range(v[1] - 1, v[1] + 2) for i in range(v[0] - 1, v[0] + 2)
    #               if (i, j) not in visited]:
    #         nodes_to_visit.append(n)

    # while len(nodes_to_visit) > 0:
    #     v = nodes_to_visit.pop(0)
    #     new_pixel = get_enhanced_pixel(v, input_image, image_enhancer)
    #     if new_pixel:
    #         output_image[v] = new_pixel
    return output_image


@solution_timer(2021, 20, 1)
def part_one(input_data: List[str]):
    input_image = dict()

    image_enhancer = [1 if x == '#' else 0 for x in input_data[0]]

    for y, row in enumerate(input_data[2:]):
        for x, pixel in enumerate(row):
            if pixel == '#':
                input_image[(x, y)] = 1

    input_image = enhance_image(image_enhancer, input_image, 0)
    input_image = enhance_image(image_enhancer, input_image, 1)

    answer = len(input_image)
    if not answer:
        raise SolutionNotFoundException(2021, 20, 1)

    return answer


@solution_timer(2021, 20, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2021, 20, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 20)
    part_one(data)
    part_two(data)
