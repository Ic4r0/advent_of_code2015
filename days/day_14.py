""" Day 14: Reindeer Olympics

Author: Ic4r0 - https://github.com/Ic4r0

Created: 10th December 2021
"""

# imports
from utils.parse_input import parse_by_line
from re import match


# modules
def compute_space(reindeer: dict, max_time: int) -> int:
    """ Compute traveled distance of a single reindeer

    :param reindeer: dict containing info about reindeer
    :param max_time: observation period
    :return: numeric result
    """
    distance = 0
    time = 0
    while time < max_time:
        if time + reindeer['time'] > max_time:
            distance += (max_time - time) * reindeer['speed']
        else:
            distance += reindeer['time'] * reindeer['speed']
        time += reindeer['time'] + reindeer['rest']
    return distance


def part_1(reindeer: dict, is_test: bool) -> int:
    """ Code for the 1st part of the 14th day of Advent of Code

    :param reindeer: dict containing info about reindeer
    :param is_test: flag to use test max_time
    :return: numeric result
    """
    max_time = 1000 if is_test else 2503
    distances = []
    for single_reindeer in reindeer.keys():
        distances.append(compute_space(reindeer[single_reindeer], max_time))
    return max(distances)


def part_2(reindeer: dict, is_test: bool) -> int:
    """ Code for the 2nd part of the 14th day of Advent of Code

    :param reindeer: dict containing info about reindeer
    :param is_test: flag to use test max_time
    :return: numeric result
    """
    max_time = 1000 if is_test else 2503
    reindeer_list = reindeer.keys()
    points = {single_reindeer: 0 for single_reindeer in reindeer_list}
    for second in range(1, max_time):
        results_by_seconds = []
        for single_reindeer in reindeer_list:
            results_by_seconds.append(compute_space(reindeer[single_reindeer], second))
        max_values_names = [
            list(reindeer_list)[idx] for idx, result in enumerate(results_by_seconds)
            if result == max(results_by_seconds)
        ]
        for name in max_values_names:
            points[name] += 1

    return max(points.values())


def day_14(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 14th day we want to execute

    :param selected_part: selected Advent of Code part of the 14th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(14, int_list=False, is_test=test)
    reindeer = dict()
    for line in input_list:
        matches = match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
        name, speed, time, rest = matches.groups()
        reindeer[name] = {
            'speed': int(speed),
            'time': int(time),
            'rest': int(rest),
        }

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(reindeer, is_test=test)
        print('The result of 1st part of the 14th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(reindeer, is_test=test)
        print('The result of 2nd part of the 14th day of AoC is: ' + str(result_part_2))
