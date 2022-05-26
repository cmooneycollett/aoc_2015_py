import re


def main():
    # Read problem input file
    input = process_input_file()
    p1_solution = solve_part1(input)
    p2_solution = solve_part2(input)
    print("P1 solution - {}".format(p1_solution))
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    with open("./inputs/day_02.txt") as file:
        raw_input = file.read().strip()
        data = []
        regex = re.compile("(\d+)x(\d+)x(\d+)")
        for line in raw_input.splitlines():
            line = line.strip()
            if len(line) == 0:
                continue
            m = regex.match(line)
            line_data = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
            data.append(line_data)
    return data


def solve_part1(input) -> int:
    total_paper = 0
    for data in input:
        side_areas = [data[0] * data[1], data[0] * data[2], data[1] * data[2]]
        slack = min(side_areas)
        total_paper += 2 * sum(side_areas) + slack
    return total_paper


def solve_part2(input) -> int:
    total_ribbon = 0
    for data in input:
        side_perims = [2 * (data[0] + data[1]), 2 *
                       (data[0] + data[2]), 2 * (data[1] + data[2])]
        volume = data[0] * data[1] * data[2]
        ribbon = min(side_perims) + volume
        total_ribbon += ribbon
    return total_ribbon


if __name__ == "__main__":
    main()
