import os

import requests

from adventofcode.config import ROOT_DIR
from adventofcode.util.input_helpers import get_input_directory_path,get_input_path


def get_input(year: int, day: int):
    session = _read_session()
    data = _download_input(year, day, session)
    _save_input(data, year, day)


def _download_input(year: int, day: int, session: str) -> bytes:
    """
    Downloads the input as text from the advent of code site
    """
    cookies = {'session': session}
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    # TODO: put User-Agent in env variables
    headers = {'User-Agent': 'github.com/AntoineGanne/adventofcode by antoine.ganne+aoc@hotmail.fr'}
    resp = requests.get(url, cookies=cookies)
    resp.raise_for_status()
    return resp.content  # type: ignore


def _save_input(data: bytes, year: int, day: int) -> None:
    inputs_path = get_input_directory_path(year, day)

    if not os.path.exists((year_path := os.path.join(inputs_path))):
        os.mkdir(year_path)

    with open(get_input_path(year,day), 'wb') as file:
        file.write(data)


def _read_session():
    target = os.path.join(ROOT_DIR, '../../.session')
    path = os.path.abspath(target)

    with open(path) as f:
        return f.read()
