FIRST_VALIDATION_STRING = \
"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

VALID_CUBE_COUNTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def get_game_points(game: str) -> int:
    game_id, rounds = game.split(":")
    game_id = int(game_id.removeprefix("Game "))
    for round in rounds.split(";"):
        cubes = round.split(",")
        for cube in cubes:
            count, color = cube.split()
            if VALID_CUBE_COUNTS.get(color) < int(count):
                return 0
    else:
        return game_id

def check_possible_games(input_string: str):
    sum_of_ids = 0
    for game in input_string.splitlines():
        if not game:
            continue
        sum_of_ids += get_game_points(game)
    return sum_of_ids

if __name__ == "__main__":
    actual_value = check_possible_games(FIRST_VALIDATION_STRING)
    expected_value = 8
    assert actual_value == expected_value