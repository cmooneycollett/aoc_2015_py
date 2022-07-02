"""
Solutions for AOC 2015 Day 14.
"""


import re


class Reindeer:
    """
    Represents a single Reindeer involved in the race described in the AOC 2015
    Day 14 problem. The reindeer starts by travelling at its designated speed
    for its travel duration, then rests for its designated rest period until it
    re-enters the travel phase phase.
    """

    def __init__(self, name, speed, travel_duration, rest_duration):
        """
        Creates a new Reindeer that is within travel phase, without having
        travelled any distance yet.
        """
        self.name = name
        self.speed = speed
        self.travel_duration = travel_duration
        self.rest_duration = rest_duration
        self.is_travelling = True
        self.seconds_travelled = 0
        self.seconds_rested = 0
        self.distance_travelled = 0

    def advance_one_second(self):
        """
        Advances the Reindeer forward by one second in time, increasing distance
        travelled and switching between travel/rest phases as required.
        """
        if self.is_travelling:
            self.seconds_travelled += 1
            self.distance_travelled += self.speed   # Implicitly mult by 1 second
            if self.seconds_travelled == self.travel_duration:
                self.seconds_travelled = 0
                self.is_travelling = False      # Reindeer enters rest phase
        else:   # reindeer is resting
            self.seconds_rested += 1
            if self.seconds_rested == self.rest_duration:
                self.seconds_rested = 0
                self.is_travelling = True       # Reindeer enters travel phase

    def calculate_complete_cycles_and_spare_seconds(self, race_duration):
        """
        For the given race duration, calculates the total number of complete
        travel periods the reindeer will complete and the number of spare
        seconds for the final incomplete travel period. Return value is tuple
        containing these two values in order.
        """
        reindeer_cycle_duration = self.travel_duration + self.rest_duration
        complete_cycles = race_duration // reindeer_cycle_duration
        spare_seconds = race_duration % reindeer_cycle_duration
        return (complete_cycles, spare_seconds)

    def calculate_distance_travelled_in_race(self, race_duration):
        """
        Calculates the total distance the Reindeer would travel during a race
        for the specfied duration.
        """
        (complete_cycles, spare_seconds) = \
            self.calculate_complete_cycles_and_spare_seconds(race_duration)
        distance_travelled = complete_cycles * self.speed * self.travel_duration
        if spare_seconds <= self.travel_duration:
            distance_travelled += self.speed * spare_seconds
        else:
            distance_travelled += self.speed * self.travel_duration
        return distance_travelled


def process_input_file():
    """
    Processes the AOC 2015 Day 14 input file into the format required by the
    solver functions.
    """
    input_data = []
    regex_reindeer = re.compile(
        r"^([A-Z][a-z]+) can fly (\d+) km/s for (\d+) seconds, but then must "
        r"rest for (\d+) seconds.$")
    with open("./input/day_14.txt", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            match_reindeer = regex_reindeer.match(line)
            name = match_reindeer.group(1)
            speed = int(match_reindeer.group(2))             # km/s
            travel_duration = int(match_reindeer.group(3))   # seconds
            rest_duration = int(match_reindeer.group(4))     # seconds
            reindeer = Reindeer(name, speed, travel_duration, rest_duration)
            input_data.append(reindeer)
    return input_data


def solve_part1(input_data):
    """
    Solves AOC 2015 Day 14 Part 1 // Calculates the total distance travelled by
    the winning reindeer.
    """
    race_duration = 2503    # seconds
    distances_travelled = []
    for reindeer in input_data:
        distance = reindeer.calculate_distance_travelled_in_race(race_duration)
        distances_travelled.append(distance)
    return max(distances_travelled)


def solve_part2(input_data):
    """
    Solves AOC 2015 Day 14 Part 2 // Calculates the total points awarded to the
    winning reindeer.
    """
    race_duration = 2503    # seconds
    # Create the reindeers
    reindeers = input_data
    points = {}
    for reindeer in input_data:
        points[reindeer.name] = 0
    # Conduct reindeer race, awarding one point to lead reindeer after each second
    for _ in range(0, race_duration):
        # Advance each reindeer by one second and record their travelled dist
        running_distances = {}
        for reindeer in reindeers:
            reindeer.advance_one_second()
            running_distances[reindeer.name] = reindeer.distance_travelled
        # Determine the lead reindeer/s and award them each one point
        lead_reindeers = []
        lead_distance = None
        for (reindeer_name, distance) in running_distances.items():
            if lead_distance is None or distance > lead_distance:
                lead_distance = distance
                lead_reindeers = [reindeer_name]
            elif distance == lead_distance:
                lead_reindeers.append(reindeer_name)
        for reindeer_name in lead_reindeers:
            points[reindeer_name] += 1
    return max(points.values())
