import re
from enum import Enum, auto, unique
import copy
from webbrowser import Opera


@unique
class Operation(Enum):
    OP_VALUE = auto()
    OP_AND = auto()
    OP_LSHIFT = auto()
    OP_NOT = auto()
    OP_OR = auto()
    OP_RSHIFT = auto()


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    p2_solution = solve_part2(input)
    print("P1 solution - {}".format(p1_solution))
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    input = {}
    regex_op_value = re.compile(r"^([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_and = re.compile(r"^([a-z]+|\d+) AND ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_lshift = re.compile(
        r"^([a-z]+|\d+) LSHIFT ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_not = re.compile(r"^NOT ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_or = re.compile(r"^([a-z]+|\d+) OR ([a-z]+|\d+) -> ([a-z]+)$")
    regex_op_rshift = re.compile(
        r"^([a-z]+|\d+) RSHIFT ([a-z]+|\d+) -> ([a-z]+)$")
    with open("./inputs/day_07.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            if regex_op_value.match(line):
                m = regex_op_value.match(line)
                value = m.group(1)
                output = m.group(2)
                if value.isnumeric():
                    value = int(value)
                input[output] = (Operation.OP_VALUE, value)
            elif regex_op_and.match(line):
                m = regex_op_and.match(line)
                left = m.group(1)
                right = m.group(2)
                output = m.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input[output] = (Operation.OP_AND, left, right)
            elif regex_op_lshift.match(line):
                m = regex_op_lshift.match(line)
                left = m.group(1)
                right = m.group(2)
                output = m.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input[output] = (Operation.OP_LSHIFT, left, right)
            elif regex_op_not.match(line):
                m = regex_op_not.match(line)
                value = m.group(1)
                output = m.group(2)
                if value.isnumeric():
                    value = int(value)
                input[output] = (Operation.OP_NOT, value)
            elif regex_op_or.match(line):
                m = regex_op_or.match(line)
                left = m.group(1)
                right = m.group(2)
                output = m.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input[output] = (Operation.OP_OR, left, right)
            elif regex_op_rshift.match(line):
                m = regex_op_rshift.match(line)
                left = m.group(1)
                right = m.group(2)
                output = m.group(3)
                if left.isnumeric():
                    left = int(left)
                if right.isnumeric():
                    right = int(right)
                input[output] = (Operation.OP_RSHIFT, left, right)
            else:
                print(line)
    return input


def solve_part1(input):
    wire_known_values = {}
    evaluate_wire(input, wire_known_values, "a")
    return wire_known_values["a"]


def solve_part2(input):
    ()


def evaluate_wire(wire_states, wire_known_values, target_wire):
    if target_wire in wire_known_values:
        return
    match wire_states[target_wire][0]:
        case Operation.OP_VALUE:
            if type(wire_states[target_wire][1]) is str:
                new_target_wire = wire_states[target_wire][1]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                wire_known_values[target_wire] = wire_known_values[new_target_wire]
            else:
                wire_known_values[target_wire] = wire_states[target_wire][1]
        case Operation.OP_AND:
            # Evaluate left
            left = None
            if type(wire_states[target_wire][1]) is str:
                new_target_wire = wire_states[target_wire][1]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                left = wire_known_values[new_target_wire]
            else:
                left = wire_states[target_wire][1]
            # Evaluate right
            right = None
            if type(wire_states[target_wire][2]) is str:
                new_target_wire = wire_states[target_wire][2]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                right = wire_known_values[new_target_wire]
            else:
                right = wire_states[target_wire][2]
            # Calculate op result
            op_result = left & right
            # Update known values
            wire_known_values[target_wire] = op_result
        case Operation.OP_LSHIFT:
            # Evaluate left
            left = None
            if type(wire_states[target_wire][1]) is str:
                new_target_wire = wire_states[target_wire][1]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                left = wire_known_values[new_target_wire]
            else:
                left = wire_states[target_wire][1]
            # Evaluate right
            right = None
            if type(wire_states[target_wire][2]) is str:
                new_target_wire = wire_states[target_wire][2]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                right = wire_known_values[new_target_wire]
            else:
                right = wire_states[target_wire][2]
            # Calculate op result
            op_result = left << right
            # Update known values
            wire_known_values[target_wire] = op_result
        case Operation.OP_NOT:
            # Evaluate left
            left = None
            if type(wire_states[target_wire][1]) is str:
                new_target_wire = wire_states[target_wire][1]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                left = wire_known_values[new_target_wire]
            else:
                left = wire_states[target_wire][1]
            # Calculate op result
            op_result = ~left
            # Update known values
            wire_known_values[target_wire] = op_result
        case Operation.OP_OR:
            # Evaluate left
            left = None
            if type(wire_states[target_wire][1]) is str:
                new_target_wire = wire_states[target_wire][1]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                left = wire_known_values[new_target_wire]
            else:
                left = wire_states[target_wire][1]
            # Evaluate right
            right = None
            if type(wire_states[target_wire][2]) is str:
                new_target_wire = wire_states[target_wire][2]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                right = wire_known_values[new_target_wire]
            else:
                right = wire_states[target_wire][2]
            # Calculate op result
            op_result = left | right
            # Update known values
            wire_known_values[target_wire] = op_result
        case Operation.OP_RSHIFT:
            # Evaluate left
            left = None
            if type(wire_states[target_wire][1]) is str:
                new_target_wire = wire_states[target_wire][1]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                left = wire_known_values[new_target_wire]
            else:
                left = wire_states[target_wire][1]
            # Evaluate right
            right = None
            if type(wire_states[target_wire][2]) is str:
                new_target_wire = wire_states[target_wire][2]
                evaluate_wire(wire_states, wire_known_values, new_target_wire)
                right = wire_known_values[new_target_wire]
            else:
                right = wire_states[target_wire][2]
            # Calculate op result
            op_result = left >> right
            # Update known values
            wire_known_values[target_wire] = op_result


if __name__ == "__main__":
    main()
