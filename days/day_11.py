""" Day 11: Corporate Policy

Author: Ic4r0 - https://github.com/Ic4r0

Created: 8th December 2021
"""

# imports
from utils.parse_input import parse_single_line


# modules
def replace_char(string: str, new_char: str, idx: int) -> str:
    """ Replace new_char in string at idx

    :param string: original string
    :param new_char: new character to replace
    :param idx: index of the character to replace
    :return: check
    """
    string_list = list(string)
    string_list[idx] = new_char
    return ''.join(string_list)


def increase_password(password: str) -> str:
    """ Increase a password right to left

    :param password: password to increase
    :return: check
    """
    new_string = password
    for idx in range(len(password) - 1, -1, -1):
        char_at_idx = password[idx]
        char_int = ord(char_at_idx)
        if char_int < ord('z'[0]):
            new_char = chr(char_int + 1)
            new_string = replace_char(new_string, new_char, idx)
            break
        else:
            new_char = 'a'
            new_string = replace_char(new_string, new_char, idx)

    return new_string


def check_increasing_characters(password: str) -> bool:
    """ Check if there are at least 3 consecutive increasing characters

    :param password: password to check
    :return: check
    """
    idx = 0
    while idx < len(password) - 2:
        first = ord(password[idx])
        second = ord(password[idx + 1])
        third = ord(password[idx + 2])
        if first + 1 == second and second + 1 == third:
            return True
        idx += 1
    return False


def check_forbidden_characters(password: str) -> bool:
    """ Check if there are forbidden characters

    :param password: password to check
    :return: check
    """
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    else:
        return True


def check_repeated_characters(password: str) -> bool:
    """ Check if there are more than 2 cases of repeating characters

    :param password: password to check
    :return: check
    """
    idx = 0
    repetitions = 0
    while idx < len(password) - 1:
        first = ord(password[idx])
        second = ord(password[idx + 1])
        if first == second:
            repetitions += 1
            idx += 1
        idx += 1
    return repetitions > 1


def check_password(password: str) -> bool:
    """ Compute different checks

    :param password: password to check
    :return: check
    """
    return (
            check_increasing_characters(password) and
            check_forbidden_characters(password) and
            check_repeated_characters(password)
    )


def part_1(input_string: str) -> str:
    """ Code for the 1st part of the 11th day of Advent of Code

    :param input_string: input string
    :return: string result
    """
    new_password = increase_password(input_string)
    while not check_password(new_password):
        new_password = increase_password(new_password)
    return new_password


def part_2(input_string: str) -> str:
    """ Code for the 2nd part of the 11th day of Advent of Code

    :param input_string: input string
    :return: string result
    """
    new_password = input_string
    for _ in range(2):
        new_password = part_1(new_password)
    return new_password


def day_11(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 11th day we want to execute

    :param selected_part: selected Advent of Code part of the 11th day
    :param test: flag to use test input
    """
    input_digits = parse_single_line(11, is_test=test)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_digits)
        print('The result of 1st part of the 11th day of AoC is: ' + result_part_1)
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_digits)
        print('The result of 2nd part of the 11th day of AoC is: ' + result_part_2)
