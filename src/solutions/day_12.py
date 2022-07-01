"""
Solutions for AOC 2015 Day 12.
"""


import json
import re


def process_input_file():
    """
    Processes the AOC 2015 Day 12 input file into the format required by the
    solver functions.
    """
    with open("./input/day_12.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_data):
    """
    Calculates the total of all numbers discovered in the json data serialised
    in input.
    """
    # Extract all numbers from the input json string.
    numbers_raw = re.findall(r"-?\d+", input_data)
    return sum(int(n) for n in numbers_raw)


def solve_part2(input_data):
    """
    Calculates the total of all valid numbers (not within a json object
    containing a value of \"red\") discovered in the json data serialised in
    input.
    """
    numbers_valid = []
    json_data = json.loads(input_data)
    # Discover all valid numbers within the json data
    discover_valid_numbers(numbers_valid, json_data)
    # Return the total of all valid numbers
    return sum(numbers_valid)


def discover_valid_numbers(numbers_valid, obj):
    """
    Find all valid numbers (i.e. not within a python dict (json object)
    containing a value of \"red\") by recursively inspecting each object and
    value discovered. String values are ignored because they do not contain
    valid numbers, other values or data structures with their own values.
    """
    # Handle cases for int, list and dict - str values are ignored
    if isinstance(obj, int):
        numbers_valid.append(obj)
    elif isinstance(obj, list):
        for sub_obj in obj:
            if isinstance(sub_obj, int):
                numbers_valid.append(sub_obj)
            elif isinstance(sub_obj, list) or isinstance(sub_obj, dict):
                discover_valid_numbers(numbers_valid, sub_obj)
    elif isinstance(obj, dict):
        # Check for invalid object
        if "red" in obj.values():
            return
        for sub_obj in obj.values():
            if isinstance(sub_obj, int):
                numbers_valid.append(sub_obj)
            elif isinstance(sub_obj, list) or isinstance(sub_obj, dict):
                discover_valid_numbers(numbers_valid, sub_obj)
