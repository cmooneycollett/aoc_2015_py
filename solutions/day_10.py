"""
Solutions for AOC 2015 Day 10.
"""


def main():
    """
    Solves AOC 2015 Day 10 Parts 1 and 2, printing out the solutions.
    """
    input_data = process_input_file()
    p1_solution = solve_part1(input_data)
    print(f"P1 solution - {p1_solution}")
    p2_solution = solve_part2(input_data)
    print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2015 Day 10 input file into the format required by the
    solver functions.
    """
    with open("./inputs/day_10.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_data):
    """
    Applies 40 iterations of the "look-and-say" process to the input string,
    returning the resulting string.
    """
    result_string = str(input_data)
    for _ in range(0, 40):
        result_string = apply_looksay_iteration(result_string)
    return len(result_string)


def solve_part2(input_data):
    """
    Applies 50 iterations of the "look-and-say" process to the input string,
    returning the resulting string.
    """
    result_str = str(input_data)
    for _ in range(0, 50):
        result_str = apply_looksay_iteration(result_str)
    return len(result_str)


def apply_looksay_iteration(input_string):
    """
    Returns the result of applying one iteration of the "look-and-say" process
    to the input string.
    """
    output_string = str("")
    i = 0
    while True:
        if i >= len(input_string):
            break
        # Check current character
        char = input_string[i]
        streak_len = 1
        # Check if next char is same
        while True:
            i += 1
            if i >= len(input_string):
                break
            if input_string[i] == char:
                streak_len += 1
            else:
                break
        # Add to the output string
        output_string = "".join([output_string, str(streak_len), char])
    return output_string


if __name__ == "__main__":
    main()
