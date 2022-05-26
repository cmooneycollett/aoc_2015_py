from enum import Enum, auto, unique
import re


@unique
class Instruction(Enum):
    TURN_ON = auto()
    TURN_OFF = auto()
    TOGGLE = auto()


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    p2_solution = solve_part2(input)
    print("P1 solution - {}".format(p1_solution))
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    regex_on = re.compile(r"^(turn on) (\d+),(\d+) through (\d+),(\d+)$")
    regex_off = re.compile(r"^(turn off) (\d+),(\d+) through (\d+),(\d+)$")
    regex_toggle = re.compile(r"^(toggle) (\d+),(\d+) through (\d+),(\d+)$")
    input = []
    with open("./inputs/day_06.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            # On regex
            m_on = regex_on.match(line)
            if m_on:
                x1 = int(m_on.group(2))
                y1 = int(m_on.group(3))
                x2 = int(m_on.group(4))
                y2 = int(m_on.group(5))
                data = (Instruction.TURN_ON, x1, y1, x2, y2)
                input.append(data)
                continue
            # Off regex
            m_off = regex_off.match(line)
            if m_off:
                x1 = int(m_off.group(2))
                y1 = int(m_off.group(3))
                x2 = int(m_off.group(4))
                y2 = int(m_off.group(5))
                data = (Instruction.TURN_OFF, x1, y1, x2, y2)
                input.append(data)
            # Toggle regex
            m_tog = regex_toggle.match(line)
            if m_tog:
                x1 = int(m_tog.group(2))
                y1 = int(m_tog.group(3))
                x2 = int(m_tog.group(4))
                y2 = int(m_tog.group(5))
                data = (Instruction.TOGGLE, x1, y1, x2, y2)
                input.append(data)
    return input


def solve_part1(input):
    # Initialise grid to track light states
    lightgrid = [[False for x in range(1000)] for x in range(1000)]
    # Process each instruction
    for (instruct, x1, y1, x2, y2) in input:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                match instruct:
                    case Instruction.TURN_ON:
                        lightgrid[j][i] = True
                    case Instruction.TURN_OFF:
                        lightgrid[j][i] = False
                    case Instruction.TOGGLE:
                        lightgrid[j][i] = not lightgrid[j][i]
    # Count number of lights that are lit
    count = 0
    for i in range(1000):
        for j in range(1000):
            if lightgrid[j][i] is True:
                count += 1
    return count


def solve_part2(input):
    # Initialise lightgrid
    lightgrid = [[0 for x in range(1000)] for x in range(1000)]
    # Process each instruction
    for (instruct, x1, y1, x2, y2) in input:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                match(instruct):
                    case Instruction.TURN_ON:
                        lightgrid[j][i] += 1
                    case Instruction.TURN_OFF:
                        lightgrid[j][i] -= 1
                    case Instruction.TOGGLE:
                        lightgrid[j][i] += 2
                # Ensure brightness is kept at or above 0
                if lightgrid[j][i] < 0:
                    lightgrid[j][i] = 0
    # Count total brightness of all lights
    total_brightness = 0
    for i in range(1000):
        for j in range(1000):
            total_brightness += lightgrid[j][i]
    return total_brightness


if __name__ == "__main__":
    main()
