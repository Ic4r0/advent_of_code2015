""" Day 2: I Was Told There Would Be No Math

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd December 2021
"""

# imports
from utils.parse_input import parse_by_line


# modules
def part_1(input_list: list[tuple[int]]) -> int:
    """ Code for the 1st part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    wrapping_paper = 0
    for length, width, height in input_list:
        first_side = length * width
        second_side = width * height
        third_side = height * length
        wrapping_paper += 2 * first_side + 2 * second_side + 2 * third_side + min(first_side, second_side, third_side)
    return wrapping_paper


def part_2(input_list: list[tuple[int]]) -> int:
    """ Code for the 2nd part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    ribbon = 0
    for length, width, height in input_list:
        measurements = [length, width, height]
        measurements.sort()
        measurements.pop()
        ribbon += 2 * sum(measurements) + length * width * height
    return ribbon


def day_2(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 2nd day we want to execute

    :param selected_part: selected Advent of Code part of the 1st day
    :param test: flag to use test input
    """
    present_dimensions_from_input = parse_by_line(2, int_list=False, is_test=test)
    present_dimensions = [
        tuple(int(measure) for measure in measures.split('x')) for measures in present_dimensions_from_input
    ]
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(present_dimensions)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(present_dimensions)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_2))
