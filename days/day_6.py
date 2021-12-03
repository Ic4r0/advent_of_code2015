""" Day 6: Probably a Fire Hazard

Author: Ic4r0 - https://github.com/Ic4r0

Created: 3rd December 2021
"""

# imports
from utils.parse_input import parse_by_line
from re import match


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 6th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    light_grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for idx, instruction in enumerate(input_list):
        instruction_match = match(r'^(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)$', instruction)
        command, x1, y1, x2, y2 = instruction_match.groups()
        for y in range(int(y1), int(y2) + 1):
            for x in range(int(x1), int(x2) + 1):
                if command == 'turn on':
                    light_grid[y][x] = 1
                elif command == 'turn off':
                    light_grid[y][x] = 0
                elif command == 'toggle':
                    current_state = light_grid[y][x]
                    light_grid[y][x] = 0 if current_state == 1 else 1
    return sum([sum(row) for row in light_grid])


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 6th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    light_grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for idx, instruction in enumerate(input_list):
        instruction_match = match(r'^(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)$', instruction)
        command, x1, y1, x2, y2 = instruction_match.groups()
        for y in range(int(y1), int(y2) + 1):
            for x in range(int(x1), int(x2) + 1):
                if command == 'turn on':
                    light_grid[y][x] += 1
                elif command == 'turn off':
                    light_grid[y][x] = 0 if light_grid[y][x] < 1 else light_grid[y][x] - 1
                elif command == 'toggle':
                    light_grid[y][x] += 2
    return sum([sum(row) for row in light_grid])


def day_6(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 6th day we want to execute

    :param selected_part: selected Advent of Code part of the 6th day
    :param test: flag to use test input
    """
    light_instructions = parse_by_line(6, int_list=False, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(light_instructions)
        print('The result of 1st part of the 6th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(light_instructions)
        print('The result of 1st part of the 6th day of AoC is: ' + str(result_part_2))
