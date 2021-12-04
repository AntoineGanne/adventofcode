import re
from math import floor
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

board_size = 5


@solution_timer(2021, 4, 1)
def part_one(input_data: List[str]):
    drawn_numbers = list(map(int, input_data[0].split(',')))
    nb_boards = floor((len(input_data) - 1) / 6)

    boards, positions_of_numbers = extract_boards(input_data, nb_boards)

    # we have read all the input, now we play the bingo squid game

    # 0 if the number at the position was not drawn
    # 1 if the number at this position has been drawn
    state_of_boards = [[[0] * board_size for _ in range(board_size)] for _ in range(nb_boards)]
    first_winning_board = None
    state_of_winning_board = None
    last_number_called = None
    bingo = False

    for number in drawn_numbers:
        if number not in positions_of_numbers.keys():
            continue
        positions = positions_of_numbers[number]
        # update state of boards
        for pos in positions:
            state_of_boards[pos[0]][pos[1]][pos[2]] = 1

        # we check if there's a BINGO ✨
        for pos in positions:
            board_index = pos[0]
            row_index = pos[1]
            column_index = pos[2]
            bingo = is_there_bingo_on_board(state_of_boards[board_index], row_index, column_index)
            if bingo:
                bingo = True
                first_winning_board = boards[board_index]
                state_of_winning_board = state_of_boards[board_index]
                last_number_called = number
                break
        if bingo:
            break

    sum_unmarked_numbers = calculate_sum_unmarked_numbers(first_winning_board, state_of_winning_board)
    answer = sum_unmarked_numbers * last_number_called

    if not answer:
        raise SolutionNotFoundException(2021, 4, 1)

    return answer


def extract_boards(input_data, nb_boards):
    boards = [[[0] * board_size for _ in range(board_size)] for _ in range(nb_boards)]
    positions_of_numbers = dict()
    board_index = 0
    row_index = 0
    for i, line in enumerate(input_data[1:]):
        if i == 0:
            continue
        if i % (board_size + 1) == 0:
            board_index += 1
            row_index = 0
            continue

        row = list(map(int, re.split(r'\s+', line)))
        for column_index, number in enumerate(row):
            position = [board_index, row_index, column_index]
            if number in positions_of_numbers.keys():
                positions_of_numbers[number].append(position)
            else:
                positions_of_numbers[number] = [position]

            boards[board_index][row_index][column_index] = number
        row_index += 1
    return boards, positions_of_numbers


def calculate_sum_unmarked_numbers(first_winning_board, state_of_winning_board):
    sum_unmarked_numbers = 0
    for i in range(board_size):
        for j in range(board_size):
            if state_of_winning_board[i][j] == 0:
                sum_unmarked_numbers += first_winning_board[i][j]
    return sum_unmarked_numbers


# noinspection DuplicatedCode
@solution_timer(2021, 4, 2)
def part_two(input_data: List[str]):
    drawn_numbers = list(map(int, input_data[0].split(',')))
    nb_boards = floor((len(input_data) - 1) / 6)

    boards, positions_of_numbers = extract_boards(input_data, nb_boards)
    # we have read all the input, now we play the bingo squid game

    # 0 if the number at the position was not drawn
    # 1 if the number at this position has been drawn
    state_of_boards = [[[0] * board_size for _ in range(board_size)] for _ in range(nb_boards)]
    boards_that_have_not_won = {e for e in range(nb_boards)}
    last_number_called = None
    last_winning_board = None
    state_of_last_winning_board = None

    for number in drawn_numbers:
        print("Number drawn:", number)

        if number not in positions_of_numbers.keys():
            continue
        positions = positions_of_numbers[number]
        # update state of boards
        for pos in positions:
            state_of_boards[pos[0]][pos[1]][pos[2]] = 1

        draw_state_of_boards(boards, state_of_boards)

        # we check if there's a BINGO ✨
        for pos in positions:
            board_index = pos[0]
            row_index = pos[1]
            column_index = pos[2]

            if board_index in boards_that_have_not_won:
                bingo = is_there_bingo_on_board(state_of_boards[board_index],row_index,column_index)
                if bingo:
                    print("BINGO!", board_index)
                    boards_that_have_not_won.remove(board_index)
                    if len(boards_that_have_not_won) == 0:
                        last_winning_board = boards[board_index]
                        state_of_last_winning_board = state_of_boards[board_index]
                        last_number_called = number
                        break

        if len(boards_that_have_not_won) == 0:
            break

    sum_unmarked_numbers = calculate_sum_unmarked_numbers(last_winning_board, state_of_last_winning_board)
    answer = sum_unmarked_numbers * last_number_called

    if not answer:
        raise SolutionNotFoundException(2021, 4, 2)
    return answer


def is_there_bingo_on_board(state_of_board: list, row: int, column: int):
    assert 0 <= row < board_size
    assert 0 <= column < board_size
    bingo_row = True
    bingo_column = True
    for i in range(board_size):
        if state_of_board[i][column] == 0:
            bingo_column = False
        if state_of_board[row][i] == 0:
            bingo_row = False
    return bingo_column or bingo_row


def draw_state_of_boards(boards: List, state_of_boards: List):
    assert len(boards) == len(state_of_boards)
    print("boards")
    for index, b in enumerate(boards):
        print(index, ":")
        for i in range(board_size):
            line = ""
            for j in range(board_size):
                if state_of_boards[index][i][j] == 1:
                    number = str(b[i][j])
                    if len(number) <= 1:
                        number = "0" + number
                else:
                    number = "__"
                line = line + number + "|"
            print(line)

    print("-------------------------------------")


if __name__ == '__main__':
    data = get_input_for_day(2021, 4)
    part_one(data)
    part_two(data)
