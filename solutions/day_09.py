"""
Solutions for AOC 2015 Day 9.
"""

import itertools
import re


def main():
    """
    Solves AOC 2015 Day 9 Parts 1 and 2, printing out the solutions.
    """
    input_p = process_input_file()
    p1_solution = solve_part1(input_p)
    print(f"P1 solution - {p1_solution}")
    p2_solution = solve_part2(input_p)
    print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2015 Day 9 input file into the format required by the
    solver functions.
    """
    input_processed = {}
    regex_line = re.compile(r"^([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)$")
    with open("./inputs/day_09.txt", encoding="utf-8") as file:
        for line in file.readlines():
            # Ignore empty lines
            line = line.strip()
            if len(line) == 0:
                continue
            # Extract data fields from line
            match_dist = regex_line.match(line)
            city_from = match_dist.group(1)
            city_to = match_dist.group(2)
            distance = int(match_dist.group(3))
            if city_from not in input_processed:
                input_processed[city_from] = {}
            if city_to not in input_processed:
                input_processed[city_to] = {}
            input_processed[city_from][city_to] = distance
            input_processed[city_to][city_from] = distance
    return input_processed


def solve_part1(input_p):
    """
    Calculates the distance of the shortest route that visits all cities given
    in the input map, by trying each possible route option and tracking the
    shortest distance found.
    """
    cities = list(input_p.keys())
    city_permutations = itertools.permutations(cities)
    min_distance = -1
    # Calculate distance for all possible paths - 8! total
    for route_order in city_permutations:
        distance = 0
        for i in range(0, len(route_order) - 1):
            distance += input_p[route_order[i]][route_order[i + 1]]
        if min_distance == -1:
            min_distance = distance
        elif distance < min_distance:
            min_distance = distance
    return min_distance


def solve_part2(input_p):
    """
    Calculates the distance of the longest route that visits all cities given in
    the input map, by trying each possible route option and tracking the longest
    distance found.
    """
    cities = list(input_p.keys())
    city_permutations = itertools.permutations(cities)
    max_distance = -1
    for route_order in city_permutations:
        distance = 0
        for i in range(0, len(route_order) - 1):
            distance += input_p[route_order[i]][route_order[i + 1]]
        if max_distance == -1:
            max_distance = distance
        elif distance > max_distance:
            max_distance = distance
    return max_distance


if __name__ == "__main__":
    main()
