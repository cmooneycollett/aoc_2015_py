"""
Solutions for AOC 2015 Day 23.
"""


from enum import Enum, auto, unique
import re


@unique
class Instruction(Enum):
    """
    Represents the different instructions that can be executed by Little Jane
    Marie's computer.
    """
    HALF = auto()
    TRIPLE = auto()
    INCREMENT = auto()
    JUMP = auto()
    JUMP_IF_EVEN = auto()
    JUMP_IF_ONE = auto()


def process_input_file():
    """
    Processes the AOC 2015 Day 23 input file into the format required by the
    solver functions. Returned value is a list containing the Instructions
    specified in the input file.
    """
    instructions = []
    regex_half = re.compile(r"hlf (a|b)")
    regex_triple = re.compile(r"tpl (a|b)")
    regex_increment = re.compile(r"inc (a|b)")
    regex_jump = re.compile(r"jmp ([-+]\d+)")
    regex_jump_if_even = re.compile(r"jie (a|b), ([-+]\d+)")
    regex_jump_if_one = re.compile(r"jio (a|b), ([-+]\d+)")
    with open("./input/day_23.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            if regex_half.match(line):
                match_half = regex_half.match(line)
                instruct = (Instruction.HALF, match_half.group(1))
                instructions.append(instruct)
            elif regex_triple.match(line):
                match_triple = regex_triple.match(line)
                instruct = (Instruction.TRIPLE, match_triple.group(1))
                instructions.append(instruct)
            elif regex_increment.match(line):
                match_increment = regex_increment.match(line)
                instruct = (Instruction.INCREMENT, match_increment.group(1))
                instructions.append(instruct)
            elif regex_jump.match(line):
                match_jump = regex_jump.match(line)
                instruct = (Instruction.JUMP, int(match_jump.group(1)))
                instructions.append(instruct)
            elif regex_jump_if_even.match(line):
                match_jump_if_even = regex_jump_if_even.match(line)
                instruct = (Instruction.JUMP_IF_EVEN,
                            match_jump_if_even.group(1),
                            int(match_jump_if_even.group(2)))
                instructions.append(instruct)
            elif regex_jump_if_one.match(line):
                match_jump_if_one = regex_jump_if_one.match(line)
                instruct = (Instruction.JUMP_IF_ONE, match_jump_if_one.group(1),
                            int(match_jump_if_one.group(2)))
                instructions.append(instruct)
    return instructions


def solve_part1(input_data):
    """
    Solves AOC 2015 Day 23 Part 1 // Processes the input instructions with "a"
    and "b" registers starting with value 0, returning the final value of the
    "b" register.
    """
    registers = {"a": 0, "b": 0}  # Registers
    process_instructions(input_data, registers)
    return registers["b"]


def solve_part2(input_data):
    """
    Solves AOC 2015 Day 23 Part 2 // Processes the input instructions with "a"
    register starting at 1 and "b" register starting at 0, returning the final
    value of the "b" register.
    """
    registers = {"a": 1, "b": 0}  # Registers
    process_instructions(input_data, registers)
    return registers["b"]


def process_instructions(instructions, registers):
    """
    Executes the given instructions and updates the values of the registers.
    """
    program_counter = 0
    while True:
        if program_counter < 0 or program_counter >= len(instructions):
            break
        match instructions[program_counter][0]:
            case Instruction.HALF:
                registers[instructions[program_counter][1]] /= 2
                program_counter += 1
            case Instruction.TRIPLE:
                registers[instructions[program_counter][1]] *= 3
                program_counter += 1
            case Instruction.INCREMENT:
                registers[instructions[program_counter][1]] += 1
                program_counter += 1
            case Instruction.JUMP:
                program_counter += instructions[program_counter][1]
            case Instruction.JUMP_IF_EVEN:
                if registers[instructions[program_counter][1]] % 2 == 0:
                    program_counter += instructions[program_counter][2]
                else:
                    program_counter += 1
            case Instruction.JUMP_IF_ONE:
                if registers[instructions[program_counter][1]] == 1:
                    program_counter += instructions[program_counter][2]
                else:
                    program_counter += 1
