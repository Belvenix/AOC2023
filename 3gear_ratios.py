EXAMPLE_SCHEMATIC = \
"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


GEAR = "*"
SYMBOLS = set(["%", "&", "#", "-", "+", "=", "@", GEAR, "$", "/"])


def find_all_unique_symbols(input_: str):
    symbols = set()
    for c in input_:
        if str.isdigit(c) or c == "." or c == "\n":
            continue
        symbols.add(c)
    print(f"found symbols are: {symbols}")
    return symbols


def is_outside(grid: list[list[str]], i: int, j: int):
    heigth, width = len(grid), len(grid[0])
    if 0 > i or i >= heigth:
        return True
    if 0 > j or j >= width:
        return True
    
    return False

def is_near_symbol(grid: list[list[str]], digit_i: int, digit_j: int, digits: int) -> bool:
    if digit_j < 0:
        digit_j = len(grid[0]) - digits
        digit_i -= 1
    search_i, search_j = range(digit_i - 1, digit_i + 2), range(digit_j - 1, digit_j + digits + 1)
    grid_part = ""
    found = False
    for i in search_i:
        for j in search_j:
            if is_outside(grid, i, j):
                grid_part = ''.join([grid_part, "?"])
                continue
            c = grid[i][j]
            grid_part = ''.join([grid_part, c])
            if c in SYMBOLS:
                found =  True
        grid_part = ''.join([grid_part,"\n"])
    if found:
        print(f"The number is near symbol.")
    print(f"the grid part looks like this: \n{grid_part}")
    return found


def first_part(schematic: str):
    current_digit = None
    gear_ratio = 0
    grid = [c for c in [line for line in schematic.splitlines()]]
    heigth, width = len(grid), len(grid[0])
    for i in range(heigth):
        for j in range(width):
            c = grid[i][j]
            if not str.isdigit(c):
                if current_digit is not None:
                    n_digits = len(current_digit)
                    current_digit = int(current_digit)
                    if j == 0:
                        print(f"Found number: {current_digit} at ({i-1},{width - n_digits})")
                    else:
                        print(f"Found number: {current_digit} at ({i},{j - n_digits})")
                    if is_near_symbol(grid, i, j - n_digits, n_digits):
                        gear_ratio += current_digit
                    current_digit = None
            else:
                current_digit = ''.join([current_digit or '', c])
    print(f"Calculated gear ratio is: {gear_ratio}")
    return gear_ratio


def find_all_gears(grid: list[list[str]]) -> list[tuple[int, int]]:
    gear_positions = []
    heigth, width = len(grid), len(grid[0])
    for i in range(heigth):
        for j in range(width):
            if grid[i][j] == GEAR:
                gear_positions.append((i, j))
    return gear_positions


def find_all_digits(grid: list[list[str]]):
    found_digits = []
    current_digit = None
    heigth, width = len(grid), len(grid[0])
    for i in range(heigth):
        for j in range(width):
            c = grid[i][j]
            if not str.isdigit(c):
                if current_digit is not None:
                    n_digits = len(current_digit)
                    current_digit = int(current_digit)
                    if j == 0:
                        digit_i_position, digit_j_position = i - 1, width - n_digits
                    else:
                        digit_i_position, digit_j_position = i, j - n_digits
                    # print(f"Found number: {current_digit} at ({digit_i_position},{digit_j_position})")
                    if is_near_symbol(grid, digit_i_position, digit_j_position, n_digits):
                        found_digits.append((current_digit, (digit_i_position, digit_j_position, n_digits)))
                    current_digit = None
            else:
                current_digit = ''.join([current_digit or '', c])
    return found_digits


def is_part_overlapping_gear(part: tuple[int, tuple[int, int, int]], gear: tuple[int, int]):
    gear_i, gear_j = range(gear[0] - 1, gear[0] + 2), range(gear[1] - 1, gear[1] + 2)
    _, (part_i, part_j, part_len) = part
    for i in gear_i:
        for j in gear_j:
            part_positions = [(part_i, p_j) for p_j in range(part_j, part_j + part_len)]
            if (i, j) in part_positions:
                return True
    else:
        return False


def find_overlapping_parts(parts: list[tuple[int, tuple[int, int, int]]], gear: tuple[int, int]):
    overlapping_parts = []
    for part in parts:
        if is_part_overlapping_gear(part, gear):
            overlapping_parts.append(part)
    return overlapping_parts


def second_part(schematic: str) -> int:
    grid = [c for c in [line for line in schematic.splitlines()]]
    gears = find_all_gears(grid)
    parts = find_all_digits(grid)
    # print(f"The gears are: {gears}")
    # print(f"The found parts are: {parts}")
    gear_ratio = 0
    for gear in gears:
        overlapping_parts = find_overlapping_parts(parts, gear)
        if len(overlapping_parts) == 2:
            # print(f"Adding combined parts: {overlapping_parts}")
            gear_ratio += overlapping_parts[0][0] * overlapping_parts[1][0]
    print(f"Found gear ratio is: {gear_ratio}")
    return gear_ratio


if __name__ == "__main__":
    gear_ratio = first_part(EXAMPLE_SCHEMATIC)
    assert gear_ratio == 4361
    gear_ratio = second_part(EXAMPLE_SCHEMATIC)
    assert gear_ratio == 467835
