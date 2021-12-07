""" Day 10: Elves Look, Elves Say

Author: Ic4r0 - https://github.com/Ic4r0

Created: 7th December 2021
"""

# imports
from utils.parse_input import parse_single_line


# modules
def compute_repetitions(input_string: str) -> str:
    """ Code to get the required string from the input

    :param input_string: input string
    :return: numeric result
    """
    idx = 0
    result = ''
    while idx < len(input_string):
        current_digit = input_string[idx]
        temp_current = current_digit
        repetitions = 0
        while temp_current == current_digit:
            repetitions += 1
            idx += 1
            if idx < len(input_string):
                temp_current = input_string[idx]
            else:
                break
        result += str(repetitions) + current_digit
    return result


def part_1(input_string: str) -> int:
    """ Code for the 1st part of the 10th day of Advent of Code

    :param input_string: input string
    :return: numeric result
    """
    current_string = input_string
    for _ in range(40):
        current_string = compute_repetitions(current_string)
    return len(current_string)


def part_2(input_string: str) -> int:
    """ Code for the 2nd part of the 10th day of Advent of Code

    :param input_string: input string
    :return: numeric result
    """
    current_string = input_string
    for _ in range(50):
        current_string = compute_repetitions(current_string)
    return len(current_string)


def day_10(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 10th day we want to execute

    :param selected_part: selected Advent of Code part of the 10th day
    :param test: flag to use test input
    """
    input_digits = parse_single_line(10, is_test=test)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_digits)
        print('The result of 1st part of the 10th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_digits)
        print('The result of 2nd part of the 10th day of AoC is: ' + str(result_part_2))
