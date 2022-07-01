"""
Solutions for AOC 2015 Day 19.
"""


import re


def process_input_file():
    """
    Processes the AOC 2015 Day 19 input file into the format required by the
    solver functions. The returned value is a tuple containing the input
    molecule string and the map of replacement recipes specified in the input
    file.
    """
    replacement_recipes = {}
    input_molecule = ""
    regex_recipe = re.compile(r"^([a-zA-Z]+) => ([a-zA-Z]+)$")
    with open("./input/day_19.txt", encoding="utf-8") as file:
        recipes_phase = True
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                recipes_phase = not recipes_phase
                continue
            if recipes_phase:   # Extract replacement recipes
                match_replacement = regex_recipe.match(line)
                find = match_replacement.group(1)
                replace = match_replacement.group(2)
                if find not in replacement_recipes:
                    replacement_recipes[find] = []
                replacement_recipes[find].append(replace)
            else:   # Extract input molecule
                input_molecule = line
    return (input_molecule, replacement_recipes)


def solve_part1(input_data):
    """
    Determines the number of unique molecules that can be created by conducting
    all possible replacements on the input molecule.
    """
    unique_outputs = set()
    input_molecule = input_data[0]
    replacement_recipes = input_data[1]
    for (find, replacements) in replacement_recipes.items():
        count = len(re.findall(find, input_molecule))
        for replace in replacements:
            replaced = 0
            for i in range(0, len(input_molecule)):
                if input_molecule[i:(i + len(find))] == find:
                    output = input_molecule[:i] + replace + \
                        input_molecule[i + len(find):]
                    unique_outputs.add(output)
                    # Stop if no further replacements possible
                    replaced += 1
                    if replaced == count:
                        break
    return len(unique_outputs)


def solve_part2(input_data):
    """
    Determines the fewest replacement steps required to build the input medicine
    molecule from a single electron "e".
    """
    molecule = str(input_data[0])
    reverse_replacements = reverse_replacement_recipes(input_data[1])
    total_steps = 0
    while True:
        # Check if we have reached the fully reduced molecule
        if molecule == "e":
            break
        # Find longest string that can be reverse-replaced
        from_str = ""
        for target_str in reverse_replacements:
            # Tie-broken by first target string given in problem input file
            if target_str in molecule and len(target_str) > len(from_str):
                from_str = target_str
        # Replace each occurrence, counting each as an additional step
        to_str = reverse_replacements[from_str]
        num_replacements = len(re.findall(from_str, molecule))
        molecule = molecule.replace(from_str, to_str)
        total_steps += num_replacements
    return total_steps


def reverse_replacement_recipes(recipes):
    """
    Reverses the relationship between the find and replace strings given in the
    replacement recipes - going from one-to-many, to a one-to-one relationship.
    """
    output = {}
    for (find, replacements) in recipes.items():
        for replace in replacements:
            output[replace] = find
    return output
