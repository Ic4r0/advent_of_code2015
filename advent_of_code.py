""" Main file for the advent_of_code2015 repository

To use this run 'python advent_of_code *test* *day* *part*', where test is an optional flag used to
test the code for a chosen day, day is an integer number between 1 and 25, and part is an optional
integer number between 1 and 2

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd December 2021
"""

# imports
import sys

from utils.validators import check_valid_arguments
from days.day_1 import day_1
from days.day_2 import day_2


# module
def save_xmas(selected_day: int, selected_part: int = None, is_test: bool = False):
    """ Needed to select the correct module corresponding to the selected day

    :param selected_day: selected Advent of Code day
    :param selected_part: selected Advent of Code part of the selected day
    :param is_test: flag to use test input
    """
    if selected_day == 1:
        day_1(selected_part, is_test)
    elif selected_day == 2:
        day_2(selected_part, is_test)
    elif 0 < selected_day < 26:
        print('No available solution for the selected day')
    else:
        print('Choose a day between 1 and 25')


if __name__ == "__main__":
    test = False
    day = None
    part = None

    arguments = check_valid_arguments(sys.argv[1:])
    if arguments:
        test, day, part = arguments
        save_xmas(day, part, test)
    else:
        print('To use this run \'python advent_of_code *test* *day* *part*\', where test is an optional flag used to '
              'test the code for a chosen day, day is an integer number between 1 and 25, and part is an optional '
              'integer number between 1 and 2')
