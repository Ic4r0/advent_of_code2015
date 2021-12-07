""" Day 7: Some Assembly Required

Author: Ic4r0 - https://github.com/Ic4r0

Created: 3rd December 2021
"""

# imports
from utils.parse_input import parse_by_line


# modules
def compute_wires_values(input_list: list) -> dict:
    """ Code used to compute each wire value from the input list

    :param input_list: input list
    :return: dict containing the value for each wire (key)
    """
    wires_values = dict()

    # Iterate over remaining input list to get all wires values
    while len(input_list) > 0:
        # Get numeric values of each wire
        idx_to_delete = []
        for idx, instruction in [row for row in enumerate(input_list)
                                 if (len(row[1]) == 3 and row[1][0].isnumeric()) or
                                    (len(row[1]) == 4 and row[1][1].isnumeric()) or
                                    (len(row[1]) == 5 and row[1][0].isnumeric() and row[1][2].isnumeric())]:
            if 'AND' in instruction:
                wires_values[instruction[-1]] = int(instruction[0]) & int(instruction[2])
            elif 'OR' in instruction:
                wires_values[instruction[-1]] = int(instruction[0]) | int(instruction[2])
            elif 'NOT' in instruction:
                wires_values[instruction[-1]] = ~int(instruction[1]) & 0xffff
            elif 'RSHIFT' in instruction:
                wires_values[instruction[-1]] = int(instruction[0]) >> int(instruction[2])
            elif 'LSHIFT' in instruction:
                wires_values[instruction[-1]] = int(instruction[0]) << int(instruction[2])
            else:
                wires_values[instruction[-1]] = int(instruction[0])
            idx_to_delete.append(idx)

        # Replace just fount numeric values in the input list
        for idx, instruction in [row for row in enumerate(input_list)
                                 if (len(set(wires_values.keys()).intersection(set(row[1]))) > 0 and
                                     row[0] not in idx_to_delete)]:
            if len(instruction) == 3:
                input_list[idx] = [
                    str(wires_values[instruction[0]]),
                    instruction[1],
                    instruction[2]
                ]
            if len(instruction) == 4:
                input_list[idx] = [
                    instruction[0],
                    str(wires_values[instruction[1]]),
                    instruction[2],
                    instruction[3]
                ]
            if len(instruction) == 5:
                input_list[idx] = [
                    instruction[0] if instruction[0] not in wires_values else str(wires_values[instruction[0]]),
                    instruction[1],
                    instruction[2] if instruction[2] not in wires_values else str(wires_values[instruction[2]]),
                    instruction[3],
                    instruction[4]
                ]

        idx_to_delete.reverse()
        for elem in idx_to_delete:
            del input_list[elem]

    return wires_values


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 7th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    wires_values = compute_wires_values(input_list)
    return wires_values['a']


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 7th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    prev_a_value = compute_wires_values(input_list[:])['a']
    new_b_value = [str(prev_a_value), '->', 'b']
    wires_values = compute_wires_values([elem if elem[-1] != 'b' else new_b_value for elem in input_list])
    return wires_values['a']


def day_7(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 7th day we want to execute

    :param selected_part: selected Advent of Code part of the 7th day
    :param test: flag to use test input
    """
    circuit = [line.split() for line in parse_by_line(7, int_list=False, is_test=test)]
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(circuit[:])
        print('The result of 1st part of the 7th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(circuit[:])
        print('The result of 1st part of the 7th day of AoC is: ' + str(result_part_2))
