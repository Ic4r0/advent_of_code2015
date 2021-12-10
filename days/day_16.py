""" Day 16: Aunt Sue

Author: Ic4r0 - https://github.com/Ic4r0

Created: 10th December 2021
"""

# imports
from utils.parse_input import parse_by_line
from re import findall


# modules
def part_1(sue_info: dict) -> int:
    """ Code for the 1st part of the 16th day of Advent of Code

    :param sue_info: dict containing info about different Sue
    :return: numeric result
    """
    mfcsam = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }
    detected_sue = 0
    for n_sue, info in sue_info.items():
        is_ok = True
        for item, value in mfcsam.items():
            selected_sue_value = info.get(item, -1)
            if selected_sue_value == -1:
                continue
            elif selected_sue_value == value:
                continue
            else:
                is_ok = False
                break
        if is_ok:
            detected_sue = n_sue
            break
    return detected_sue


def part_2(sue_info: dict) -> int:
    """ Code for the 2nd part of the 16th day of Advent of Code

    :param sue_info: dict containing info about different Sue
    :return: numeric result
    """
    mfcsam = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }
    detected_sue = 0
    for n_sue, info in sue_info.items():
        is_ok = True
        for item, value in mfcsam.items():
            selected_sue_value = info.get(item, -1)
            if selected_sue_value == -1:
                continue
            elif item in ['cats', 'trees'] and value < selected_sue_value:
                continue
            elif item in ['pomeranians', 'goldfish'] and value > selected_sue_value:
                continue
            elif item not in ['cats', 'trees', 'pomeranians', 'goldfish'] and selected_sue_value == value:
                continue
            else:
                is_ok = False
                break
        if is_ok:
            detected_sue = n_sue
            break
    return detected_sue


def day_16(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 16th day we want to execute

    :param selected_part: selected Advent of Code part of the 16th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(16, int_list=False, is_test=test)
    sue_info = dict()
    for idx, line in enumerate(input_list):
        matches = findall(r'(\w+): (\d+)', line)
        sue_info[idx + 1] = dict()
        for thing, value in matches:
            sue_info[idx + 1][thing] = int(value)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(sue_info)
        print('The result of 1st part of the 16th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(sue_info)
        print('The result of 2nd part of the 16th day of AoC is: ' + str(result_part_2))
