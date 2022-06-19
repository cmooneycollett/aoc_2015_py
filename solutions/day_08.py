"""
Solutions for AOC 2015 Day 8.
"""


import re


def main():
    """
    Solves AOC 2015 Day 8 Parts 1 and 2, printing out the solutions.
    """
    input_p = process_input_file()
    p1_solution = solve_part1(input_p)
    print(f"P1 solution - {p1_solution}")
    p2_solution = solve_part2(input_p)
    print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2015 Day 8 input file into the format required by the
    solver functions.
    """
    input_processed = []
    with open("./inputs/day_08.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            input_processed.append(line)
    return input_processed


def solve_part1(input_p):
    """
    Calculates the difference between the number of characters in the string
    literals (input) and the converted "in-memory" representations of the
    strings (using the rules given in the problem description).
    """
    total_len_str_literal = 0
    total_len_str_inmem = 0
    for string in input_p:
        total_len_str_literal += len(string)
        new_string = str(string)
        # Remove open and close double-quote
        new_string = re.sub(r"^\"", r"", new_string)
        new_string = re.sub(r"\"$", r"", new_string)
        # Replace escaped characters
        new_string = re.sub(r"\\\\", r"\\", new_string)
        new_string = re.sub(r"\\\"", r'"', new_string)
        new_string = re.sub(r"\\x[0-9a-f][0-9a-f]", r"#", new_string)
        total_len_str_inmem += len(new_string)
    return total_len_str_literal - total_len_str_inmem


def solve_part2(input_p):
    """
    Calculates the difference between the number of characters between the
    newly-encoded strings (using the rules given in the problem description) and
    the original string literals (input).
    """
    total_len_str_literal = 0
    total_len_str_escaped = 0
    for string in input_p:
        total_len_str_literal += len(string)
        new_string = str(string)
        # Replace back-slash (also covers hex representations)
        new_string = re.sub(r"\\", r"\\\\", new_string)
        # Replace double quote (also covers the open and close double-quotes)
        new_string = re.sub(r'"', r'\\"', new_string)
        # Enclose in new double-quotes
        new_string = f'"{new_string}"'
        total_len_str_escaped += len(new_string)
    return total_len_str_escaped - total_len_str_literal


if __name__ == "__main__":
    main()
