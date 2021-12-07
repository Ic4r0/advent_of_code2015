""" Day 4: The Ideal Stocking Stuffer

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd December 2021
"""

# imports
from utils.parse_input import parse_single_line
import hashlib


# modules
def part_1(input_string: str) -> int:
    """ Code for the 1st part of the 4th day of Advent of Code

    :param input_string: input string
    :return: numeric result
    """
    result = 1
    while True:
        str2hash = input_string + str(result)
        md5_hash = hashlib.md5(str2hash.encode())
        hex_result = md5_hash.hexdigest()
        if hex_result[:5] == '00000':
            return result
        result += 1


def part_2(input_string: str) -> int:
    """ Code for the 2nd part of the 4th day of Advent of Code

    :param input_string: input string
    :return: numeric result
    """
    result = 1
    while True:
        str2hash = input_string + str(result)
        md5_hash = hashlib.md5(str2hash.encode())
        hex_result = md5_hash.hexdigest()
        if hex_result[:6] == '000000':
            return result
        result += 1


def day_4(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 4th day we want to execute

    :param selected_part: selected Advent of Code part of the 4th day
    :param test: flag to use test input
    """
    secret_input = parse_single_line(4, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(secret_input)
        print('The result of 1st part of the 4th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(secret_input)
        print('The result of 2nd part of the 4th day of AoC is: ' + str(result_part_2))
