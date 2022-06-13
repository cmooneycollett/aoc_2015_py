from dataclasses import dataclass
import itertools
import math


class Entity:
    def __init__(self, hp, damage, armour):
        self.hp = hp
        self.damage = damage
        self.armour = armour

    def is_dead(self):
        return self.hp <= 0

    def calculate_turns_to_defeat(self, other):
        # Calculate damage per turn
        damage_per_turn = self.damage - other.armour
        if damage_per_turn < 1:
            damage_per_turn = 1
        # Calculate turns required to defeat the other entity
        turns = int(math.ceil(other.hp / damage_per_turn))
        return turns


@dataclass
class ItemStats:
    cost: int
    damage: int
    armour: int


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    with open("./inputs/day_21.txt") as file:
        stats = []
        for line in file.readlines():
            line = line.strip()
            stat = int(line.split(": ")[1])
            stats.append(stat)
            if len(stats) == 3:
                break
        boss_entity = Entity(stats[0], stats[1], stats[2])
        return boss_entity


def solve_part1(input):
    """
    Determines the minimum cost of items the player can purchase and still
    defeat the boss.
    """
    boss_entity = input
    item_stat_combos = determine_item_combinations()
    min_cost = process_combos(item_stat_combos, boss_entity, True)
    return min_cost


def solve_part2(input):
    """
    Determines the maximum cost of items the player can purchase and still lose
    the boss fight.
    """
    boss_entity = input
    item_stat_combos = determine_item_combinations()
    min_cost = process_combos(item_stat_combos, boss_entity, False)
    return min_cost


def generate_items():
    """
    Generates the items available in the game item shop.
    """
    items = {}
    # Generate weapons
    items["Weapons"] = {}
    items["Weapons"]["Dagger"] = ItemStats(8, 4, 0)
    items["Weapons"]["Shortsword"] = ItemStats(10, 5, 0)
    items["Weapons"]["Warhammer"] = ItemStats(25, 6, 0)
    items["Weapons"]["Longsword"] = ItemStats(40, 7, 0)
    items["Weapons"]["Greataxe"] = ItemStats(74, 8, 0)
    # Generate armour
    items["Armour"] = {}
    items["Armour"]["Leather"] = ItemStats(13, 0, 1)
    items["Armour"]["Chainmail"] = ItemStats(31, 0, 2)
    items["Armour"]["Splintmail"] = ItemStats(53, 0, 3)
    items["Armour"]["Bandedmail"] = ItemStats(75, 0, 4)
    items["Armour"]["Platemail"] = ItemStats(102, 0, 5)
    # Generate rings
    items["Rings"] = {}
    items["Rings"]["Damage + 1"] = ItemStats(25, 1, 0)
    items["Rings"]["Damage + 2"] = ItemStats(50, 2, 0)
    items["Rings"]["Damage + 3"] = ItemStats(100, 3, 0)
    items["Rings"]["Defense + 1"] = ItemStats(20, 0, 1)
    items["Rings"]["Defense + 2"] = ItemStats(40, 0, 2)
    items["Rings"]["Defense + 3"] = ItemStats(80, 0, 3)
    return items


def determine_item_combinations():
    """
    Determines the possible combinations of the items the player can purchase
    from the store. Player most purchase 1 weapon, may purchase up to 1 armour
    and may purchase up to 2 rings.
    """
    items = generate_items()
    weapons = items["Weapons"]
    armour = items["Armour"]
    rings = items["Rings"]
    # Determine all possible combinations of items
    two_ring_combos = list(itertools.combinations(rings.values(), 2))
    # Combos: Weapon + 0 Armour + 0 Rings
    w_0a_0r_combos = [[a] for a in weapons.values()]
    # Combos: Weapon + Armour + 0 Rings
    w_a_0r_combos = itertools.product(weapons.values(), armour.values())
    w_a_0r_combos = [[a, b] for (a, b) in w_a_0r_combos]
    # Combos: Weapon + Armour + Rings
    w_a_r_combos = itertools.product(w_a_0r_combos, rings.values())
    w_a_r_combos = [[a, b, c] for ((a, b), c) in w_a_r_combos]
    # Combos: Weapon + 0 Armour + 1 Ring
    w_0a_r_combos = itertools.product(weapons.values(), rings.values())
    w_0a_r_combos = [[a, b] for (a, b) in w_0a_r_combos]
    # Combos: Weapon + Armour + 2 Rings
    w_a_2r_combos = itertools.product(w_a_0r_combos, two_ring_combos)
    w_a_2r_combos = [[a, b, c, d] for ((a, b), (c, d)) in w_a_2r_combos]
    # Combos: Weapon + 0 Armour + 2 Rings
    w_0a_2r_combos = itertools.product(weapons.values(), two_ring_combos)
    w_0a_2r_combos = [[a, b, c] for (a, (b, c)) in w_0a_2r_combos]
    return w_a_0r_combos + w_0a_0r_combos + w_a_r_combos + w_0a_r_combos + \
        w_a_2r_combos + w_0a_2r_combos


def determine_combo_cost(item_stat_combo, boss_entity, player_win):
    """
    Returns a tuple containing the outcome of the player/boss fight and the cost
    of the items in the item combo.
    """
    cost = 0
    player_entity = Entity(100, 0, 0)
    for item_stat in item_stat_combo:
        cost += item_stat.cost
        player_entity.damage += item_stat.damage
        player_entity.armour += item_stat.armour
    player_turns = player_entity.calculate_turns_to_defeat(boss_entity)
    boss_turns = boss_entity.calculate_turns_to_defeat(player_entity)
    if player_win and player_turns <= boss_turns or \
            not player_win and boss_turns < player_turns:
        return (True, cost)
    else:
        return (False, cost)


def process_combos(item_stat_combos, boss_entity, player_win):
    """
    Determines the min or max cost encountered for the playuer to win or lose
    the fight with the boss.
    """
    target_cost = None
    for combo in item_stat_combos:
        (desired_outcome, cost) = determine_combo_cost(
            combo, boss_entity, player_win)
        if not desired_outcome:
            continue
        if target_cost is None:
            target_cost = cost
        elif player_win and cost < target_cost:
            target_cost = cost
        elif not player_win and cost > target_cost:
            target_cost = cost
    return target_cost


if __name__ == "__main__":
    main()
