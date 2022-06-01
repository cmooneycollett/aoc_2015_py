import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def increment_string(input_chars):
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


def process_input_file():
    with open("./inputs/day_11.txt") as file:
        return list(file.read().strip())


def solve_part1(input):
    regex_triple_char = re.compile(
        r"(abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)")
    regex_pairs = re.compile(r"([a-z])\1.*([a-z])\2")
    regex_bad_letters = re.compile(r"(i|l|o)")
    new_password_chars = input.copy()
    while True:
        new_password_joined = "".join(new_password_chars)
        # Increment the password
        new_password_chars = increment_string(new_password_chars)
        # Perform validity checks
        new_password_joined = "".join(new_password_chars)
        m = regex_pairs.search(new_password_joined)
        if m is None or len(m.groups()) < 2 or m.group(1) == m.group(2):
            continue
        if regex_bad_letters.search(new_password_joined):
            continue
        if regex_triple_char.search(new_password_joined) is None:
            continue
        # New password is deemed valid
        return new_password_joined


def solve_part2(input):
    ()


if __name__ == "__main__":
    main()
