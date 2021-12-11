""" Day 18: Like a GIF For Your Yard

Author: Ic4r0 - https://github.com/Ic4r0

Created: 11th December 2021
"""

# imports
from utils.parse_input import parse_by_line
from os import system
from time import sleep


# modules
def pretty_print(input_list: list):
    """ Pretty print the lights grid

    :param input_list: input list
    """
    sleep(0.2)
    system('cls||clear')
    for y in range(len(input_list)):
        print(''.join(input_list[y]))


def neighbors_state(input_list: list, current_coords: tuple) -> int:
    """ Return numbers of on neighbors at current coordinates

    :param input_list: input list
    :param current_coords: current coordinates
    :return: on neighbors
    """
    on_lights = 0
    x_max = len(input_list[0])
    y_max = len(input_list)
    y, x = current_coords
    possible_neighbors = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
    for y_neigh, x_neigh in possible_neighbors:
        if 0 <= y_neigh < y_max and 0 <= x_neigh < x_max and input_list[y_neigh][x_neigh] == '#':
            on_lights += 1

    return on_lights


def compute_coords_state(input_list: list, current_coords: tuple) -> str:
    """ Get new coordinate state

    :param input_list: input list
    :param current_coords: current coordinates
    :return: new state
    """
    y, x = current_coords
    current_state = input_list[y][x]
    on = neighbors_state(input_list, current_coords)
    if current_state == '#':
        return '#' if on in [2, 3] else '.'
    else:
        return '#' if on == 3 else '.'


def part_1(input_list: list, is_test: bool) -> int:
    """ Code for the 1st part of the 18th day of Advent of Code

    :param input_list: input list
    :param is_test: flag to use test input
    :return: numeric result
    """
    n_steps = 4 if is_test else 100
    # pretty_print(input_list)
    for step in range(n_steps):
        input_list = [
            [
                compute_coords_state(input_list, (y, x))
                for x in range(len(input_list[0]))
            ]
            for y in range(len(input_list))
        ]
        # pretty_print(input_list)

    return len([1 for x in range(len(input_list[0])) for y in range(len(input_list)) if input_list[y][x] == '#'])


def part_2(input_list: list, is_test: bool) -> int:
    """ Code for the 2nd part of the 18th day of Advent of Code

    :param input_list: input list
    :param is_test: flag to use test input
    :return: numeric result
    """
    n_steps = 5 if is_test else 100
    x_max = len(input_list[0])
    y_max = len(input_list)
    corners = [(0, 0), (0, x_max-1), (y_max-1, 0), (y_max-1, x_max-1)]
    input_list = [
        [
            input_list[y][x]
            if (y, x) not in corners
            else '#'
            for x in range(len(input_list[0]))
        ]
        for y in range(len(input_list))
    ]
    # pretty_print(input_list)
    for step in range(n_steps):
        input_list = [
            [
                compute_coords_state(input_list, (y, x))
                if (y, x) not in corners
                else '#'
                for x in range(len(input_list[0]))
            ]
            for y in range(len(input_list))
        ]
        # pretty_print(input_list)

    return len([1 for x in range(len(input_list[0])) for y in range(len(input_list)) if input_list[y][x] == '#'])


def day_18(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 18th day we want to execute

    :param selected_part: selected Advent of Code part of the 18th day
    :param test: flag to use test input
    """
    lights = [list(line) for line in parse_by_line(18, int_list=False, is_test=test)]

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(lights[:], test)
        print('The result of 1st part of the 11th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(lights[:], test)
        print('The result of 2nd part of the 11th day of AoC is: ' + str(result_part_2))
