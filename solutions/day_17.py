def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    with open("./inputs/day_17.txt") as file:
        lines = [line.strip()
                 for line in file.readlines() if len(line.strip()) > 0]
        return [int(n) for n in lines]


def solve_part1(input):
    return count_subsets_adding_to_total(input, 150)


def solve_part2(input):
    ()


def count_subsets_adding_to_total(values, sum_total):
    subset_count = count_subsets_adding_to_total_recursive(
        values, sum_total, 0, 0)
    return subset_count


def count_subsets_adding_to_total_recursive(values, sum_total, i, current_total):
    subset_count = 0
    if current_total == sum_total:
        subset_count += 1
    elif current_total < sum_total and i < len(values):
        subset_count += count_subsets_adding_to_total_recursive(
            values, sum_total, i + 1, current_total + values[i])
        subset_count += count_subsets_adding_to_total_recursive(
            values, sum_total, i + 1, current_total)
    return subset_count


if __name__ == "__main__":
    main()
