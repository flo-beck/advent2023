# https://adventofcode.com/2023/day/1

from common.read_input import read_file_lines

TEST_CASE = {
    "p1_result": 142,
    "p2_result": 281,
}


def get_str_first_digit(line: str) -> str:
    for char in line:
        if str.isdigit(char):
            return char
    return "nope"


def part_one(my_input):
    calibration_total = 0
    for line in my_input:
        # read each line and detect the first and last digit from this line
        first_digit = get_str_first_digit(line)
        last_digit = get_str_first_digit(reversed(line))
        line_calibration = int(first_digit + last_digit)
        calibration_total += line_calibration
    return calibration_total


NUMBER = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def get_first_digit_position(line: str) -> int:
    for pos, char in enumerate(line):
        if str.isdigit(char):
            return pos
    return -1


def get_last_digit_position(line: str) -> int:
    for i in range(len(line) - 1, -1, -1):
        if str.isdigit(line[i]):
            return i
    return -1


def get_first_number_position(line: str) -> (int, str):
    first_match = (len(line), "nothing")
    for number in NUMBER:
        pos = line.find(number)
        if pos != -1 and pos < first_match[0]:
            first_match = (pos, number)
    return first_match


def get_last_number_position(line: str) -> (int, str):
    last_match = (-1, "nothing")
    for number in NUMBER:
        pos = line.rfind(number)
        if pos != -1 and pos > last_match[0]:
            last_match = (pos, number)
    return last_match


def get_str_first_digit2(line: str) -> str:
    digit_position = get_first_digit_position(line)
    number_position = get_first_number_position(line)
    if digit_position == -1 and number_position[0] == len(line):
        print(f"nothing found for FIRST in {line}")

    if digit_position == -1 or number_position[0] < digit_position:
        return NUMBER[number_position[1]]
    return str(line[digit_position])


def get_str_last_digit2(line: str) -> str:
    digit_position = get_last_digit_position(line)
    number_position = get_last_number_position(line)
    if digit_position == -1 and number_position[0] == -1:
        print(f"nothing found for LAST in {line}")
    if digit_position == -1 or number_position[0] > digit_position:
        try:
            return NUMBER[number_position[1]]
        except KeyError:
            print(line)
    return str(line[digit_position])


def part_two(my_input):
    calibration_total = 0
    for line in my_input:
        # read each line and detect the first and last digit from this line
        first_digit = get_str_first_digit2(line)
        last_digit = get_str_last_digit2(line)
        line_calibration = int(first_digit + last_digit)
        calibration_total += line_calibration
    return calibration_total


if __name__ == '__main__':
    print(f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} ')
    print(f'P1 real answer : {part_one(read_file_lines("input.txt"))}')
    print("------------")
    print(f'P2 test case answer : {part_two(read_file_lines("test_input2.txt"))}, expecting {TEST_CASE["p2_result"]} ')
    print(f'P2 real answer (previous was 55001 - this is wrong): {part_two(read_file_lines("input.txt"))}')
