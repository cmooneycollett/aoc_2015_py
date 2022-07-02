"""
Solutions for AOC 2015 Day 1.
"""


def process_input_file():
    """
    Processes the AOC 2015 Day 1 input file into format for solvers.
    """
    with open("./input/day_01.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_data):
    """
    Solves AOC 2015 Day 1 Part 1 // alculates the final floor result from
    processing the input instructions.
    """
    floor = 0
    for char in input_data:
        if char == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def solve_part2(input_data):
    """
    Solves AOC 2015 Day 1 Part 2 // Calculates the location of the input
    character that causes Santa to first enter the basement floor.
    """
    pos = 1
    floor = 0
    for char in input_data:
        if char == '(':
            floor += 1
        else:
            floor -= 1
        # Break if the basement level has been reached
        if floor == -1:
            break
        # Continue to the next character
        pos += 1
    return pos
