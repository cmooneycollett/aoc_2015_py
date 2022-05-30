import itertools
import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    p2_solution = solve_part2(input)
    print("P1 solution - {}".format(p1_solution))
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    input = {}
    regex_line = re.compile(r"^([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)$")
    with open("./inputs/day_09.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            m = regex_line.match(line)
            city_from = m.group(1)
            city_to = m.group(2)
            distance = int(m.group(3))
            if city_from not in input:
                input[city_from] = {}
            if city_to not in input:
                input[city_to] = {}
            input[city_from][city_to] = distance
            input[city_to][city_from] = distance
    return input


def solve_part1(input):
    cities = list(input.keys())
    city_perms = itertools.permutations(cities)
    min_distance = None
    # Calculate distance for all possible paths - 8! total
    for perm in city_perms:
        distance = 0
        for i in range(0, len(perm) - 1):
            distance += input[perm[i]][perm[i + 1]]
        if min_distance is None:
            min_distance = distance
        elif distance < min_distance:
            min_distance = distance
    return min_distance


def solve_part2(input):
    cities = list(input.keys())
    city_perms = itertools.permutations(cities)
    max_distance = None
    for perm in city_perms:
        distance = 0
        for i in range(0, len(perm) - 1):
            distance += input[perm[i]][perm[i + 1]]
        if max_distance is None:
            max_distance = distance
        elif distance > max_distance:
            max_distance = distance
    return max_distance


if __name__ == "__main__":
    main()
