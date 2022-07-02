"""
Solutions for AOC 2015 Day 6.
"""


from enum import Enum, auto, unique
import re


@unique
class Instruction(Enum):
    """
    Instruction members represent the different instructions that can be used
    to operate on the light grid.
    """
    TURN_ON = auto()
    TURN_OFF = auto()
    TOGGLE = auto()


def process_input_file():
    """
    Processes the AOC 2015 Day 6 input file into the format required by the
    solver functions.
    """
    regex_on = re.compile(r"^(turn on) (\d+),(\d+) through (\d+),(\d+)$")
    regex_off = re.compile(r"^(turn off) (\d+),(\d+) through (\d+),(\d+)$")
    regex_toggle = re.compile(r"^(toggle) (\d+),(\d+) through (\d+),(\d+)$")
    input_data = []
    with open("./input/day_06.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            # On regex
            if (match_on := regex_on.match(line)) is not None:
                loc_x1 = int(match_on.group(2))
                loc_y1 = int(match_on.group(3))
                loc_x2 = int(match_on.group(4))
                loc_y2 = int(match_on.group(5))
                data = (Instruction.TURN_ON, loc_x1, loc_y1, loc_x2, loc_y2)
                input_data.append(data)
                continue
            # Off regex
            if (match_off := regex_off.match(line)):
                loc_x1 = int(match_off.group(2))
                loc_y1 = int(match_off.group(3))
                loc_x2 = int(match_off.group(4))
                loc_y2 = int(match_off.group(5))
                data = (Instruction.TURN_OFF, loc_x1, loc_y1, loc_x2, loc_y2)
                input_data.append(data)
            # Toggle regex
            if (match_toggle := regex_toggle.match(line)):
                loc_x1 = int(match_toggle.group(2))
                loc_y1 = int(match_toggle.group(3))
                loc_x2 = int(match_toggle.group(4))
                loc_y2 = int(match_toggle.group(5))
                data = (Instruction.TOGGLE, loc_x1, loc_y1, loc_x2, loc_y2)
                input_data.append(data)
    return input_data


def solve_part1(input_data):
    """
    Solves AOC 2015 Day 6 Part 1 // Modifies the state of the light grid
    (1000x1000 tiles, all tiles start off) by processing the input instructions.
    Returns how many lights are lit after following all instructions.
    """
    # Initialise lightgrid - all lights start as off
    lightgrid = [[False for _ in range(1000)] for _ in range(1000)]
    # Process each instruction
    for (instruction, loc_x1, loc_y1, loc_x2, loc_y2) in input_data:
        for loc_y in range(loc_y1, loc_y2 + 1):
            for loc_x in range(loc_x1, loc_x2 + 1):
                match instruction:
                    case Instruction.TURN_ON:
                        lightgrid[loc_y][loc_x] = True
                    case Instruction.TURN_OFF:
                        lightgrid[loc_y][loc_x] = False
                    case Instruction.TOGGLE:
                        lightgrid[loc_y][loc_x] = not lightgrid[loc_y][loc_x]
    # Count number of lights that are lit
    return sum(row.count(True) for row in lightgrid)


def solve_part2(input_data):
    """
    Solves AOC 2015 Day 6 Part 2 // Modifies the state of the light grid
    (1000x1000 grid, all tiles starting with brightness 0) by processing the
    input instructions (using Part 2 rules). Returns the total brightness of all
    lights after following all instructions.
    """
    # Initialise lightgrid - starting brightness 0 for all lights
    lightgrid = [[0 for _ in range(1000)] for _ in range(1000)]
    # Process each instruction
    for (instruction, loc_x1, loc_y1, loc_x2, loc_y2) in input_data:
        for loc_y in range(loc_y1, loc_y2 + 1):
            for loc_x in range(loc_x1, loc_x2 + 1):
                match(instruction):
                    case Instruction.TURN_ON:
                        lightgrid[loc_y][loc_x] += 1
                    case Instruction.TURN_OFF:
                        lightgrid[loc_y][loc_x] -= 1
                    case Instruction.TOGGLE:
                        lightgrid[loc_y][loc_x] += 2
                # Ensure brightness is kept at or above 0
                if lightgrid[loc_y][loc_x] < 0:
                    lightgrid[loc_y][loc_x] = 0
    # Count total brightness of all lights
    return sum(sum(row) for row in lightgrid)
