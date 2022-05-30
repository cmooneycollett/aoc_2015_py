import hashlib


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    with open("./inputs/day_04.txt") as file:
        data = file.read().strip()
        return data


def solve_part1(input) -> int:
    value = 0
    while True:
        prehash = "{}{}".format(input, str(value))
        hash = hashlib.md5(prehash.encode())
        if hash.hexdigest().startswith("00000"):
            return value
        else:
            value += 1


def solve_part2(input) -> int:
    value = 0
    while True:
        prehash = "{}{}".format(input, str(value))
        hash = hashlib.md5(prehash.encode())
        if hash.hexdigest().startswith("000000"):
            return value
        else:
            value += 1


if __name__ == "__main__":
    main()
