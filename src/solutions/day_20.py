"""
Solutions for AOC 2015 Day 20.
"""


def process_input_file():
    """
    Processes the AOC 2015 Day 20 input file into the format required by the
    solver functions. Returned value is the single integer value given in the
    input file.
    """
    with open("./input/day_20.txt", encoding="utf-8") as file:
        return int(file.read().strip())


def solve_part1(input_data):
    """
    Determines the lowest house number to receive at least as many presents as
    the input value, with each elf visiting an infinite number of houses.
    """
    target = input_data
    presents_arr = [0 for _ in range(0, target)]   # presents per house
    house_target = -1
    for elf in range(1, target + 1):
        # Consider problem space up to the target present count
        for house in range(elf, target, elf):
            presents_arr[house - 1] += elf * 10
        if presents_arr[elf - 1] >= target:
            house_target = elf
            break
    return house_target


def solve_part2(input_data):
    """
    Determines the lowest house number to receive at least as many presents as
    the input value, with each elf visiting 50 houses (including their starting
    house).
    """
    target = input_data
    presets_record = {}
    elf = 1
    while True:
        # Elf only visits its first 50 houses
        for mult in range(1, 51):
            if elf * mult in presets_record:
                presets_record[elf * mult] += elf * 11
            else:
                presets_record[elf * mult] = elf * 11
        # Check if present target has been reached
        if presets_record[elf] >= target:
            break
        elf += 1
    return elf
