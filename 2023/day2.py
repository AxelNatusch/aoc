def get_input():
    with open("data/day2.txt") as f:
        return f.readlines()


def part1():
    total_sum = 0
    for line in get_input():
        line = line.strip("\n")
        x = line.split(":")
        key = x[0]
        num_of_key = key.split(" ")[1]
        values = x[1].split(";")

        for value in values:
            x = value.split(", ")
            for y in x:
                y = y.strip().split(" ")
                if y[1] == "green":
                    if int(y[0]) >= 13:
                        break
                elif y[1] == "red":
                    if int(y[0]) >= 12:
                        break
                elif y[1] == "blue":
                    if int(y[0]) >= 14:
                        break

        total_sum += int(num_of_key)

    print(total_sum)


# The maximum numbers of red, green, and blue cubes available
max_cubes = {"red": 12, "green": 13, "blue": 14}


# Function to check if a game is possible
def is_game_possible(game_data):
    for round in game_data:
        counts = {"red": 0, "green": 0, "blue": 0}
        for color_count in round.split(", "):
            count, color = color_count.split(" ")
            counts[color] += int(count)
            if counts[color] > max_cubes[color]:
                return False
    return True


# Function to process the games data from the file
def process_games_data():
    games_data = get_input()
    possible_game_ids = []
    for game in games_data:
        game_id, data = game.strip().split(": ", 1)
        game_id = int(game_id.split(" ")[1])  # Extract the game ID
        if is_game_possible(data.split("; ")):
            possible_game_ids.append(game_id)
    return sum(possible_game_ids)


def find_minimum_cubes(game_data):
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for round in game_data:
        round_cubes = {"red": 0, "green": 0, "blue": 0}
        for color_count in round.split(", "):
            count, color = color_count.split(" ")
            round_cubes[color] = max(round_cubes[color], int(count))
        for color in min_cubes:
            min_cubes[color] = max(min_cubes[color], round_cubes[color])
    return min_cubes


def calculate_total_power(games_data):
    total_power = 0
    for game in games_data:
        _, data = game.strip().split(": ", 1)
        min_cubes = find_minimum_cubes(data.split("; "))
        power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
        total_power += power
    return total_power


def main():
    games_data = get_input()
    total_power = calculate_total_power(games_data)
    print(f"Total Power: {total_power}")


if __name__ == "__main__":
    main()
