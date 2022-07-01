"""
Solutions for AOC 2015 Day 2.
"""


import re


def process_input_file():
    """
    Processes the AOC 2015 Day 2 input file into format for solver functions.
    """
    with open("./input/day_02.txt", encoding="utf-8") as file:
        raw_input = file.read().strip()
        input_data = []
        regex = re.compile(r"(\d+)x(\d+)x(\d+)")
        for line in raw_input.splitlines():
            line = line.strip()
            if len(line) == 0:
                continue
            match_r = regex.match(line)
            line_data = (int(match_r.group(1)), int(match_r.group(2)),
                         int(match_r.group(3)))
            input_data.append(line_data)
        return input_data


def solve_part1(input_data):
    """
    Calculates the total square feet of wrapping paper required to wrap the
    presents specified in input.
    """
    total_paper = 0  # unit: square feet
    for data in input_data:
        side_areas = [data[0] * data[1], data[0] * data[2], data[1] * data[2]]
        slack = min(side_areas)
        total_paper += 2 * sum(side_areas) + slack
    return total_paper


def solve_part2(input_data):
    """
    Calculates the total length of ribbon in feet required to wrap the presents
    specified in input.
    """
    total_ribbon = 0    # unit: feet
    for data in input_data:
        side_perims = [2 * (data[0] + data[1]), 2 *
                       (data[0] + data[2]), 2 * (data[1] + data[2])]
        volume = data[0] * data[1] * data[2]
        ribbon = min(side_perims) + volume
        total_ribbon += ribbon
    return total_ribbon
