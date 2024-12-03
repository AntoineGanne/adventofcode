import os
import sys
from argparse import ArgumentParser
from typing import List, Tuple
from datetime import date

from requests import HTTPError

from adventofcode.config import ROOT_DIR
from adventofcode.scripts.get_inputs import get_input
from adventofcode.util.console import console
from adventofcode.util.input_helpers import get_input_for_day, get_directory_path, get_input_directory_path, \
    get_example_input_path, get_input_path


def add_day():
    year, day = _parse_args(sys.argv[1:])
    if year is None:
        year = "2022"
    console.print(f'Creating solution day file for year {year} day {day}')

    module_path = os.path.join(ROOT_DIR, f'year_{year}')
    create_module_dir(module_path)

    day_directory_path = get_directory_path(year, day)
    create_module_dir(day_directory_path)

    solution_file = os.path.join(day_directory_path, f'solution_{day:02}_{year:4}.py')
    solution_template_path = os.path.join(ROOT_DIR, 'scripts', 'templates', 'day_template.txt')
    write_solution_template(solution_file, solution_template_path, year, day)

    test_file = os.path.join(day_directory_path, f'test_day_{day:02}_{year}.py')
    test_template_path = os.path.join(ROOT_DIR, 'scripts', 'templates', 'test_template.txt')
    write_solution_template(test_file, test_template_path, year, day)

    input_module_path = get_input_directory_path(year, day)
    create_dir(input_module_path)

    example_file_input = get_example_input_path(year, day)
    if not os.path.exists(example_file_input):
        with open(example_file_input, 'w'):
            pass

    verify_input_exists(year, day)


def write_solution_template(path: str, template_path: str, year: int, day: int) -> None:
    if not os.path.exists(path):
        template = _read_template(template_path, year, day)
        with open(path, 'w') as f:
            f.write(template)
        console.print(f'[green]Wrote template to {path}')
    else:
        console.print(f'[yellow]Did not write template for year {year} day {day}, the file already exists.')


def create_module_dir(path: str) -> None:
    create_dir(path)

    if not os.path.exists(init_file := os.path.join(path, '__init__.py')):
        with open(init_file, 'w'):
            pass


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)


def verify_input_exists(year: int, day: int) -> None:
    try:
        _ = get_input_for_day(year, day)
        console.print(f'Input data already exists for year {year} day {day}, skipping download')
        return
    except FileNotFoundError:
        try:
            get_input(year, day)
            console.print(f'Automatically downloaded input data for year {year} day {day}')
            return
        except HTTPError as e:
            console.print(f'[red]Could not retrieve input data for year {year} day {day} automatically: {e}')
        except FileNotFoundError:
            console.print(f'[red]Could not retrieve input data for year {year} day {day}: .session set incorrectly')

    raise ValueError('Exception occurred in verify_input_exists')


def _read_template(template_path: str, year: int, day: int) -> str:
    with open(template_path) as f:
        template = f.read()

    template = template.replace('{year}', f'{year:04}')
    template = template.replace('{day}', str(day))
    template = template.replace('{file_day}', f'{day:02}')

    return template


def read_solution_template(year: int, day: int) -> str:
    template_path = os.path.join(ROOT_DIR, 'scripts/templates/day_template.txt')
    return _read_template(template_path, year, day)


def _parse_args(args: List[str]) -> Tuple[int, int]:
    parser = ArgumentParser(description='Add a day')
    parser.add_argument('--year', type=int, required=False, default=date.today().year, help='The year of the exercise')
    parser.add_argument('--day', type=int, required=False, default=date.today().day, help='The day of the exercise')
    parsed = parser.parse_args(args)
    return parsed.year, parsed.day


if __name__ == '__main__':
    add_day()
