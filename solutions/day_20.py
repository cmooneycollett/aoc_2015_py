import math


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    with open("./inputs/day_20.txt") as file:
        return int(file.read().strip())


def solve_part1(input):
    target = input
    presents_arr = [0 for _i in range(0, target)]   # presents per house
    house_target = -1
    for elf in range(1, target + 1):
        # Consider problem space up to the target present count
        for house in range(elf, target, elf):
            presents_arr[house - 1] += elf * 10
        if presents_arr[elf - 1] >= target:
            house_target = elf
            break
    return house_target


def solve_part2(input):
    target = input
    presets_record = {}
    elf = 1
    while True:
        # Elf only visits its first 50 houses
        for mult in range(1, 51):
            if (elf * mult) in presets_record:
                presets_record[elf * mult] += elf * 11
            else:
                presets_record[elf * mult] = elf * 11
        # Check if present target has been reached
        if presets_record[elf] >= target:
            break
        else:
            elf += 1
    return elf


if __name__ == "__main__":
    main()
