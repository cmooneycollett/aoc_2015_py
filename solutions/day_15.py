import re
from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    input = []
    regex_ingredient = re.compile(
        r"^([a-zA-Z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), "
        r"texture (-?\d+), calories (-?\d+)$")
    with open("./inputs/day_15.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            m = regex_ingredient.match(line)
            name = m.group(1)
            capacity = int(m.group(2))
            durability = int(m.group(3))
            flavor = int(m.group(4))
            texture = int(m.group(5))
            calories = int(m.group(6))
            ingredient = Ingredient(
                name, capacity, durability, flavor, texture, calories)
            input.append(ingredient)
    return input


def solve_part1(input):
    """
    Finds the total score for the highest-scoring cookie by combining the input
    ingredients, using exactly 100 units (tsp) of ingredients total.
    """
    max_cookie_score = None
    for n0 in range(0, 100):    # sprinkes
        for n1 in range(0, 100 - n0):   # peanutbutter
            for n2 in range(0, 100 - n0 - n1):  # frosting
                n3 = 100 - n0 - n1 - n2 # sugar
                # Calculate parameter scores
                score_c = input[0].capacity * n0 + input[1].capacity * \
                    n1 + input[2].capacity * n2 + input[3].capacity * n3
                score_d = input[0].durability * n0 + input[1].durability * \
                    n1 + input[2].durability * n2 + input[3].durability * n3
                score_f = input[0].flavor * n0 + input[1].flavor * \
                    n1 + input[2].flavor * n2 + input[3].flavor * n3
                score_t = input[0].texture * n0 + input[1].texture * \
                    n1 + input[2].texture * n2 + input[3].texture * n3
                # Calculate cookie score
                cookie_score = 0
                if score_c > 0 and score_d > 0 and score_f > 0 and score_t > 0:
                    cookie_score = score_c * score_d * score_f * score_t
                if max_cookie_score is None or cookie_score > max_cookie_score:
                    max_cookie_score = cookie_score
    return max_cookie_score


def solve_part2(input):
    ()


if __name__ == "__main__":
    main()
