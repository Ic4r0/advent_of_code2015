""" Day 15: Science for Hungry People

Author: Ic4r0 - https://github.com/Ic4r0

Created: 10th December 2021
"""

# imports
from utils.parse_input import parse_by_line
from re import match
from functools import reduce
import operator


# modules
def compute_scores(ingredients: dict) -> list:
    """ Compute scores for each possible recipe

    :param ingredients: dict containing info about ingredients
    :return: list of tuple containing (total score, calories)
    """
    ingredients_names = list(ingredients.keys())
    scores = []
    for a in range(0, 101):
        for b in range(0, 101-a):
            for c in range(0, 101-a-b):
                d = 100 - a - b - c
                score = {
                    'capacity': 0,
                    'durability': 0,
                    'flavor': 0,
                    'texture': 0,
                }
                calories = 0
                teaspoons = [a, b, c, d]
                for idx in range(len(ingredients_names)):
                    name = ingredients_names[idx]
                    teaspoon = teaspoons[idx]
                    score['capacity'] += teaspoon * ingredients[name]['capacity']
                    score['durability'] += teaspoon * ingredients[name]['durability']
                    score['flavor'] += teaspoon * ingredients[name]['flavor']
                    score['texture'] += teaspoon * ingredients[name]['texture']
                    calories += teaspoon * ingredients[name]['calories']
                if any([value < 0 for value in score.values()]):
                    scores.append((0, calories))
                else:
                    scores.append((reduce(operator.mul, score.values(), 1), calories))

    return scores


def part_1(ingredients: dict) -> int:
    """ Code for the 1st part of the 15th day of Advent of Code

    :param ingredients: dict containing info about ingredients
    :return: numeric result
    """
    return max([score for score, _ in compute_scores(ingredients)])


def part_2(ingredients: dict) -> int:
    """ Code for the 2nd part of the 15th day of Advent of Code

    :param ingredients: dict containing info about ingredients
    :return: numeric result
    """
    return max([score for score, calories in compute_scores(ingredients) if calories == 500])


def day_15(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 15th day we want to execute

    :param selected_part: selected Advent of Code part of the 15th day
    :param test: flag to use test input
    """
    input_list = parse_by_line(15, int_list=False, is_test=test)
    ingredients = dict()
    for line in input_list:
        matches = match(
            r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)',
            line
        )
        name, capacity, durability, flavor, texture, calories = matches.groups()
        ingredients[name] = {
            'capacity': int(capacity),
            'durability': int(durability),
            'flavor': int(flavor),
            'texture': int(texture),
            'calories': int(calories),
        }

    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(ingredients)
        print('The result of 1st part of the 15th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(ingredients)
        print('The result of 2nd part of the 15th day of AoC is: ' + str(result_part_2))
