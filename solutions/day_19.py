import re


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    replacement_recipes = {}
    input_molecule = ""
    regex_recipe = re.compile(r"^([a-zA-Z]+) => ([a-zA-Z]+)$")
    with open("./inputs/day_19.txt") as file:
        recipes_phase = True
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                recipes_phase = not recipes_phase
                continue
            if recipes_phase:
                m = regex_recipe.match(line)
                find = m.group(1)
                replace = m.group(2)
                if find not in replacement_recipes:
                    replacement_recipes[find] = []
                replacement_recipes[find].append(replace)
            else:
                input_molecule = line
    return (input_molecule, replacement_recipes)


def solve_part1(input):
    unique_outputs = set()
    input_molecule = input[0]
    replacement_recipes = input[1]
    for (find, replacements) in replacement_recipes.items():
        count = len(re.findall(find, input_molecule))
        for replace in replacements:
            replaced = 0
            for i in range(0, len(input_molecule)):
                if input_molecule[i:(i + len(find))] == find:
                    output = input_molecule[:i] + replace + input_molecule[i + len(find):]
                    unique_outputs.add(output)
                    # Stop if no further replacements possible
                    replaced += 1
                    if replaced == count:
                        break
    return len(unique_outputs)


def solve_part2(input):
    ()


def replace_nth_occurrence(input_str, find, replace, n):
    f_index = input_str.find(find)
    i = 1
    while True:
        if f_index == -1:
            break
        if i == n:
            output = input_str[:f_index] + replace + input_str[f_index + len(find):]
            return output
        else:
            f_index = input_str.find(find, f_index + len(find) + 1)
            i += 1
    return input_str


if __name__ == "__main__":
    main()
