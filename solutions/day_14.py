import re


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
    race_duration = 2503    # seconds
    distances_traveled = {}
    for reindeer_name in input.keys():
        params = input[reindeer_name]
        # Calculate how many full travel periods are completed by reindeer, and spare seconds
        period_dur = params[1] + params[2]
        complete_periods_travels = race_duration // period_dur  # integer division required
        spare_seconds = race_duration % period_dur
        # Calculate total distance travelled
        distances_traveled[reindeer_name] = complete_periods_travels * params[0] * params[1]
        if spare_seconds <= params[1]:
            distances_traveled[reindeer_name] += params[0] * spare_seconds
        else:
            distances_traveled[reindeer_name] += params[0] * params[1]
    return max(distances_traveled.values())


def solve_part2(input):
    ()


if __name__ == "__main__":
    main()
