# https://adventofcode.com/2023/day/4
from typing import NamedTuple
from common.read_input import read_file_lines

TEST_CASE = {
    "p1_result": 13,
    "p2_result": 30,
}


def get_line_points(matches: int) -> int:
    total = 0
    for point in range(0, matches):
        if total == 0:
            total += 1
        else:
            total += total

    return total


def part_one(my_input: [str]):
    total = 0
    for line in my_input:
        matches = 0
        card_num_split = line.split(': ')
        card_num = card_num_split[0]
        winning_num_split = card_num_split[1].split(" | ")
        winning_nums_lst = [int(val) for val in winning_num_split[0].split()]
        my_nums_lst = [int(val) for val in winning_num_split[1].split()]
        for num in winning_nums_lst:
            matches += 1 if num in my_nums_lst else 0
        total += get_line_points(matches)
    return total


# class Scratchcard(NamedTuple):
#     matches: int
#     instances: int
#     number_str: str


class Scratchcard:
    def __init__(self, name: str, matches: int, instances: int, winning_nums: [int], card_nums: [int]):
        self.name = name
        self.matches = matches
        self.instances = instances
        self.winning_nums = winning_nums
        self.card_nums = card_nums

    def __repr__(self):
        return f'{self.name} - Matches : {self.matches} Instances : {self.instances}'


def add_winning_copies(my_cards: [Scratchcard]):
    for i, my_card in enumerate(my_cards):
        if my_card.matches > 0:
            for copy_i in range(1, my_card.matches + 1):
                my_cards[i + copy_i].instances += my_card.instances


def count_instances(my_cards: [Scratchcard]) -> int:
    total = 0
    for card in my_cards:
        total += card.instances
    return total


def part_two(my_input):
    my_cards = []
    for line in my_input:
        matches = 0
        card_num_split = line.split(': ')
        card_num = card_num_split[0]
        winning_num_split = card_num_split[1].split(" | ")
        winning_nums_lst = [int(val) for val in winning_num_split[0].split()]
        my_nums_lst = [int(val) for val in winning_num_split[1].split()]
        for num in winning_nums_lst:
            matches += 1 if num in my_nums_lst else 0
        my_cards.append(Scratchcard(card_num, matches, 1, winning_nums_lst, my_nums_lst))

    add_winning_copies(my_cards)

    return count_instances(my_cards)


if __name__ == '__main__':
    print(f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} ')
    print(f'P1 real answer : {part_one(read_file_lines("input.txt"))}')
    print("------------")
    print(f'P2 test case answer : {part_two(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p2_result"]} ')
    print(f'P2 real answer : {part_two(read_file_lines("input.txt"))}')
