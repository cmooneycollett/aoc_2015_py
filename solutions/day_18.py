"""
Solutions for AOC 2015 Day 18.
"""


from copy import deepcopy


def main():
    """
    Solves AOC 2015 Day 18 Parts 1 and 2, printing out the solutions.
    """
    input_data = process_input_file()
    p1_solution = solve_part1(input_data)
    print(f"P1 solution - {p1_solution}")
    p2_solution = solve_part2(input_data)
    print(f"P2 solution - {p2_solution}")


def process_input_file():
    """
    Processes the AOC 2015 Day 18 input file into the format required by the
    solver functions. Returned data structure is a 2D list
    """
    input_data = []
    with open("./inputs/day_18.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            input_data.append(list(line))
    return input_data


def solve_part1(input_data):
    """
    Takes the input lightgrid and conducts 100 steps, returning the number of
    cells that are left lit at the end.
    """
    grid = animate_light_grid(input_data, 100)
    return sum(x.count("#") for x in grid)


def solve_part2(input_data):
    """
    Takes the input lightgrid and conducts 100 steps with the four corner cells
    stuck in the "on" setting, returning the number of cells that are left lit
    at the end.
    """
    # Set the input grid corners to initially be on
    input_grid = deepcopy(input_data)
    input_grid[0][0] = "#"      # x: 0, y: 0
    input_grid[0][99] = "#"     # x: 99, y: 0
    input_grid[99][0] = "#"     # x: 0, y: 99
    input_grid[99][99] = "#"    # x: 99, y: 99
    grid = animate_light_grid(input_grid, 100, corner_lights_stuck_on=True)
    return sum(x.count("#") for x in grid)


def animate_light_grid(input_grid, steps, corner_lights_stuck_on=False):
    """
    Takes the input lightgrid and conducts the given number of steps, with the
    corner lights stuck on if set to True.
    """
    grid = input_grid
    for _ in range(0, steps):
        new_grid = []
        for (loc_y, row) in enumerate(grid):
            new_grid.append([])
            for (loc_x, state) in enumerate(row):
                if corner_lights_stuck_on and (
                        loc_x == 0 and loc_y == 0 or loc_x == 99 and loc_y == 0 or
                        loc_x == 0 and loc_y == 99 or loc_x == 99 and loc_y == 99):
                    new_grid[loc_y].append("#")
                    continue
                # Determine state of cell of new grid
                neighbour_states = count_neighbour_states(grid, loc_x, loc_y)
                match state:
                    case "#":  # Light is currently on
                        if neighbour_states["#"] == 2 or neighbour_states["#"] == 3:
                            new_grid[loc_y].append("#")
                        else:
                            new_grid[loc_y].append(".")
                    case ".":  # Light is currently off
                        if neighbour_states["#"] == 3:
                            new_grid[loc_y].append("#")
                        else:
                            new_grid[loc_y].append(".")
        grid = new_grid
    return grid


def calculate_surrounding_locations(loc_x, loc_y, x_min, y_min, x_max, y_max):
    """
    Calculates the (x, y) locations surrounding the specified point, limited by
    the given minimum and maximum x and y values (inclusive).
    """
    output = []
    for y_delta in [-1, 0, 1]:
        new_y = loc_y + y_delta
        if new_y < y_min or new_y > y_max:
            continue
        for x_delta in [-1, 0, 1]:
            new_x = loc_x + x_delta
            if new_x < x_min or new_x > x_max or y_delta == 0 and x_delta == 0:
                continue
            output.append((new_x, new_y))
    return output


def count_neighbour_states(lightgrid, loc_x, loc_y):
    """
    Returns a count of the cell states surrounding the given location in the
    lightgrid.
    """
    output = {"#": 0, ".": 0}
    surrounding_points = calculate_surrounding_locations(
        loc_x, loc_y, 0, 0, len(lightgrid) - 1, len(lightgrid) - 1)
    for (x_0, y_0) in surrounding_points:
        output[lightgrid[y_0][x_0]] += 1
    return output


if __name__ == "__main__":
    main()
