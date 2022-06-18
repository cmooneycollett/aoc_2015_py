from enum import Enum, auto, unique
import re


@unique
class Instruction(Enum):
    HALF = auto()
    TRIPLE = auto()
    INCREMENT = auto()
    JUMP = auto()
    JUMP_IF_EVEN = auto()
    JUMP_IF_ONE = auto()


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    instructions = []
    regex_half = re.compile(r"hlf (a|b)")
    regex_triple = re.compile(r"tpl (a|b)")
    regex_increment = re.compile(r"inc (a|b)")
    regex_jump = re.compile(r"jmp ([-+]\d+)")
    regex_jump_if_even = re.compile(r"jie (a|b), ([-+]\d+)")
    regex_jump_if_one = re.compile(r"jio (a|b), ([-+]\d+)")
    with open("./inputs/day_23.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            if regex_half.match(line):
                m = regex_half.match(line)
                instruct = (Instruction.HALF, m.group(1))
                instructions.append(instruct)
            elif regex_triple.match(line):
                m = regex_triple.match(line)
                instruct = (Instruction.TRIPLE, m.group(1))
                instructions.append(instruct)
            elif regex_increment.match(line):
                m = regex_increment.match(line)
                instruct = (Instruction.INCREMENT, m.group(1))
                instructions.append(instruct)
            elif regex_jump.match(line):
                m = regex_jump.match(line)
                instruct = (Instruction.JUMP, int(m.group(1)))
                instructions.append(instruct)
            elif regex_jump_if_even.match(line):
                m = regex_jump_if_even.match(line)
                instruct = (Instruction.JUMP_IF_EVEN,
                            m.group(1), int(m.group(2)))
                instructions.append(instruct)
            elif regex_jump_if_one.match(line):
                m = regex_jump_if_one.match(line)
                instruct = (Instruction.JUMP_IF_ONE,
                            m.group(1), int(m.group(2)))
                instructions.append(instruct)
    return instructions


def solve_part1(input):
    registers = {"a": 0, "b": 0}  # Registers
    process_instructions(input, registers)
    return registers["b"]


def solve_part2(input):
    ()


def process_instructions(instructions, registers):
    """
    Executes the given instructions and updates the values of the registers.
    """
    pc = 0
    while True:
        if pc < 0 or pc >= len(instructions):
            break
        match instructions[pc][0]:
            case Instruction.HALF:
                registers[instructions[pc][1]] /= 2
                pc += 1
            case Instruction.TRIPLE:
                registers[instructions[pc][1]] *= 3
                pc += 1
            case Instruction.INCREMENT:
                registers[instructions[pc][1]] += 1
                pc += 1
            case Instruction.JUMP:
                pc += instructions[pc][1]
            case Instruction.JUMP_IF_EVEN:
                if registers[instructions[pc][1]] % 2 == 0:
                    pc += instructions[pc][2]
                else:
                    pc += 1
            case Instruction.JUMP_IF_ONE:
                if registers[instructions[pc][1]] == 1:
                    pc += instructions[pc][2]
                else:
                    pc += 1


if __name__ == "__main__":
    main()
