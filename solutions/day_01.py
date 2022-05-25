def main():
    # Read in problem input
    input = generate_input()
    p1_solution = solve_part1(input)
    p2_solution = solve_part2(input)
    print("P1 solution - {}".format(p1_solution))
    print("P2 solution - {}".format(p2_solution))


def generate_input():
    with open("./inputs/day_01.txt") as file:
        input = file.read().strip()
    return input


def solve_part1(input) -> int:
    floor = 0
    for c in input:
        if c == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def solve_part2(input) -> int:
    pos = 1
    floor = 0
    for c in input:
        if c == '(':
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
