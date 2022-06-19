"""
Solutions for AOC 2015 Day 7.
"""

import copy
import re
from enum import Enum, auto, unique


@unique
class Operation(Enum):
    """
    Operation enum members represent the different logical operations present
    across the bitwise logic gates encountered in the problem.
    """
    OP_VALUE = auto()   # Input value given or from wire (not modified)
    OP_AND = auto()     # Bit-wise AND of two values fed to next wire
    OP_LSHIFT = auto()  # Left shift the "left" values by "right" places
    OP_NOT = auto()     # Bitwise NOT of one value fed to next wire
    OP_OR = auto()      # Bit-wise OR or one value fed to next wire
    OP_RSHIFT = auto()  # Right shift the "left" value by "right" places


def main():
    """
    Solves AOC 2015 Day 7 Parts 1 and 2, printing out the results.
    """
    input_p = process_input_file()
    p1_solution = solve_part1(input_p)
    print(f"P1 solution - {p1_solution}")
    p2_solution = solve_part2(input_p)
    print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2015 Day 7 input file into the format required by the
    solver functions.
    """
    input_processed = {}
    regex_op_value = re.compile(r"^([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_and = re.compile(r"^([a-z]+|\d+) AND ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_lshift = re.compile(
        r"^([a-z]+|\d+) LSHIFT ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_not = re.compile(r"^NOT ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_or = re.compile(r"^([a-z]+|\d+) OR ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_rshift = re.compile(
        r"^([a-z]+|\d+) RSHIFT ([a-z]+|\d+) -> ([a-z]+)$")
    with open("./inputs/day_07.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            if regex_op_value.match(line):
                m_value = regex_op_value.match(line)
                value = m_value.group(1)
                output = m_value.group(2)
                if value.isnumeric():
                    value = int(value)
                input_processed[output] = (Operation.OP_VALUE, value)
            elif regex_op_and.match(line):
                match_and = regex_op_and.match(line)
                left = match_and.group(1)
                right = match_and.group(2)
                output = match_and.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input_processed[output] = (Operation.OP_AND, left, right)
            elif regex_op_lshift.match(line):
                match_lshift = regex_op_lshift.match(line)
                left = match_lshift.group(1)
                right = match_lshift.group(2)
                output = match_lshift.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input_processed[output] = (Operation.OP_LSHIFT, left, right)
            elif regex_op_not.match(line):
                match_not = regex_op_not.match(line)
                value = match_not.group(1)
                output = match_not.group(2)
                if value.isnumeric():
                    value = int(value)
                input_processed[output] = (Operation.OP_NOT, value)
            elif regex_op_or.match(line):
                match_or = regex_op_or.match(line)
                left = match_or.group(1)
                right = match_or.group(2)
                output = match_or.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input_processed[output] = (Operation.OP_OR, left, right)
            elif regex_op_rshift.match(line):
                match_rshift = regex_op_rshift.match(line)
                left = match_rshift.group(1)
                right = match_rshift.group(2)
                output = match_rshift.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input_processed[output] = (Operation.OP_RSHIFT, left, right)
    return input_processed


def solve_part1(input_p):
    """
    Evaluates the inputs to the wire system and returns the resulting value
    provided to wire "a".
    """
    wire_known_values = {}
    evaluate_wire(input_p, wire_known_values, "a")
    return wire_known_values["a"]


def solve_part2(input_p):
    """
    Conducts initial pass of wire system evaluation, overrides the "b" wire with
    the "a" wire result, resets the other wires and re-evaluates the wire
    system. Returns the value provided to the "a" wire after the second wire
    system evaluation.
    """
    # Conduct first pass
    wire_known_values = {}
    evaluate_wire(input_p, wire_known_values, "a")
    # Override value on "b" wire
    new_wire_states = copy.deepcopy(input_p)
    new_wire_states["b"] = (Operation.OP_VALUE, wire_known_values["a"])
    # Conduct second pass
    wire_known_values = {}
    evaluate_wire(new_wire_states, wire_known_values, "a")
    return wire_known_values["a"]


def evaluate_wire(wire_states, wire_known_values, target_wire):
    """
    Evaluates the value of the target wire by recursively processing the wires
    providing input values to it.
    """
    if target_wire in wire_known_values:
        return
    # Initialise op parameters and result
    left = 0
    right = 0
    op_result = 0
    # Evaluate left
    if isinstance(wire_states[target_wire][1], str):
        new_target_wire = wire_states[target_wire][1]
        evaluate_wire(wire_states, wire_known_values, new_target_wire)
        left = wire_known_values[new_target_wire]
    else:
        left = wire_states[target_wire][1]
    # Evaluate right
    if (wire_states[target_wire][0] is Operation.OP_AND or
            wire_states[target_wire][0] is Operation.OP_LSHIFT or
            wire_states[target_wire][0] is Operation.OP_OR or
            wire_states[target_wire][0] is Operation.OP_RSHIFT):
        if isinstance(wire_states[target_wire][2], str):
            new_target_wire = wire_states[target_wire][2]
            evaluate_wire(wire_states, wire_known_values, new_target_wire)
            right = wire_known_values[new_target_wire]
        else:
            right = wire_states[target_wire][2]
    # Calculate op result
    match wire_states[target_wire][0]:
        case Operation.OP_VALUE:
            op_result = left
        case Operation.OP_AND:
            op_result = left & right
        case Operation.OP_LSHIFT:
            op_result = left << right
        case Operation.OP_NOT:
            op_result = ~left
        case Operation.OP_OR:
            op_result = left | right
        case Operation.OP_RSHIFT:
            op_result = left >> right
    # Update known wire values
    wire_known_values[target_wire] = op_result


if __name__ == "__main__":
    main()
