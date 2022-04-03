from adventofcode.util.input_helpers import get_test_input_for_day
from adventofcode.year_2021.day_20_2021 import part_two, part_one, get_enhanced_pixel


def test():
    # img = {(5, 6): 1, (6, 7): 1}
    # ns = get_index((6, 6), img)
    # assert ns == 34

    image_enhancer = [1 if x == '#' else 0 for x in
                      "#.#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"]

    img = {(-1, 6): 1, (0, 7): 1}
    ns = get_enhanced_pixel((0, 6), img, image_enhancer,
                            ((0, 6), (0, 6)), 0)
    assert ns == 1

    img = {}
    ns = get_enhanced_pixel((6, 6), img, image_enhancer,
                            ((0, 6), (0, 6)), 0)
    assert ns == 1



def test_part_one():
    answer = part_one(get_test_input_for_day(2021, 20))

    assert answer == 35


def test_part_two():
    answer = part_two(get_test_input_for_day(2021, 20))
    assert answer is not None
