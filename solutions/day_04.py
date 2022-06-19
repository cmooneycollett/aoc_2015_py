"""
Solutions for AOC 2015 Day 4.
"""

import hashlib


def main():
    """
    Solves AOC 2015 Parts 1 and 2, printing out the solutions.
    """
    input_data = process_input_file()
    p1_solution = solve_part1(input_data)
    print(f"P1 solution - {p1_solution}")
    p2_solution = solve_part2(input_data)
    print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2015 Day 4 input file into the format needed by the solver
    functions.
    """
    with open("./inputs/day_04.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_data):
    """
    Finds the first MD5 hash of input key and sequence number that begins with
    five zeroes, returning the corresponding sequence number.
    """
    sequence_num = 0
    while True:
        prehash_string = f"{input_data}{sequence_num}"
        hash_result = hashlib.md5(prehash_string.encode())
        if hash_result.hexdigest().startswith("00000"):
            return sequence_num
        # Continue to the next sequence number
        sequence_num += 1


def solve_part2(input_data):
    """
    Finds the first MD5 hash of the input key and sequence number that begins
    with six zeroes, returning the corresponding sequence number.
    """
    sequence_num = 0
    while True:
        prehash_string = f"{input_data}{sequence_num}"
        hash_result = hashlib.md5(prehash_string.encode())
        if hash_result.hexdigest().startswith("000000"):
            return sequence_num
        # Continue to the next sequence number
        sequence_num += 1


if __name__ == "__main__":
    main()
