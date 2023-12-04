# https://adventofcode.com/2023/day/1
import re

from common.read_input import read_file_lines

TEST_CASE = {
    "p1_result": 8,
    "p2_result": 2286,
}


class Handful:
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green

    def __repr__(self):
        return f'HANDFUL - Red : {self.red} Blue : {self.blue} Green : {self.green}'


def get_rounds(game_record) -> int:
    rounds_str = re.findall(r'Game \d+: (.*)', game_record)[0]
    rounds_list = rounds_str.split(';')
    return len(rounds_list)


def get_handfuls(game_record) -> [Handful]:
    rounds_str = re.findall(r'Game \d+: (.*)', game_record)[0]
    rounds_list = rounds_str.split(';')
    handfuls = []
    for handful in rounds_list:
        amount_colour_list = [x.strip() for x in handful.split(',')]
        amount_red = 0
        amount_blue = 0
        amount_green = 0
        for colour in amount_colour_list:
            split = colour.split(" ")
            if split[1] == 'red':
                amount_red = int(split[0])
            elif split[1] == 'blue':
                amount_blue = int(split[0])
            else:
                amount_green = int(split[0])
        handfuls.append(Handful(amount_red, amount_blue, amount_green))
    return handfuls


def get_min_possible_cubes(handfuls, colour_str) -> int:
    min_colour = 0
    for handful in handfuls:
        if colour_str == 'red':
            colour_to_check = handful.red
        elif colour_str == 'blue':
            colour_to_check = handful.blue
        else:
            colour_to_check = handful.green
        if colour_to_check > min_colour:
            min_colour = colour_to_check
    return min_colour


def get_game_id(game_record) -> int:
    return int(re.findall(r'Game (\d+):', game_record)[0])


class Game:
    def __init__(self, game_record):
        self.id = get_game_id(game_record)
        self.total_rounds = get_rounds(game_record)
        self.round_handfuls = get_handfuls(game_record)
        self.min_red = get_min_possible_cubes(self.round_handfuls, "red")
        self.min_blue = get_min_possible_cubes(self.round_handfuls, "blue")
        self.min_green = get_min_possible_cubes(self.round_handfuls, "green")
        self.power = self.min_red * self.min_blue * self.min_green

    def __repr__(self):
        return f'Game {self.id} - Min-Red : {self.min_red} Min-Blue : {self.min_blue} Min-Green : {self.min_green} Power : {self.power}'


MAX_CUBES = {
    "red": 12,
    "blue": 14,
    "green": 13
}


def part_one(my_input):
    games_list = [Game(line) for line in my_input]
    total_possible_games = 0
    for game in games_list:
        game_possible = True
        for handful in game.round_handfuls:
            if handful.red > MAX_CUBES["red"] or handful.blue > MAX_CUBES["blue"] or handful.green > MAX_CUBES["green"]:
                game_possible = False
        if game_possible:
            total_possible_games += game.id
    return total_possible_games


def part_two(my_input):
    games_list = [Game(line) for line in my_input]
    total_powers = 0
    for game in games_list:
        total_powers += game.power
    return total_powers


if __name__ == '__main__':
    print(f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} ')
    print(f'P1 real answer : {part_one(read_file_lines("input.txt"))} NB 2095 is too high')
    print("------------")
    print(f'P2 test case answer : {part_two(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p2_result"]} ')
    print(f'P2 real answer : {part_two(read_file_lines("input.txt"))}')
