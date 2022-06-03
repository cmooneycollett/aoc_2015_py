import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    input = []
    regex_sue = re.compile(
        r"^Sue (\d+): "
        r"(children|cats|samoyeds|pomeranians|akitas|vizslas|goldfish|trees|cars|perfumes): (\d+), "
        r"(children|cats|samoyeds|pomeranians|akitas|vizslas|goldfish|trees|cars|perfumes): (\d+), "
        r"(children|cats|samoyeds|pomeranians|akitas|vizslas|goldfish|trees|cars|perfumes): (\d+)$")
    with open("./inputs/day_16.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            m = regex_sue.match(line)
            field_1 = m.group(2)
            field_1_val = int(m.group(3))
            field_2 = m.group(4)
            field_2_val = int(m.group(5))
            field_3 = m.group(6)
            field_3_val = int(m.group(7))
            input.append(
                {field_1: field_1_val, field_2: field_2_val, field_3: field_3_val})
    return input


def solve_part1(input):
    """
    Determines which is the real Aunt Sue by matching observations against the
    output information from the MFCSAM.
    """
    sue_details = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,
                   "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    sue_candidate_indices = []
    for i in range(0, len(input)):
        sue = input[i]
        is_candidate = True
        for (field, val) in sue.items():
            if val != sue_details[field]:
                is_candidate = False
                break
        if is_candidate:
            sue_candidate_indices.append(i + 1)
    return sue_candidate_indices[0]


def solve_part2(input):
    """
    Determines which is the real Aunt Sue by matching observations against the
    output information from the MFCSAM, taking into account the greater than
    fields for "cats" and "trees", and the less than fields for "pomeranians"
    and "goldfish".
    """
    sue_details = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,
                   "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    sue_candidate_indices = []
    for i in range(0, len(input)):
        sue = input[i]
        is_candidate = True
        for (field, val) in sue.items():
            match field:
                case "children": is_candidate = (val == sue_details[field])
                case "cats": is_candidate = (val > sue_details[field])
                case "samoyeds": is_candidate = (val == sue_details[field])
                case "pomeranians": is_candidate = (val < sue_details[field])
                case "akitas": is_candidate = (val == sue_details[field])
                case "vizslas": is_candidate = (val == sue_details[field])
                case "goldfish": is_candidate = (val < sue_details[field])
                case "trees": is_candidate = (val > sue_details[field])
                case "cars": is_candidate = (val == sue_details[field])
                case "perfumes": is_candidate = (val == sue_details[field])
            if not is_candidate:
                break
        if is_candidate:
            sue_candidate_indices.append(i + 1)
    return sue_candidate_indices[0]


if __name__ == "__main__":
    main()
