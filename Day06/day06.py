# https://adventofcode.com/2023/day/6
import math

from common.read_input import read_file_lines
from collections import namedtuple
import time


TEST_CASE = {
    "p1_result": 288,
    "p2_result": 71503,
}


def parse_race_input(my_input: [str]) -> []:
    time_lst = [int(val) for val in my_input[0].split(":")[1].split()]
    distance_lst = [int(val) for val in my_input[1].split(":")[1].split()]
    Race = namedtuple('Race', 'time distance')
    races = []
    for i in range(0, len(time_lst)):
        races.append(Race(time_lst[i], distance_lst[i]))
    return races


def calc_distance_travelled(race_time: int, len_push_button: int) -> int:
    return (race_time - len_push_button) * len_push_button


def count_winning_options_race_lst(races: []) -> [int] :
    winning_options_lst = []

    for race in races:
        winning_options = 0
        for second in range(1, race.time):
            if calc_distance_travelled(race.time, second) > race.distance:
                winning_options += 1
        winning_options_lst.append(winning_options)
    return winning_options_lst


def part_one(my_input: [str]):
    races = parse_race_input(my_input)
    winning_options_lst = count_winning_options_race_lst(races)
    return math.prod(winning_options_lst)


def parse_part2_race_input(my_input: [str]):
    part2_time = int(my_input[0].split(":")[1].replace(" ", ""))
    part2_distance = int(my_input[1].split(":")[1].replace(" ", ""))
    Race = namedtuple('Race', 'time distance')
    return Race(part2_time, part2_distance)


def part_two(my_input):
    race = parse_part2_race_input(my_input)
    st = time.time()
    winning_options_lst = count_winning_options_race_lst([race])

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    return winning_options_lst[0]


if __name__ == '__main__':
    print(f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} ')
    print(f'P1 real answer : {part_one(read_file_lines("input.txt"))}, expecting 440000')
    print("------------")
    print(f'P2 test case answer : {part_two(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p2_result"]} ')
    print(f'P2 real answer : {part_two(read_file_lines("input.txt"))}')
