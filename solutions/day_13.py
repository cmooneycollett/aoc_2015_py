"""
Solutions for AOC 2015 Day 13.
"""


import itertools
import re


def main():
    """
    Solves AOC 2015 Day 13 Parts 1 and 2, printing out the solutions.
    """
    input_data = process_input_file()
    p1_solution = solve_part1(input_data)
    print(f"P1 solution - {p1_solution}")
    p2_solution = solve_part2(input_data)
    print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2015 Day 13 input file into the format required by the
    solver functions. Returned data structure is a dictionary that, for each
    guest (first key), maps the happiness they would gain or lose (key) by
    sitting next to each of the other guests (second key).
    """
    input_data = {}
    regex_happiness_line = re.compile(
        r"^([A-Z][a-z]+) would (gain|lose) (\d+) happiness units by sitting "
        r"next to ([A-Z][a-z]+).$")
    with open("./inputs/day_13.txt", encoding="utf-8") as file:
        for line in file.readlines():
            # Skip blank lines
            line = line.strip()
            if len(line) == 0:
                continue
            # Extract interaction fields
            match_line = regex_happiness_line.match(line)
            person_1 = match_line.group(1)
            person_2 = match_line.group(4)
            happ_units = int(match_line.group(3))
            if match_line.group(2) == "lose":
                happ_units = -happ_units
            # Insert data into problem input - interaction is uni-directional
            if person_1 not in input_data:
                input_data[person_1] = {}
            input_data[person_1][person_2] = happ_units
    return input_data


def solve_part1(input_data):
    """
    Determines the total change in happiness for the optimal seating arrangement
    by checking each possible order of guests, calculating result and comparing
    to running optimal value.
    """
    max_happiness_delta = find_maximum_happiness_delta(input_data)
    return max_happiness_delta


def solve_part2(input_data):
    """
    Determines the total change in happiness for the optimal seating arrangement
    including self seated (0 happiness gained or lost for these interactions) by
    checking each possible order of guests, calculating result and comparing to
    the running optimal value.
    """
    # Update the new happiness matrix to include self
    new_happiness_matrix = dict(input_data)
    old_guest_list = list(input_data.keys())
    self_name = "Mr. Robot"
    new_happiness_matrix[self_name] = {}
    for guest_name in old_guest_list:
        new_happiness_matrix[self_name][guest_name] = 0
        new_happiness_matrix[guest_name][self_name] = 0
    # Find the optimal seating arrangement
    max_happiness_delta = find_maximum_happiness_delta(new_happiness_matrix)
    return max_happiness_delta


def find_maximum_happiness_delta(happiness_matrix):
    """
    Determines the maximum possible happiness delta in the optimal seating
    arrangement by evaluating the happiness delta for each permutation of guests
    and selecting the highest happiness delta observed.
    """
    # Determine the possible permutations of guests
    guest_list = list(happiness_matrix.keys())
    guest_permutations = itertools.permutations(guest_list)
    max_happiness_delta = None
    for guest_order in guest_permutations:
        # Calculate the happiness delta for current guest ordering
        happiness_delta = 0
        for guest_1_index, guest_1_name in enumerate(guest_order):
            guest_2_index = guest_1_index + 1
            if guest_2_index >= len(guest_order):
                guest_2_index = 0
            guest_2_name = guest_order[guest_2_index]
            happiness_delta += happiness_matrix[guest_1_name][guest_2_name]
            happiness_delta += happiness_matrix[guest_2_name][guest_1_name]
        # Update the maximum happiness delta value if required
        if max_happiness_delta is None:
            max_happiness_delta = happiness_delta
        elif happiness_delta > max_happiness_delta:
            max_happiness_delta = happiness_delta
    return max_happiness_delta


if __name__ == "__main__":
    main()
