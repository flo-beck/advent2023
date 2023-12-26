# https://adventofcode.com/2023/day/4
from typing import NamedTuple
from common.read_input import read_file_lines

TEST_CASE = {
    "p1_result": 35,
    "p2_result": '?',
}


class RangeMap:
    def __init__(self, dest_start: int, source_start: int, length: int):
        self.source_start = source_start
        self.dest_start = dest_start
        self.length = length

    def __repr__(self):
        return f'Source {self.source_start} - Dest {self.dest_start} - Len {self.length}'


def get_number_from_map(source: int, my_map: [RangeMap]) -> int:
    dest = source
    for my_range in my_map:
        if my_range.source_start <= source < my_range.source_start + my_range.length:
            dest = my_range.dest_start + (source - my_range.source_start)
    return dest


class Seed:
    def __init__(self, num: int):
        self.num = num
        self.soil = 0
        self.fertilizer = 0
        self.water = 0
        self.light = 0
        self.temp = 0
        self.humidity = 0
        self.location = 0

    def __repr__(self):
        return f'Seed {self.num} \nSoil : {self.soil}\nFertilizer : {self.fertilizer}\nWater : {self.water}\nLight : {self.light}\nTemp : {self.temp}\nHumidity : {self.humidity}\nLocation : {self.location}'

    def set_soil(self, soil_map: [RangeMap]):
        self.soil = get_number_from_map(self.num, soil_map)

    def set_fertilizer(self, fertilizer_map: [RangeMap]):
        self.fertilizer = get_number_from_map(self.soil, fertilizer_map)

    def set_water(self, water_map: [RangeMap]):
        self.water = get_number_from_map(self.fertilizer, water_map)

    def set_light(self, light_map: [RangeMap]):
        self.light = get_number_from_map(self.water, light_map)

    def set_temp(self, temp_map: [RangeMap]):
        self.temp = get_number_from_map(self.light, temp_map)

    def set_humidity(self, humidity_map: [RangeMap]):
        self.humidity = get_number_from_map(self.temp, humidity_map)

    def set_location(self, location_map: [RangeMap]):
        self.location = get_number_from_map(self.humidity, location_map)


MAPS = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": []
}


def part_one(my_input: [str]):
    # parse input
    seed_lst = [Seed(int(val)) for val in my_input[0].split(":")[1].split()]
    map_name = ""
    map_lst = []
    for line in my_input[2:]:
        if line == "" and len(map_lst) > 0:
            MAPS[map_name] = map_lst
            map_lst = []
        elif " map:" in line:
            map_name = line.split(" ")[0]
        else:
            nums = line.split()
            map_lst.append(RangeMap(int(nums[0]), int(nums[1]), int(nums[2])))
    MAPS[map_name] = map_lst

    # print(seed_lst)
    # print(MAPS)

    # Calc Each seed
    lowest_location = 9999999999999999
    for seed in seed_lst:
        seed.set_soil(MAPS["seed-to-soil"])
        seed.set_fertilizer(MAPS["soil-to-fertilizer"])
        seed.set_water(MAPS["fertilizer-to-water"])
        seed.set_light(MAPS["water-to-light"])
        seed.set_temp(MAPS["light-to-temperature"])
        seed.set_humidity(MAPS["temperature-to-humidity"])
        seed.set_location(MAPS["humidity-to-location"])
        lowest_location = seed.location if seed.location < lowest_location else lowest_location
    print(seed_lst)
    return lowest_location


# def part_two(my_input):
#     return 1


if __name__ == '__main__':
    print(f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} ')
    print(f'P1 real answer : {part_one(read_file_lines("input.txt"))} 141508751 is too low')
    # print("------------")
    # print(f'P2 test case answer : {part_two(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p2_result"]} ')
    # print(f'P2 real answer : {part_two(read_file_lines("input.txt"))}')
