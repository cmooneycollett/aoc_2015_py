import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    regex_grid = re.compile(r"row (\d+), column (\d+)")
    with open("./inputs/day_25.txt") as file:
        raw_input = file.read().strip()
        m = regex_grid.search(raw_input)
        return (int(m.group(1)), int(m.group(2)))


def solve_part1(input):
    """
    Calculates the code required to start-up the weather machine.
    """
    (row, column) = input
    # First stage
    seq = sum(range(1, column + 1))    # Initially the column top value
    increment = column
    for _ in range(1, row):
        seq += increment
        increment += 1
    # Second stage
    code = 20151125 # Value in grid at r,c (1,1)
    for _ in range(1, seq):
        code *= 252533
        code %= 33554393
    return code


def solve_part2(input):
    ()


if __name__ == "__main__":
    main()
