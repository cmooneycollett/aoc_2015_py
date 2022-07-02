"""
Solutions for AOC 2015 Day 2.
"""


import re


def process_input_file():
    """
    Processes the AOC 2015 Day 2 input file into the format required by the
    solver functions. Returned value is a list containing the dimensions of the
    presents specified in the input file.
    """
    with open("./input/day_02.txt", encoding="utf-8") as file:
        raw_input = file.read().strip()
        input_data = []
        regex = re.compile(r"(\d+)x(\d+)x(\d+)")
        for line in raw_input.splitlines():
            if len(line := line.strip()) == 0:
                continue
            match_line = regex.match(line)
            length = int(match_line.group(1))
            width = int(match_line.group(2))
            height = int(match_line.group(3))
            input_data.append((length, width, height))
        return input_data


def solve_part1(input_data):
    """
    Solves AOC 2015 Day 2 Part 1 // Calculates the total square feet of wrapping
    paper required to wrap the presents specified in input.
    """
    total_paper = 0  # unit: square feet
    for (length, width, height) in input_data:
        side_areas = [length * width, length * height, width * height]
        slack = min(side_areas)
        total_paper += 2 * sum(side_areas) + slack
    return total_paper


def solve_part2(input_data):
    """
    Solves AOC 2015 Day 2 Part 2 // Calculates the total length of ribbon in
    feet required to wrap the presents specified in input.
    """
    total_ribbon = 0    # unit: feet
    for (length, width, height) in input_data:
        perimeters = [2 * (length + width), 2 * (length + height),
                      2 * (width + height)]  # for each face
        volume = length * width * height
        ribbon = min(perimeters) + volume
        total_ribbon += ribbon
    return total_ribbon
