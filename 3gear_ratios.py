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


def find_all_unique_symbols(input_: str):
    symbols = set()
    for c in input_:
        if str.isdigit(c) or c == "." or c == "\n":
            continue
        symbols.add(c)
    print(f"found symbols are: {symbols}")
    return symbols

SYMBOLS = find_all_unique_symbols(EXAMPLE_SCHEMATIC)

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

def main(schematic: str):
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

if __name__ == "__main__":
    gear_ratio = main(EXAMPLE_SCHEMATIC)
    assert gear_ratio == 4361
    # find_all_unique_symbols(REAL_SCHEMATIC)
    # gear_ratio = main(REAL_SCHEMATIC)