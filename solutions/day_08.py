import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    p2_solution = solve_part2(input)
    print("P1 solution - {}".format(p1_solution))
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    input = []
    with open("./inputs/day_08.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            input.append(line)
    return input


def solve_part1(input):
    total_len_str_literal = 0
    total_len_str_inmem = 0
    for s in input:
        total_len_str_literal += len(s)
        new_s = str(s)
        # Remove open and close double-quote
        new_s = re.sub(r"^\"", r"", new_s)
        new_s = re.sub(r"\"$", r"", new_s)
        # Replace escaped characters
        new_s = re.sub(r"\\\\", r"\\", new_s)
        new_s = re.sub(r"\\\"", r'"', new_s)
        new_s = re.sub(r"\\x[0-9a-f][0-9a-f]", r"#", new_s)
        total_len_str_inmem += len(new_s)
    return total_len_str_literal - total_len_str_inmem


def solve_part2(input):
    total_len_str_literal = 0
    total_len_str_escaped = 0
    for s in input:
        total_len_str_literal += len(s)
        new_s = str(s)
        # Replace back-slash (also covers hex representations)
        new_s = re.sub(r"\\", r"\\\\", new_s)
        # Replace double quote (also covers the open and close double-quotes)
        new_s = re.sub(r'"', r'\\"', new_s)
        # Enclose in new double-quotes
        new_s = '"{}"'.format(new_s)
        total_len_str_escaped += len(new_s)
    return total_len_str_escaped - total_len_str_literal


if __name__ == "__main__":
    main()
