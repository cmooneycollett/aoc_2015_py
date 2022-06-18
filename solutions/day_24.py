import itertools
import math


def main():
    input = process_input_file()
    # p1_solution = solve_part1(input)
    # print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    with open("./inputs/day_24.txt") as file:
        return [int(x.strip()) for x in file.readlines() if len(x.strip()) > 0]


def solve_part1(input):
    """
    Finds the minimum quantum entangement for compartment 1 (passenger
    compartment) in the optimal arrangement, when dividing the values across
    three separate compartments with equal sums.
    """
    total = sum(input)
    min_qe = find_min_qe_comp_1(input, total // 3)
    return min_qe


def solve_part2(input):
    """
    Finds the minimum quantum entangement for compartment 1 (passenger
    compartment) in the optimal arrangement, when dividing the values across
    four separate compartments with equal sums.
    """
    total = sum(input)
    min_qe = find_min_qe_comp_1(input, total // 4)
    return min_qe


def find_min_qe_comp_1(values, limit):
    """
    Finds the minimum quantum entanglement for compartment 1 (passenger
    compartment) in the optimal arrangement (fewest possible packages). The
    subsets considered are only those that are found to add to exactly the given
    limit.
    """
    min_len = []
    min_qe = []
    find_min_qe_comp_1_recursive(values, limit, [], 0, 0, min_len, min_qe)
    if len(min_qe) == 1:
        return min_qe[0]
    else:
        return -1


def find_min_qe_comp_1_recursive(
        values, limit, running_list, index, sum, min_len, min_qe):
    """
    Recursive helper for finding minimum quantum entanglement for optimal
    arrangement. Keeps track of the running list of the subset as subsequent
    recursive calls step through the values list.
    """
    # Check if limit has been reached or exceeded
    if sum == limit:
        if len(min_len) == 0:
            min_len.append(len(running_list))
            min_qe.append(math.prod(running_list))
        elif min_len[0] > len(running_list):
            min_len[0] = len(running_list)
            min_qe[0] = math.prod(running_list)
        elif min_len[0] == len(running_list):
            prod = math.prod(running_list)
            if min_qe[0] > prod:
                min_qe[0] = prod
        return
    elif sum > limit or index >= len(values):
        return
    # Select and not select
    new_running_list = list(running_list)
    new_running_list.append(values[index])
    # Select
    find_min_qe_comp_1_recursive(values, limit, new_running_list, index + 1,
                                 sum + values[index], min_len, min_qe)
    # Not select
    find_min_qe_comp_1_recursive(values, limit, running_list, index + 1, sum,
                                 min_len, min_qe)


if __name__ == "__main__":
    main()
