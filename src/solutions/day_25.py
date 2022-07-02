"""
Solutions for AOC 2015 Day 25.
"""


import re


def process_input_file():
    """
    Processes the AOC 2015 Day 25 input file into format for solver functions.
    """
    regex_grid = re.compile(r"row (\d+), column (\d+)")
    with open("./input/day_25.txt", encoding="utf-8") as file:
        raw_input = file.read().strip()
        r_match = regex_grid.search(raw_input)
        return (int(r_match.group(1)), int(r_match.group(2)))


def solve_part1(input_data):
    """
    Calculates the code required to start-up the weather machine.
    """
    (row, column) = input_data
    # First stage
    seq = sum(range(1, column + 1))    # Initially the column top value
    increment = column
    for _ in range(1, row):
        seq += increment
        increment += 1
    # Second stage
    code = 20151125  # Value in grid at r,c (1,1)
    for _ in range(1, seq):
        code *= 252533
        code %= 33554393
    return code


def solve_part2(_):
    """
    No solution required for AOC 2015 Day 25 Part 2 - Christmas has been saved!
    """
    return ()
