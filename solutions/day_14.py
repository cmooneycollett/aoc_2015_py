import re


class Reindeer:
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


def main():
    input = process_input_file()
    p1_solution = solve_part1(input)
    print("P1 solution - {}".format(p1_solution))
    p2_solution = solve_part2(input)
    print("P2 solution - {}".format(p2_solution))


def process_input_file():
    input = {}
    regex_reindeer = re.compile(
        r"^([A-Z][a-z]+) can fly (\d+) km/s for (\d+) seconds, but then must "
        r"rest for (\d+) seconds.$")
    with open("./inputs/day_14.txt") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            m = regex_reindeer.match(line)
            reindeer_name = m.group(1)
            speed = int(m.group(2))             # km/s
            travel_duration = int(m.group(3))   # seconds
            rest_duration = int(m.group(4))     # seconds
            input[reindeer_name] = (speed, travel_duration, rest_duration)
    return input


def solve_part1(input):
    """
    Calculates the total distance travelled by the winning reindeer.
    """
    race_duration = 2503    # seconds
    distances_traveled = {}
    for (reindeer_name, params) in input.items():
        # Calculate how many full travel periods are completed by reindeer, and spare seconds
        period_dur = params[1] + params[2]
        complete_periods_travels = race_duration // period_dur  # integer division required
        spare_seconds = race_duration % period_dur
        # Calculate total distance travelled
        distances_traveled[reindeer_name] = complete_periods_travels * \
            params[0] * params[1]
        if spare_seconds <= params[1]:
            distances_traveled[reindeer_name] += params[0] * spare_seconds
        else:
            distances_traveled[reindeer_name] += params[0] * params[1]
    return max(distances_traveled.values())


def solve_part2(input):
    """
    Calculates the total points awarded to the winning reindeer.
    """
    race_duration = 2503    # seconds
    # Create the reindeers
    reindeers = []
    points = {}
    for (reindeer_name, params) in input.items():
        reindeers.append(
            Reindeer(reindeer_name, params[0], params[1], params[2]))
        points[reindeer_name] = 0
    # Conduct reindeer race, awarding one point to lead reindeer after each second
    for _x in range(0, race_duration):
        running_distances = {}
        for i in range(0, len(reindeers)):
            reindeers[i].advance_one_second()
            running_distances[reindeers[i].name] = reindeers[i].distance_travelled
        # Find lead reindeers and award point/s
        lead_reindeers = []
        lead_distance = None
        for (reindeer_name, distance) in running_distances.items():
            distance = running_distances[reindeer_name]
            if lead_distance is None or distance > lead_distance:
                lead_distance = distance
                lead_reindeers = [reindeer_name]
            elif distance == lead_distance:
                lead_reindeers.append(reindeer_name)
        for reindeer_name in lead_reindeers:
            points[reindeer_name] += 1
    return max(points.values())


if __name__ == "__main__":
    main()
