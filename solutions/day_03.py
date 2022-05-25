def main():
    input = generate_input()
    p1_solution = solve_part1(input)
    p2_solution = solve_part2(input)
    print("P1 solution - {}".format(p1_solution))
    print("P2 solution - {}".format(p2_solution))


def generate_input():
    with open("./inputs/day_03.txt") as file:
        input = file.read().strip()
        return input


def solve_part1(input) -> int:
    santa_pos = [0, 0]
    pos_visited = set()
    pos_visited.add(tuple(santa_pos))
    for c in input:
        match c:
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


def solve_part2(input) -> int:
    santa_pos = [0, 0]
    robosanta_pos = [0, 0]
    pos_visited = set()
    pos_visited.add(tuple(santa_pos))
    santa_move = True
    for c in input:
        match c:
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
        

if __name__ == "__main__":
    main()
