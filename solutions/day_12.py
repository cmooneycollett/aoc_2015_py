import json
import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    with open("./inputs/day_12.txt") as file:
        return file.read().strip()


def solve_part1(input):
    numbers_raw = re.findall(r"-?\d+", input)
    numbers = [int(n) for n in numbers_raw]
    total = 0
    for n in numbers:
        total += n
    return total


def solve_part2(input):
    numbers_valid = []
    json_data = json.loads(input)
    # Discover all valid numbers within the json data
    discover_valid_numbers(numbers_valid, json_data)
    # Return the total of all valid numbers
    return sum(numbers_valid)


def discover_valid_numbers(numbers_valid, obj):
    if isinstance(obj, int):
        numbers_valid.append(obj)
    elif isinstance(obj, list):
        for x in obj:
            if isinstance(x, int):
                numbers_valid.append(x)
            elif isinstance(x, list) or isinstance(x, dict):
                discover_valid_numbers(numbers_valid, x)
    elif isinstance(obj, dict):
        # Check for invalid object
        if "red" in obj.values():
            return
        for x in obj.values():
            if isinstance(x, int):
                numbers_valid.append(x)
            elif isinstance(x, list) or isinstance(x, dict):
                discover_valid_numbers(numbers_valid, x)


if __name__ == "__main__":
    main()
