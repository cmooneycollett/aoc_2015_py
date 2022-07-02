"""
Solutions for AOC 2015 Day 1.
"""


def process_input_file():
    """
    Processes the AOC 2015 Day 1 input file into the format required by the
    solver functions. Returned value is the string of floor movement
    instructions specified in the input file.
    """
    with open("./input/day_01.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_data):
    """
    Solves AOC 2015 Day 1 Part 1 // Calculates the final floor result from
    processing the input instructions.
    """
    floor = 0   # Begin at ground floor
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
    position = 1    # First character in the instructions has "position" 1
    floor = 0       # Begin at ground floor
    for char in input_data:
        if char == '(':
            floor += 1
        else:
            floor -= 1
        # Break if the basement level has been reached
        if floor == -1:
            break
        # Continue to the next character
        position += 1
    return position
