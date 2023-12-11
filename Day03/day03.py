# https://adventofcode.com/2023/day/3
from typing import NamedTuple

from common.read_input import read_file_lines

TEST_CASE = {
    "p1_result": 4361,
    "p2_result": 467835,
}


def is_within_bounds(x: int, y: int, my_input: [str]) -> bool:
    max_y_index = len(my_input) - 1
    max_x_index = len(my_input[0]) - 1
    return 0 <= x <= max_x_index and 0 <= y <= max_y_index


# def is_symbol(x: int, y: int, my_input: [str]) -> bool:
def is_symbol(my_char: str) -> bool:
    return my_char != "." and not str.isdigit(my_char)


def is_symbol_adjacent(x: int, y: int, my_input: [str]) -> bool:
    symbol_above = is_within_bounds(x, y - 1, my_input) and is_symbol(my_input[y - 1][x])
    symbol_below = is_within_bounds(x, y + 1, my_input) and is_symbol(my_input[y + 1][x])
    symbol_left = is_within_bounds(x - 1, y, my_input) and is_symbol(my_input[y][x - 1])
    symbol_right = is_within_bounds(x + 1, y, my_input) and is_symbol(my_input[y][x + 1])
    symbol_top_left = is_within_bounds(x - 1, y - 1, my_input) and is_symbol(my_input[y - 1][x - 1])
    symbol_top_right = is_within_bounds(x + 1, y - 1, my_input) and is_symbol(my_input[y - 1][x + 1])
    symbol_bottom_left = is_within_bounds(x - 1, y + 1, my_input) and is_symbol(my_input[y + 1][x - 1])
    symbol_bottom_right = is_within_bounds(x + 1, y + 1, my_input) and is_symbol(my_input[y + 1][x + 1])

    return (symbol_above or symbol_below or symbol_left or symbol_right or
            symbol_top_left or symbol_top_right or symbol_bottom_left or symbol_bottom_right)


def part_one(my_input: [str]):
    part_numbers = []
    in_number = False
    is_part_number = False
    number_str = ""

    for y, row in enumerate(my_input):
        if in_number and is_part_number:
            part_numbers.append(int(number_str))
        in_number = False
        number_str = ""
        is_part_number = False
        for x, value in enumerate(row):
            if str.isdigit(value):
                in_number = True
                number_str += value
                if is_symbol_adjacent(x, y, my_input):
                    is_part_number = True
            else:  # not in a number or just finished a number_str
                if in_number and is_part_number:
                    part_numbers.append(int(number_str))
                number_str = ""
                in_number = False
                is_part_number = False
    # print(part_numbers)
    return sum(part_numbers)


# def is_number_adjacent(x: int, y: int, my_input: [str]) -> bool:
#     num_above = is_within_bounds(x, y - 1, my_input) and str.isdigit(my_input[y - 1][x])
#     num_below = is_within_bounds(x, y + 1, my_input) and str.isdigit(my_input[y + 1][x])
#     num_left = is_within_bounds(x - 1, y, my_input) and str.isdigit(my_input[y][x - 1])
#     num_right = is_within_bounds(x + 1, y, my_input) and str.isdigit(my_input[y][x + 1])
#     num_top_left = is_within_bounds(x - 1, y - 1, my_input) and str.isdigit(my_input[y - 1][x - 1])
#     num_top_right = is_within_bounds(x + 1, y - 1, my_input) and str.isdigit(my_input[y - 1][x + 1])
#     num_bottom_left = is_within_bounds(x - 1, y + 1, my_input) and str.isdigit(my_input[y + 1][x - 1])
#     num_bottom_right = is_within_bounds(x + 1, y + 1, my_input) and str.isdigit(my_input[y + 1][x + 1])
#
#     return (num_above or
#             num_below or
#             num_left or
#             num_right or
#             num_top_left or
#             num_top_right or
#             num_bottom_left or
#             num_bottom_right)


class FullNumber(NamedTuple):
    x_start: int
    x_end: int
    number_str: str


def get_full_number(x: int, row: [str]) -> FullNumber:
    number_str = ""
    x_start = x
    while x_start > 0 and str.isdigit(row[x_start - 1]):
        x_start -= 1
    x_end = x_start
    while x_end <= len(row) - 1 and str.isdigit(row[x_end]):
        number_str += row[x_end]
        x_end += 1
    return FullNumber(x_start, x_end - 1, number_str)


def get_adjacent_numbers_on_row(x: int, row: str) -> [str]:
    max_x_index = len(row) - 1
    my_numbers_strs = []
    i = x - 1 if x > 0 else x
    while i <= max_x_index and i <= x + 1:
        if str.isdigit(row[i]):
            full_number = get_full_number(i, row)
            my_numbers_strs.append(full_number.number_str)
            i = full_number.x_end
        i += 1
    return my_numbers_strs


def get_adjacent_numbers(y: int, x: int, my_input: [str]) -> [str]:
    max_y_index = len(my_input) - 1
    max_x_index = len(my_input[0]) - 1
    my_adjacent_numbers = []
    # find first digit in row above that touches symbol

    if y > 0:  # check row above
        my_adjacent_numbers += get_adjacent_numbers_on_row(x, my_input[y - 1])

    if x > 0 and str.isdigit(my_input[y][x - 1]):  # check left
        my_adjacent_numbers.append(get_full_number(x - 1, my_input[y]).number_str)
    if x < max_x_index and str.isdigit(my_input[y][x + 1]):  # check right
        my_adjacent_numbers.append(get_full_number(x + 1, my_input[y]).number_str)

    if y < max_y_index:  # check row below
        my_adjacent_numbers += get_adjacent_numbers_on_row(x, my_input[y + 1])

    return my_adjacent_numbers


def part_two(my_input):
    gear_ratios = []

    for y, row in enumerate(my_input):
        for x, value in enumerate(row):
            if value != "." and not str.isdigit(value):  # i.e this is a SYMBOL
                my_numbers = get_adjacent_numbers(y, x, my_input)
                if len(my_numbers) == 2:
                    gear_ratios.append(int(my_numbers[0]) * int(my_numbers[1]))

    return sum(gear_ratios)


if __name__ == '__main__':
    # print(f'P1 test case answer : {part_one(read_file_lines("test_input2.txt"))}, expecting {TEST_CASE["p1_result"]} ')
    # print(f'P1 real answer : {part_one(read_file_lines("input.txt"))} NB - 506273 is too low')
    print("------------")
    print(f'P2 test case answer : {part_two(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p2_result"]} ')
    print(f'P2 test2 case answer : {part_two(read_file_lines("test_input2.txt"))}, expecting {TEST_CASE["p2_result"]} ')
    print(f'P2 real answer : {part_two(read_file_lines("input.txt"))}   NB 72533474 is too low')
