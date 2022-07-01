"""
Solutions for AOC 2015 Day 17.
"""


def process_input_file():
    """
    Processes the AOC 2015 Day 17 input file into the format required by the
    solver functions. Returned value is a list containing the int values listed
    in the input file.
    """
    with open("./input/day_17.txt", encoding="utf-8") as file:
        lines = [line.strip()
                 for line in file.readlines() if len(line.strip()) > 0]
        return [int(n) for n in lines]


def solve_part1(input_data):
    """
    Calculates the total number of ways that the input values can be selected
    in such a way that the selected values add up to 150.
    """
    return sum(count_subsets_adding_to_total(input_data, 150).values())


def solve_part2(input_data):
    """
    Calculates the number of ways the input values can be selected in such a way
    that the selected values add up to 150, and the number of selected values is
    the minimum possible number.
    """
    container_counts = count_subsets_adding_to_total(input_data, 150)
    min_containers = min(container_counts.keys())
    return container_counts[min_containers]


def count_subsets_adding_to_total(values, sum_total):
    """
    Counts the number of subsets from the input values that add to the given
    total. Return value is dict containing how many times (value) n elements
    (key) were found to add up to exactly the given total.
    """
    container_counts = {}
    count_subsets_adding_to_total_recursive(
        values, sum_total, 0, 0, 0, container_counts)
    return container_counts


def count_subsets_adding_to_total_recursive(
        values, sum_total, i, current_total, total_containers, container_counts):
    """
    Resursively processes the values list to find the combinations of input
    elements adding up to the given total.
    """
    if current_total == sum_total:
        if total_containers not in container_counts:
            container_counts[total_containers] = 1
        else:
            container_counts[total_containers] += 1
    elif current_total < sum_total and i < len(values):
        count_subsets_adding_to_total_recursive(values, sum_total, i + 1,
                                                current_total + values[i],
                                                total_containers + 1,
                                                container_counts)
        count_subsets_adding_to_total_recursive(values, sum_total, i + 1,
                                                current_total, total_containers,
                                                container_counts)
