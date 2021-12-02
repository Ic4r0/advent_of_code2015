""" Day 1: Not Quite Lisp

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd December 2021
"""

# imports
from utils.parse_input import parse_single_line


# modules
def part_1(input_string: str) -> int:
    """ Code for the 1st part of the 1st day of Advent of Code

    :param input_string: input string
    :return: numeric result
    """
    increments = [1 if parenthesis == '(' else -1 for parenthesis in input_string]
    return sum(increments)


def part_2(input_string: str) -> int:
    """ Code for the 2nd part of the 1st day of Advent of Code

    :param input_string: input string
    :return: numeric result
    """
    floor = 0
    for idx, parenthesis in enumerate(input_string):
        if parenthesis == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return idx + 1
    return -1


def day_1(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 1st day we want to execute

    :param selected_part: selected Advent of Code part of the 1st day
    :param test: flag to use test input
    """
    directions = parse_single_line(1, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(directions)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(directions)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_2))
