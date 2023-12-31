from collections.abc import Callable

VALIDATION_STRING = """
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
    for game_round in rounds.split(";"):
        cubes = game_round.split(",")
        for cube in cubes:
            count, color = cube.split()
            if VALID_CUBE_COUNTS.get(color) < int(count):
                return 0
    return game_id


def get_game_power(game: str) -> int:
    _, rounds = game.split(":")
    color_minimums = {key: 0 for key in VALID_CUBE_COUNTS}
    for game_round in rounds.split(";"):
        cubes = game_round.split(",")
        for cube in cubes:
            count, color = cube.split()
            if color_minimums.get(color) < int(count):
                color_minimums[color] = int(count)
    cube_power = 1
    for color_counts in color_minimums.values():
        cube_power *= color_counts
    return cube_power


def reducer(input_string: str, summation_func: Callable[[str], int]):
    value = 0
    for game in input_string.splitlines():
        if not game:
            continue
        value += summation_func(game)
    return value


if __name__ == "__main__":
    actual_value = reducer(VALIDATION_STRING, get_game_points)
    expected_value = 8
    assert actual_value == expected_value
    actual_cube_power = reducer(VALIDATION_STRING, get_game_power)
    expected_cube_power = 2286
    assert actual_cube_power == expected_cube_power
