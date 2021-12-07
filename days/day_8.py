""" Day 8: Matchsticks

Author: Ic4r0 - https://github.com/Ic4r0

Created: 7th December 2021
"""

# imports
from utils.parse_input import parse_by_line
from re import match


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 8th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    code_strings_length = sum(len(elem) for elem in input_list)
    char_strings_length = 0
    for string in input_list:
        trimmed_string = string[1:-1]
        char_single_string_length = 0
        idx = 0
        while idx < len(trimmed_string):
            if trimmed_string[idx] == '\\':
                if trimmed_string[idx + 1] == '\\' or trimmed_string[idx + 1] == '"':
                    char_single_string_length += 1
                    idx += 1
                elif match(r'^(x[0-9a-fA-F]{2})', trimmed_string[idx + 1:]):
                    char_single_string_length += 1
                    idx += 3
            else:
                char_single_string_length += 1
            idx += 1
        char_strings_length += char_single_string_length
    return code_strings_length - char_strings_length


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 8th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    new_input_list = []
    for string in input_list[:]:
        new_string = ''
        idx = 0
        while idx < len(string):
            if string[idx] == '"':
                new_string += '\\"'
            elif string[idx] == '\\':
                if string[idx + 1] == '"':
                    new_string += '\\\\\\"'
                    idx += 1
                else:
                    new_string += '\\\\'
            else:
                new_string += string[idx]
            idx += 1
        new_input_list.append('"' + new_string + '"')

    code_original_strings_length = sum(len(elem) for elem in input_list)
    code_new_strings_length = sum(len(elem) for elem in new_input_list)
    return code_new_strings_length - code_original_strings_length


def day_8(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 8th day we want to execute

    :param selected_part: selected Advent of Code part of the 8th day
    :param test: flag to use test input
    """
    strings_list = parse_by_line(8, int_list=False, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(strings_list)
        print('The result of 1st part of the 8th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(strings_list)
        print('The result of 2nd part of the 8th day of AoC is: ' + str(result_part_2))
