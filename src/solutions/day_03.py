"""
Solutions for AOC 2015 Day 3.
"""


def process_input_file():
    """
    Processes the AOC 2015 Day 3 input file into format for solver functions.
    """
    with open("./input/day_03.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_data):
    """
    Solves AOC 2015 Day 3 Part 1 // Calculates the number of houses that receive
    at least one present, after Santa travels along path specified in input.
    """
    santa_pos = [0, 0]
    pos_visited = set()
    pos_visited.add(tuple(santa_pos))
    for char in input_data:
        match char:
            case '^':
                santa_pos[1] -= 1
            case '>':
                santa_pos[0] += 1
            case 'v':
                santa_pos[1] += 1
            case '<':
                santa_pos[0] -= 1
        pos_visited.add(tuple(santa_pos))
    return len(pos_visited)


def solve_part2(input_data):
    """
    Solves AOC 2015 Day 3 Part 2 // Calculates the number of houses that receive
    at least one present, after Santa and Robo-Santa take alternating moves
    taken from input.
    """
    santa_pos = [0, 0]
    robosanta_pos = [0, 0]
    pos_visited = set()
    pos_visited.add(tuple(santa_pos))
    santa_move = True
    for char in input_data:
        match char:
            case '^':
                if santa_move:
                    santa_pos[1] -= 1
                else:
                    robosanta_pos[1] -= 1
            case '>':
                if santa_move:
                    santa_pos[0] += 1
                else:
                    robosanta_pos[0] += 1
            case 'v':
                if santa_move:
                    santa_pos[1] += 1
                else:
                    robosanta_pos[1] += 1
            case '<':
                if santa_move:
                    santa_pos[0] -= 1
                else:
                    robosanta_pos[0] -= 1
        if santa_move:
            pos_visited.add(tuple(santa_pos))
            santa_move = False
        else:
            pos_visited.add(tuple(robosanta_pos))
            santa_move = True
    return len(pos_visited)
