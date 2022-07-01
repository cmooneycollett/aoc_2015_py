"""
Solutions for AOC 2015 Day 15.
"""


import re
from dataclasses import dataclass


@dataclass
class Ingredient:
    """
    Dataclass used to represent one of the possible cookie ingredients.
    """
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def process_input_file():
    """
    Processes the AOC 2015 Day 15 input file into the format required by the
    solver functions. Returned data structure is a list of the ingredient
    objects specified in the input file.
    """
    input_data = {}
    regex_ingredient = re.compile(
        r"^([a-zA-Z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), "
        r"texture (-?\d+), calories (-?\d+)$")
    with open("./input/day_15.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            # Extract ingredient parameters from input file line
            match_ingredient = regex_ingredient.match(line)
            name = match_ingredient.group(1)
            capacity = int(match_ingredient.group(2))
            durability = int(match_ingredient.group(3))
            flavor = int(match_ingredient.group(4))
            texture = int(match_ingredient.group(5))
            calories = int(match_ingredient.group(6))
            ingredient = Ingredient(
                name, capacity, durability, flavor, texture, calories)
            input_data[name] = ingredient
    return input_data


def solve_part1(input_data):
    """
    Finds the total score for the highest-scoring cookie by combining the input
    ingredients, using exactly 100 units (tsp) of ingredients total.
    """
    return calculate_optimal_cookie_score(input_data)


def solve_part2(input_data):
    """
    Finds the total score for the highest-scoring cookie with exactly 500
    calories by combining the input ingredients, using exactly 100 units (tsp)
    of ingredients total.
    """
    return calculate_optimal_cookie_score(input_data, calorie_req=500)


def calculate_optimal_cookie_score(ingredients, calorie_req=None):
    """
    Finds the total score for the highest-scoring cookie (with exact calorie
    requirement if specified) by combining the input ingredients, using exactly
    100 units (tsp) of ingredients total.
    """
    max_cookie_score = None
    for q_sprinkles in range(0, 100):
        for q_peanutbutter in range(0, 100 - q_sprinkles):
            for q_frosting in range(0, 100 - q_sprinkles - q_peanutbutter):
                q_sugar = 100 - q_sprinkles - q_peanutbutter - q_frosting
                # Check calorie total
                if calorie_req is not None:
                    calories = ingredients["Sprinkles"].calories * q_sprinkles + \
                        ingredients["PeanutButter"].calories * q_peanutbutter + \
                        ingredients["Frosting"].calories * q_frosting + \
                        ingredients["Sugar"].calories * q_sugar
                    if calories != calorie_req:
                        continue
                # Calculate cookie property scores
                capacity = ingredients["Sprinkles"].capacity * q_sprinkles + \
                    ingredients["PeanutButter"].capacity * q_peanutbutter + \
                    ingredients["Frosting"].capacity * q_frosting + \
                    ingredients["Sugar"].capacity * q_sugar
                durability = ingredients["Sprinkles"].durability * q_sprinkles + \
                    ingredients["PeanutButter"].durability * q_peanutbutter + \
                    ingredients["Frosting"].durability * q_frosting + \
                    ingredients["Sugar"].durability * q_sugar
                flavour = ingredients["Sprinkles"].flavor * q_sprinkles + \
                    ingredients["PeanutButter"].flavor * q_peanutbutter + \
                    ingredients["Frosting"].flavor * q_frosting + \
                    ingredients["Sugar"].flavor * q_sugar
                texture = ingredients["Sprinkles"].texture * q_sprinkles + \
                    ingredients["PeanutButter"].texture * q_peanutbutter + \
                    ingredients["Frosting"].texture * q_frosting + \
                    ingredients["Sugar"].texture * q_sugar
                # Calculate cookie score and update maximum value if required
                cookie_score = 0
                if capacity > 0 and durability > 0 and flavour > 0 and \
                        texture > 0:
                    cookie_score = capacity * durability * \
                        flavour * texture
                if max_cookie_score is None or cookie_score > max_cookie_score:
                    max_cookie_score = cookie_score
    return max_cookie_score
