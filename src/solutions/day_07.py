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


def process_input_file():
    """
    Processes the AOC 2015 Day 7 input file into the format required by the
    solver functions.
    """
    input_data = {}
    regex_op_value = re.compile(r"^([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_and = re.compile(r"^([a-z]+|\d+) AND ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_lshift = re.compile(
        r"^([a-z]+|\d+) LSHIFT ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_not = re.compile(r"^NOT ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_or = re.compile(r"^([a-z]+|\d+) OR ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_rshift = re.compile(
        r"^([a-z]+|\d+) RSHIFT ([a-z]+|\d+) -> ([a-z]+)$")
    with open("./input/day_07.txt", encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if (match_line := regex_op_value.match(line)):
                value = match_line.group(1)
                output = match_line.group(2)
                if value.isnumeric():
                    value = int(value)
                input_data[output] = (Operation.OP_VALUE, value)
            elif (match_line := regex_op_and.match(line)):
                left = match_line.group(1)
                right = match_line.group(2)
                output = match_line.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input_data[output] = (Operation.OP_AND, left, right)
            elif (match_line := regex_op_lshift.match(line)):
                left = match_line.group(1)
                right = match_line.group(2)
                output = match_line.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input_data[output] = (Operation.OP_LSHIFT, left, right)
            elif (match_line := regex_op_not.match(line)):
                value = match_line.group(1)
                output = match_line.group(2)
                if value.isnumeric():
                    value = int(value)
                input_data[output] = (Operation.OP_NOT, value)
            elif (match_line := regex_op_or.match(line)):
                left = match_line.group(1)
                right = match_line.group(2)
                output = match_line.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input_data[output] = (Operation.OP_OR, left, right)
            elif (match_line := regex_op_rshift.match(line)):
                left = match_line.group(1)
                right = match_line.group(2)
                output = match_line.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input_data[output] = (Operation.OP_RSHIFT, left, right)
    return input_data


def solve_part1(input_data):
    """
    Solves AOC 2015 Day 7 Part 1 // Evaluates the inputs to the wire system and
    returns the resulting value provided to wire "a".
    """
    wire_known_values = {}
    evaluate_wire(input_data, wire_known_values, "a")
    return wire_known_values["a"]


def solve_part2(input_data):
    """
    Solves AOC 2015 Day 7 Part 2 // Conducts initial pass of wire system
    evaluation, overrides the "b" wire with the "a" wire result, resets the
    other wires and re-evaluates the wire system. Returns the value provided to
    the "a" wire after the second wire system evaluation.
    """
    # Conduct first pass
    wire_known_values = {}
    evaluate_wire(input_data, wire_known_values, "a")
    # Override value on "b" wire
    new_wire_states = copy.deepcopy(input_data)
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
