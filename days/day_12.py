""" Day 12: JSAbacusFramework.io

Author: Ic4r0 - https://github.com/Ic4r0

Created: 12th December 2021
"""

# imports
from utils.parse_input import parse_single_line
from re import findall
import json


# modules
def part_1(input_string: str) -> int:
    """ Code for the 1st part of the 12th day of Advent of Code

    :param input_string: input string
    :return: string result
    """
    matched_numbers = findall(r'-?[0-9]+', input_string)
    if matched_numbers:
        return sum(int(number) for number in matched_numbers)
    return 0


def part_2(input_string: str) -> int:
    """ Code for the 2nd part of the 12th day of Advent of Code

    :param input_string: input string
    :return: string result
    """
    new_input_string = str(json.loads(
        input_string,
        object_hook=lambda obj: {} if 'red' in obj.values() else obj
    ))
    matched_numbers = findall(r'-?[0-9]+', new_input_string)
    if matched_numbers:
        return sum(int(number) for number in matched_numbers)
    return 0


def day_12(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 12th day we want to execute

    :param selected_part: selected Advent of Code part of the 12th day
    :param test: flag to use test input
    """
    input_json = parse_single_line(12, is_test=test)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_json)
        print('The result of 1st part of the 12th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_json)
        print('The result of 2nd part of the 12th day of AoC is: ' + str(result_part_2))
