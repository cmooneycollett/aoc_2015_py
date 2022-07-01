"""
Solution code for AOC 2015 Day 11.
"""


import re


def process_input_file():
    """
    Processes the AOC 2015 Day 11 input file into the format required by the
    solver functions.
    """
    with open("./input/day_11.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_data):
    """
    Finds the next valid password after the given initial password.
    """
    return find_next_valid_password(input_data)


def solve_part2(input_data):
    """
    Find the second next valid password after the given initial password.
    """
    first_pass = find_next_valid_password(input_data)
    return find_next_valid_password(first_pass)


def increment_string(input_chars):
    """
    Increments the input characters by one place, going from right-to-left
    through 'a' to 'z'.
    """
    output_chars = input_chars.copy()
    i = len(output_chars) - 1
    while True:
        if i < 0:
            output_chars = ["a", output_chars]
            break
        if output_chars[i] == 'z':
            output_chars[i] = 'a'
            i -= 1
        else:
            output_chars[i] = chr(ord(output_chars[i]) + 1)
            break
    return output_chars


def find_next_valid_password(input_password):
    """
    Takes the input password and continues to increment the string characters
    right-to-left through 'a' to 'z' until the next valid password is found
    matching the rules given in the problem description.
    """
    regex_triple_char = re.compile(
        r"(abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)")
    regex_pairs = re.compile(r"([a-z])\1.*([a-z])\2")
    regex_bad_letters = re.compile(r"(i|l|o)")
    new_password_chars = list(input_password)
    while True:
        new_password_joined = "".join(new_password_chars)
        # Increment the password
        new_password_chars = increment_string(new_password_chars)
        # Perform validity checks
        new_password_joined = "".join(new_password_chars)
        match_pairs = regex_pairs.search(new_password_joined)
        if match_pairs is None or len(match_pairs.groups()) < 2 or \
                match_pairs.group(1) == match_pairs.group(2):
            continue
        if regex_bad_letters.search(new_password_joined):
            continue
        if regex_triple_char.search(new_password_joined) is None:
            continue
        # New password is deemed valid
        return new_password_joined
