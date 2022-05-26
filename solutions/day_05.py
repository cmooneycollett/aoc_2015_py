import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    p2_solution = solve_part2(input)
    print("P1 solution - {}".format(p1_solution))
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    input = []
    with open("./inputs/day_05.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            input.append(line)
    return input


def solve_part1(input):
    regex_nice_1 = re.compile(r'^.*([aeiou]).*([aeiou]).*([aeiou]).*$')
    regex_nice_2 = re.compile(r'^.*([a-z])\1.*$')
    regex_bad_1 = re.compile(r'^.*(ab|cd|pq|xy).*$')
    nice_count = 0
    for s in input:
        if regex_nice_1.match(s) and regex_nice_2.match(s) and not regex_bad_1.match(s):
            nice_count += 1
    return nice_count


def solve_part2(input):
    ()


if __name__ == "__main__":
    main()
