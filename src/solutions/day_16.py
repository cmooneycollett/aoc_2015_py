"""
Solutions for AOC 2015 Day 16.
"""


import re


def process_input_file():
    """
    Processes the AOC 2015 Day 16 input file into the format required by the
    solver functions. The
    """
    input_data = {}
    regex_sue = re.compile(
        r"^Sue (\d+): "
        r"(children|cats|samoyeds|pomeranians|akitas|vizslas|goldfish|trees|cars|perfumes): (\d+), "
        r"(children|cats|samoyeds|pomeranians|akitas|vizslas|goldfish|trees|cars|perfumes): (\d+), "
        r"(children|cats|samoyeds|pomeranians|akitas|vizslas|goldfish|trees|cars|perfumes): (\d+)$")
    with open("./input/day_16.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            match_sue_info = regex_sue.match(line)
            sue_number = int(match_sue_info.group(1))
            field1_name = match_sue_info.group(2)
            field1_value = int(match_sue_info.group(3))
            field2_name = match_sue_info.group(4)
            field2_value = int(match_sue_info.group(5))
            field3_name = match_sue_info.group(6)
            field3_value = int(match_sue_info.group(7))
            input_data[sue_number] = {field1_name: field1_value,
                                      field2_name: field2_value,
                                      field3_name: field3_value}
    return input_data


def solve_part1(input_data):
    """
    Determines which is the real Aunt Sue by matching observations against the
    output information from the My First Crime Scene Analysis Machine (MFCSAM).
    """
    sue_details = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,
                   "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,
                   "cars": 2, "perfumes": 1}
    for (candidate_number, candidate_details) in input_data.items():
        is_candidate = True
        for (name, value) in candidate_details.items():
            if value != sue_details[name]:
                is_candidate = False
                break
        if is_candidate:
            return candidate_number
    return -1


def solve_part2(input_data):
    """
    Determines which is the real Aunt Sue by matching observations against the
    output information from the MFCSAM, taking into account the greater than
    fields for "cats" and "trees", and the less than fields for "pomeranians"
    and "goldfish".
    """
    sue_details = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,
                   "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,
                   "cars": 2, "perfumes": 1}
    for (candidate_number, candidate_details) in input_data.items():
        is_candidate = True
        for (name, value) in candidate_details.items():
            match name:
                case "children": is_candidate = (value == sue_details[name])
                case "cats": is_candidate = (value > sue_details[name])
                case "samoyeds": is_candidate = (value == sue_details[name])
                case "pomeranians": is_candidate = (value < sue_details[name])
                case "akitas": is_candidate = (value == sue_details[name])
                case "vizslas": is_candidate = (value == sue_details[name])
                case "goldfish": is_candidate = (value < sue_details[name])
                case "trees": is_candidate = (value > sue_details[name])
                case "cars": is_candidate = (value == sue_details[name])
                case "perfumes": is_candidate = (value == sue_details[name])
            if not is_candidate:
                break
        if is_candidate:
            return candidate_number
    return -1
