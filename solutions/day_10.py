from unittest import result


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    p2_solution = solve_part2(input)
    print("P1 solution - {}".format(p1_solution))
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    with open("./inputs/day_10.txt") as file:
        return file.read().strip()


def solve_part1(input):
    result_str = str(input)
    for _ in range(0, 40):
        result_str = apply_looksay_iteration(result_str)
    return len(result_str)


def solve_part2(input):
    ()


def apply_looksay_iteration(input_str):
    output_str = str("")
    i = 0
    while True:
        if i >= len(input_str):
            break
        # Check current character
        current_c = input_str[i]
        streak_len = 1
        # Check if next char is same
        while True:
            i += 1
            if i >= len(input_str):
                break
            if input_str[i] == current_c:
                streak_len += 1
            else:
                break
        # Add to the output string
        output_str = "{}{}{}".format(output_str, str(streak_len), current_c)
    return output_str


if __name__ == "__main__":
    main()
