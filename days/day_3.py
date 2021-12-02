""" Day 3: Perfectly Spherical Houses in a Vacuum

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd December 2021
"""

# imports
from utils.parse_input import parse_single_line
import operator


# modules
def part_1(input_string: str) -> int:
    """ Code for the 1st part of the 3rd day of Advent of Code

    :param input_string: input string
    :return: numeric result
    """
    houses = {
        (0, 0): 1
    }
    current_position = (0, 0)

    for direction in input_string:
        if direction == '^':
            current_position = (current_position[0], current_position[1] + 1)
        elif direction == 'v':
            current_position = (current_position[0], current_position[1] - 1)
        elif direction == '<':
            current_position = (current_position[0] - 1, current_position[1])
        elif direction == '>':
            current_position = (current_position[0] + 1, current_position[1])

        if current_position not in houses:
            houses[current_position] = 1
        else:
            houses[current_position] += 1

    return len(list(houses))


def part_2(input_string: str) -> int:
    """ Code for the 2nd part of the 3rd day of Advent of Code

    :param input_string: input string
    :return: numeric result
    """
    houses = {
        (0, 0): 1
    }
    current_position_santa = (0, 0)
    current_position_robot = (0, 0)
    current_position = (0, 0)

    for idx, direction in enumerate(input_string):
        step = (0, 0)
        if direction == '^':
            step = (0, 1)
        elif direction == 'v':
            step = (0, -1)
        elif direction == '<':
            step = (-1, 0)
        elif direction == '>':
            step = (1, 0)

        if idx % 2 == 0:
            current_position_santa = tuple(map(operator.add, current_position_santa, step))
            current_position = current_position_santa
        else:
            current_position_robot = tuple(map(operator.add, current_position_robot, step))
            current_position = current_position_robot

        if current_position not in houses:
            houses[current_position] = 1
        else:
            houses[current_position] += 1

    return len(list(houses))


def day_3(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 3rd day we want to execute

    :param selected_part: selected Advent of Code part of the 1st day
    :param test: flag to use test input
    """
    directions = parse_single_line(3, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(directions)
        print('The result of 1st part of the 3rd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(directions)
        print('The result of 1st part of the 3rd day of AoC is: ' + str(result_part_2))
