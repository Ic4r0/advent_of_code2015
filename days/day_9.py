""" Day 9: All in a Single Night

Author: Ic4r0 - https://github.com/Ic4r0

Created: 7th December 2021
"""

# imports
from utils.parse_input import parse_by_line
from re import match
from itertools import permutations


# modules
def part_1(locations: list, distances: dict) -> int:
    """ Code for the 1st part of the 9th day of Advent of Code

    :param locations: destination list
    :param distances: distances between destinations
    :return: numeric result
    """
    permutations_list = permutations(locations)
    possible_distances = []
    for route in permutations_list:
        current_distance = 0
        for idx in range(len(route) - 1):
            current_distance += distances[route[idx]][route[idx + 1]]
        possible_distances.append(current_distance)
    return min(possible_distances)


def part_2(locations: list, distances: dict) -> int:
    """ Code for the 2nd part of the 9th day of Advent of Code

    :param locations: destination list
    :param distances: distances between destinations
    :return: numeric result
    """
    permutations_list = permutations(locations)
    possible_distances = []
    for route in permutations_list:
        current_distance = 0
        for idx in range(len(route) - 1):
            current_distance += distances[route[idx]][route[idx + 1]]
        possible_distances.append(current_distance)
    return max(possible_distances)


def day_9(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 9th day we want to execute

    :param selected_part: selected Advent of Code part of the 9th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(9, int_list=False, is_test=test)
    distances = dict()
    locations = []
    for row in input_list:
        regex_match = match(r'^(\w+) to (\w+) = (\d+)$', row)
        dest1, dest2, dist = regex_match.groups()
        if dest1 not in distances:
            distances[dest1] = dict()
        if dest2 not in distances:
            distances[dest2] = dict()
        distances[dest1][dest2] = int(dist)
        distances[dest2][dest1] = int(dist)
        if dest1 not in locations:
            locations.append(dest1)
        if dest2 not in locations:
            locations.append(dest2)

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(locations, distances)
        print('The result of 1st part of the 9th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(locations, distances)
        print('The result of 2nd part of the 9th day of AoC is: ' + str(result_part_2))
