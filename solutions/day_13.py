import itertools
import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    input = {}
    regex_happ = re.compile(
        r"^([A-Z][a-z]+) would (gain|lose) (\d+) happiness units by sitting "
        r"next to ([A-Z][a-z]+).$")
    with open("./inputs/day_13.txt") as file:
        for line in file.readlines():
            # Skip blank lines
            line = line.strip()
            if len(line) == 0:
                continue
            # Extract interaction fields
            m = regex_happ.match(line)
            person_1 = m.group(1)
            person_2 = m.group(4)
            happ_units = int(m.group(3))
            if m.group(2) == "lose":
                happ_units = -happ_units
            # Insert data into problem input - interaction is uni-directional
            if person_1 not in input:
                input[person_1] = {}
            input[person_1][person_2] = happ_units
    return input


def solve_part1(input):
    """
    Determines the total change in happiness for the optimal seating arrangement by checking each
    possible order of guests, calculating result and comparing to running optimal value.
    """
    (_max_happ_guest_order, max_happ_delta) = find_optimal_seating_arrangement(input)
    return max_happ_delta


def solve_part2(input):
    """
    Determines the total change in happiness for the optimal seating arrangement including self
    seated (0 happiness gained or lost for these interactions) by checking each possible order of
    guests, calculating result and comparing to the running optimal value.
    """
    # Update the new happiness matrix to include self
    new_happ_matrix = dict(input)
    old_guest_list = list(input.keys())
    self_name = "Mr. Robot"
    new_happ_matrix[self_name] = {}
    for guest_name in old_guest_list:
        new_happ_matrix[self_name][guest_name] = 0
        new_happ_matrix[guest_name][self_name] = 0
    # Find the optimal seating arrangement
    (_max_happ_guest_order, max_happ_delta) = find_optimal_seating_arrangement(
        new_happ_matrix)
    return max_happ_delta


def find_optimal_seating_arrangement(happ_mat):
    guest_list = list(happ_mat.keys())
    guest_perms = itertools.permutations(guest_list)
    max_happiness_delta = None
    max_happiness_guest_order = None
    for perm in guest_perms:
        happiness_delta = 0
        for p1 in range(0, len(perm)):
            # Table is circular so last guest is sitting next to first
            p2 = p1 + 1
            if p1 == (len(perm) - 1):
                p2 = 0
            happiness_delta += happ_mat[perm[p1]][perm[p2]]
            happiness_delta += happ_mat[perm[p2]][perm[p1]]
        if max_happiness_delta is None:
            max_happiness_delta = happiness_delta
            max_happiness_guest_order = list(perm)
        elif happiness_delta > max_happiness_delta:
            max_happiness_delta = happiness_delta
            max_happiness_guest_order = list(perm)
    return (max_happiness_guest_order, max_happiness_delta)


if __name__ == "__main__":
    main()
