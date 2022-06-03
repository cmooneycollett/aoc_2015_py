def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    input = []
    with open("./inputs/day_18.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            input.append(list(line))
    return input


def solve_part1(input):
    grid = input
    for _x in range(0, 100):
        new_grid = []
        for y in range(0, 100):
            new_grid.append([])
            for x in range(0, 100):
                # Determine state of cell of new grid
                neighbour_states = count_neighbour_states(grid, x, y)
                match grid[y][x]:
                    case "#":  # Light is currently on
                        if neighbour_states["#"] == 2 or neighbour_states["#"] == 3:
                            new_grid[y].append("#")
                        else:
                            new_grid[y].append(".")
                    case ".":  # Light is currently off
                        if neighbour_states["#"] == 3:
                            new_grid[y].append("#")
                        else:
                            new_grid[y].append(".")
        grid = new_grid
    return sum(x.count("#") for x in grid)


def solve_part2(input):
    ()


def calculate_surrounding_locations(x, y, x_min, y_min, x_max, y_max):
    output = []
    for y_delta in [-1, 0, 1]:
        new_y = y + y_delta
        if new_y < y_min or new_y > y_max:
            continue
        for x_delta in [-1, 0, 1]:
            new_x = x + x_delta
            if new_x < x_min or new_x > x_max or y_delta == 0 and x_delta == 0:
                continue
            output.append((new_x, new_y))
    return output


def count_neighbour_states(grid, x, y):
    output = {"#": 0, ".": 0}
    surrounding_points = calculate_surrounding_locations(x, y, 0, 0, 99, 99)
    for (x_0, y_0) in surrounding_points:
        output[grid[y_0][x_0]] += 1
    return output


if __name__ == "__main__":
    main()
