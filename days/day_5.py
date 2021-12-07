""" Day 5: Doesn't He Have Intern-Elves For This?

Author: Ic4r0 - https://github.com/Ic4r0

Created: 3rd December 2021
"""

# imports
from utils.parse_input import parse_by_line
from re import match


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 5th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    return len([
        row for row in input_list
        if (match(r'^.*(.)\1+', row) and
            match(r'^(?!.*(ab|cd|pq|xy))', row) and
            match(r'^.*([aeiou].*){3,}', row))
    ])


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 5th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    return len([
        row for row in input_list
        if match(r'^.*(..).*\1', row) and match(r'^.*(.).\1', row)
    ])


def day_5(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 5th day we want to execute

    :param selected_part: selected Advent of Code part of the 5th day
    :param test: flag to use test input
    """
    nice_or_naughty_list = parse_by_line(5, int_list=False, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(nice_or_naughty_list)
        print('The result of 1st part of the 5th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(nice_or_naughty_list)
        print('The result of 2nd part of the 5th day of AoC is: ' + str(result_part_2))
