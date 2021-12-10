""" Day 13: Knights of the Dinner Table

Author: Ic4r0 - https://github.com/Ic4r0

Created: 10th December 2021
"""

# imports
from utils.parse_input import parse_by_line
from re import match
from itertools import permutations


# modules
def compute_total_happiness(potential_happiness: dict, arrangement: tuple) -> int:
    """ Compute total happiness for a specific arrangement

    :param potential_happiness: dict containing info about potential happiness
    :param arrangement: arrangement of people
    :return: total happiness
    """
    happiness_sum = 0
    for idx, person in enumerate(arrangement):
        if idx == 0:
            happiness_1 = potential_happiness[person][arrangement[-1]]
            happiness_2 = potential_happiness[person][arrangement[idx+1]]
        elif idx == len(arrangement) - 1:
            happiness_1 = potential_happiness[person][arrangement[idx-1]]
            happiness_2 = potential_happiness[person][arrangement[0]]
        else:
            happiness_1 = potential_happiness[person][arrangement[idx-1]]
            happiness_2 = potential_happiness[person][arrangement[idx+1]]
        happiness_sum += happiness_1 + happiness_2
    return happiness_sum


def part_1(potential_happiness: dict) -> int:
    """ Code for the 1st part of the 13th day of Advent of Code

    :param potential_happiness: dict containing info about potential happiness
    :return: numeric result
    """
    seating_arrangements = permutations(potential_happiness.keys())
    total_change_happiness = []
    for arrangement in seating_arrangements:
        total_change_happiness.append(compute_total_happiness(potential_happiness, arrangement))
    return max(total_change_happiness)


def part_2(potential_happiness: dict) -> int:
    """ Code for the 2nd part of the 13th day of Advent of Code

    :param potential_happiness: dict containing info about potential happiness
    :return: numeric result
    """
    guests = potential_happiness.keys()
    potential_happiness['Me'] = dict()
    for guest in guests:
        potential_happiness[guest]['Me'] = 0
        potential_happiness['Me'][guest] = 0
    seating_arrangements = permutations(potential_happiness.keys())
    total_change_happiness = []
    for arrangement in seating_arrangements:
        total_change_happiness.append(compute_total_happiness(potential_happiness, arrangement))
    return max(total_change_happiness)


def day_13(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 13th day we want to execute

    :param selected_part: selected Advent of Code part of the 13th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(13, int_list=False, is_test=test)
    potential_happiness = dict()
    for line in input_list:
        matches = match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).', line)
        name_1, sign, value, name_2 = matches.groups()
        if name_1 not in potential_happiness:
            potential_happiness[name_1] = dict()
        potential_happiness[name_1][name_2] = int(value) if sign == 'gain' else -1 * int(value)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(potential_happiness)
        print('The result of 1st part of the 13th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(potential_happiness)
        print('The result of 2nd part of the 13th day of AoC is: ' + str(result_part_2))
