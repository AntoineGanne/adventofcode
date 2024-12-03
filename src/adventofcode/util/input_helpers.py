import os
from typing import List

from adventofcode.config import ROOT_DIR


def get_input_for_day(year: int, day: int) -> List[str]:
    """
    Get the input for the year/day as list of strings
    """
    input_file = os.path.join(get_input_directory_path(year, day), f'input_{day:02}_{year:04}.txt')
    return _get_input(input_file)


def get_input_for_day_as_str(year: int, day: int) -> str:  # TODO: delete this function (only used in tests)
    input_file = get_input_path(year, day)
    return _read_file(input_file)


def get_input_path(year: int, day: int) -> str:
    return os.path.join(get_input_directory_path(year, day), f'input_{day:02}_{year:04}.txt')


def get_test_input_for_day(year: int, day: int) -> List[str]:
    """
    Get the input for the year/day as list of strings
    """
    input_file = get_example_input_path(year, day)
    return _get_input(input_file)


def get_example_input_path(year: int, day: int) -> str:
    return os.path.join(get_input_directory_path(year, day), f'example_input_{day:02}_{year:04}.txt')


def get_test_input_module_path(year) -> str:
    test_input_module_path = os.path.abspath(os.path.join(ROOT_DIR, 'test_inputs', f'{year}'))
    return test_input_module_path


def get_directory_path(year, day) -> str:
    return os.path.abspath(os.path.join(ROOT_DIR, f'year_{year:04}', f'day_{day:02}'))


def get_input_directory_path(year, day) -> str:
    return os.path.abspath(os.path.join(get_directory_path(year, day), 'inputs'))


def _read_lines(file_name) -> List[str]:
    """
    Reads file to list of string
    """
    with open(file_name) as file:
        lines = file.readlines()

    return lines


def _get_input(file_name) -> List[str]:
    """
    Strips new lines from input file and returns it as list of string
    """
    lines = _read_lines(file_name)
    return [line.strip() for line in lines]


def _read_file(file_name) -> str:
    """
    Reads file to string
    """
    with open(file_name) as file:
        content = file.read()

    content = content.rstrip('\n')
    return content
