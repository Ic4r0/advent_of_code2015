""" Day 17: No Such Thing as Too Much

Author: Ic4r0 - https://github.com/Ic4r0

Created: 11th December 2021
"""

# imports
from utils.parse_input import parse_by_line
from itertools import combinations


# modules
def part_1(input_list: list, is_test: bool) -> int:
    """ Code for the 1st part of the 17th day of Advent of Code

    :param input_list: input list
    :param is_test: flag to use test input
    :return: numeric result
    """
    eggnog_liters = 25 if is_test else 150
    combinations_list = []
    for comb_length in range(len(input_list)):
        combinations_list.extend(list(combinations(input_list, comb_length)))
    return len([combination for combination in combinations_list if sum(combination) == eggnog_liters])


def part_2(input_list: list, is_test: bool) -> int:
    """ Code for the 2nd part of the 17th day of Advent of Code

    :param input_list: input list
    :param is_test: flag to use test input
    :return: numeric result
    """
    eggnog_liters = 25 if is_test else 150
    combinations_list = []
    for comb_length in range(len(input_list)):
        combinations_list.extend(list(combinations(input_list, comb_length)))
    filtered_combinations = [len(combination) for combination in combinations_list if sum(combination) == eggnog_liters]
    return len(
        [1 for combination_length in filtered_combinations if combination_length == min(filtered_combinations)]
    )


def day_17(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 17th day we want to execute

    :param selected_part: selected Advent of Code part of the 17th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(17, is_test=test)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(input_list, test)
        print('The result of 1st part of the 17th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(input_list, test)
        print('The result of 2nd part of the 17th day of AoC is: ' + str(result_part_2))
