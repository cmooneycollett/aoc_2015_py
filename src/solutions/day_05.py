"""
Solutions for AOC 2015 Day 5.
"""


import re


def process_input_file():
    """
    Processes the AOC 2015 Day 5 input file into the format required by the
    solver functions.
    """
    input_data = []
    with open("./input/day_05.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            input_data.append(line)
    return input_data


def solve_part1(input_data):
    """
    Checks input strings for "niceness" (using the Part 1 properties specified
    in problem description), and returns how many of the strings are nice.
    """
    regex_nice_1 = re.compile(r"^.*([aeiou]).*([aeiou]).*([aeiou]).*$")
    regex_nice_2 = re.compile(r"^.*([a-z])\1.*$")
    regex_bad_1 = re.compile(r"^.*(ab|cd|pq|xy).*$")
    nice_count = 0
    for string in input_data:
        if regex_nice_1.match(string) and regex_nice_2.match(string) and \
                not regex_bad_1.match(string):
            nice_count += 1
    return nice_count


def solve_part2(input_data):
    """
    Checks input strings for "niceness" (using the updated Part 2 properties
    specified in problem description), and returns how many of the strings are
    nice.
    """
    regex_nice_1 = re.compile(r"^.*([a-z][a-z]).*\1.*$")
    regex_nice_2 = re.compile(r"^.*([a-z])[a-z]\1.*$")
    nice_count = 0
    for string in input_data:
        if regex_nice_1.match(string) and regex_nice_2.match(string):
            nice_count += 1
    return nice_count
