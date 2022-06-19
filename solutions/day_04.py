"""
Solutions for AOC 2015 Day 4.
"""

import hashlib


def main():
    """
    Solves AOC 2015 Parts 1 and 2, printing out the solutions.
    """
    input_p = process_input_file()
    p1_solution = solve_part1(input_p)
    print(f"P1 solution - {p1_solution}")
    p2_solution = solve_part2(input_p)
    print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2015 Day 4 input file into the format needed by the solver
    functions.
    """
    with open("./inputs/day_04.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_p):
    """
    Finds the first MD5 hash of input key and sequence number that begins with
    five zeroes, returning the corresponding sequence number.
    """
    value = 0
    while True:
        prehash = f"{input_p}{value}"
        hash_result = hashlib.md5(prehash.encode())
        if hash_result.hexdigest().startswith("00000"):
            return value
        # Continue to the next sequence number
        value += 1


def solve_part2(input_p):
    """
    Finds the first MD5 hash of the input key and sequence number that begins
    with six zeroes, returning the corresponding sequence number.
    """
    value = 0
    while True:
        prehash = f"{input_p}{value}"
        hash_result = hashlib.md5(prehash.encode())
        if hash_result.hexdigest().startswith("000000"):
            return value
        # Continue to the next sequence number
        value += 1


if __name__ == "__main__":
    main()
