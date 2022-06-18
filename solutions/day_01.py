"""
Solutions for AOC 2015 Day 1.
"""


def main():
    """
    Solves AOC 2015 Day 1 Parts 1 and 2, printing out the solutions.
    """
    # Read in problem input
    input_p = process_input_file()
    p1_solution = solve_part1(input_p)
    print(f"P1 solution - {p1_solution}")
    p2_solution = solve_part2(input_p)
    print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2015 Day 1 input file into format for solvers.
    """
    with open("./inputs/day_01.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_p):
    """
    Calculates the final floor result from processing the input instructions.
    """
    floor = 0
    for char in input_p:
        if char == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def solve_part2(input_p):
    """
    Calculates the location of the input character that causes Santa to first
    enter the basement floor.
    """
    pos = 1
    floor = 0
    for char in input_p:
        if char == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            break
        else:
            pos += 1
    return pos


if __name__ == "__main__":
    main()
