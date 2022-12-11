import functools
import math
import re
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


class MonkeyManager:
    def __init__(self):
        self.monkeys: List[Monkey] = []
        self.common_prod = 0

    def init_product_of_divisors(self):
        self.common_prod = math.prod([m.test_number for m in self.monkeys])

    def add_monkey(self, monkey):
        self.monkeys.append(monkey)

    def send_item(self, monkey_id, item):
        self.monkeys[monkey_id].receive(item)

    def round(self, is_part_two: bool = False):
        for monkey in self.monkeys:
            monkey.turn(is_part_two)

    def max_n_activity(self, n: int):
        assert n < len(self.monkeys)
        return sorted([m.activity for m in self.monkeys], reverse=True)[:n]

    def get_test_number_of_monkey(self, monkey_id: int) -> int:
        return self.monkeys[monkey_id].test_number

    def print(self):
        print([monkey.items for monkey in self.monkeys])


class Monkey:
    def __init__(self, monkey_id: int,
                 items: List[int],
                 operation: str,
                 test: int,
                 monkeyIfTrue: int,
                 monkeyIfFalse: int,
                 monkeyManager: MonkeyManager):
        self.monkeyId = monkey_id
        self.items = items
        self.operation = operation
        self.test_number = test
        self.monkeyIfTrue = monkeyIfTrue
        self.monkeyIfFalse = monkeyIfFalse
        self.activity = 0
        self.monkeyManager = monkeyManager

    def receive(self, item: int):
        self.items.append(item)

    def inspect_part_one(self, item: int) -> (int, int):
        self.activity += 1
        op = self.operation.replace("old", str(item))
        worry_level = eval(op) // 3
        if worry_level % self.test_number == 0:
            return worry_level, self.monkeyIfTrue
        else:
            return worry_level, self.monkeyIfFalse

    def inspect_part_two(self, item: int) -> (int, int):
        self.activity += 1
        op = self.operation.replace("old", str(item))
        worry_level = eval(op)
        if worry_level % self.test_number == 0:
            send_to = self.monkeyIfTrue
        else:
            send_to = self.monkeyIfFalse
        test_number_modulo = self.monkeyManager.common_prod
        return worry_level % test_number_modulo, send_to

    def turn(self, is_part_two: bool = False):
        for item in self.items:
            if is_part_two:
                new_item, monkey_to_send_item = self.inspect_part_two(item)
            else:
                new_item, monkey_to_send_item = self.inspect_part_one(item)

            self.monkeyManager.send_item(monkey_to_send_item, new_item)
        self.items = []


@solution_timer(2022, 11, 1)
def part_one(input_data: List[str]):
    manager = read_input(input_data)

    for round in range(20):
        manager.round()

    print(manager.max_n_activity(2))
    answer = functools.reduce(lambda a, b: a * b,
                              manager.max_n_activity(2))

    if not answer:
        raise SolutionNotFoundException(2022, 11, 1)

    return answer


def read_input(input_data):
    monkey_id = 0
    manager = MonkeyManager()
    for i in range(0, len(input_data), 7):
        start_items = re.findall(r'\d+', input_data[i + 1])
        start_items = list(map(int, start_items))
        operation = input_data[i + 2].split('=')[-1]
        test_number = int(input_data[i + 3].split(' ')[-1])
        monkeytrue = int(input_data[i + 4].split(' ')[-1])
        monkeyfalse = int(input_data[i + 5].split(' ')[-1])
        monkey = Monkey(monkey_id,
                        start_items,
                        operation,
                        test_number,
                        monkeytrue,
                        monkeyfalse,
                        manager)
        manager.add_monkey(monkey)
        monkey_id += 1
    manager.init_product_of_divisors()
    return manager


@solution_timer(2022, 11, 2)
def part_two(input_data: List[str]):
    manager = read_input(input_data)

    for round in range(10_000):
        manager.round(True)

    print(manager.max_n_activity(2))
    answer = functools.reduce(lambda a, b: a * b,
                              manager.max_n_activity(2))
    if not answer:
        raise SolutionNotFoundException(2022, 11, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2022, 11)
    part_one(data)
    part_two(data)
