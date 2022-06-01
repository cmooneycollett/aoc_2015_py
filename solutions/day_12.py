import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    with open("./inputs/day_12.txt") as file:
        return file.read().strip()


def solve_part1(input):
    numbers_raw = re.findall(r"-?\d+", input)
    numbers = [int(n) for n in numbers_raw]
    total = 0
    for n in numbers:
        total += n
    return total


def solve_part2(input):
    ()


if __name__ == "__main__":
    main()
