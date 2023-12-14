import logging
from copy import deepcopy
from enum import Enum
from itertools import combinations

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)

EXAMPLE_COSMOS = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

EXAMPLE_COSMOS_DISTANCE = 374

EXAMPLE_COSMIC_X10_DISTANCE = 1030
EXAMPLE_COSMIC_X100_DISTANCE = 8410


class SpaceType(Enum):
    EMPTY = "."
    GALAXY = "#"


class Space:
    def __init__(self, type_: SpaceType, x: int, y: int) -> None:
        self.type_ = type_
        self.x, self.y = x, y

    def set_coords(self, x: int, y: int):
        self.x, self.y = x, y

    def __str__(self):
        return self.type_.value


class Grid:
    def __init__(self, input_: str):
        self.grid: list[list[Space]] = []
        for y, line in enumerate(input_.splitlines()):
            self.grid.append(
                [Space(SpaceType(s), x, y) for x, s in enumerate(line) if s],
            )
            self.height = len(self.grid)
            self.width = len(self.grid[0])
        self.big_grid = None
        self.big_height, self.big_width = None, None
        self.small_galaxy_finder = []
        self.big_galaxy_finder = []

    def display(self, big: bool = False):
        iterable = self.big_grid if big else self.grid
        for line in iterable:
            space_line = ""
            for space in line:
                space_line += str(space)
            logging.debug(space_line)

    def expand_galaxy(self):
        self.big_grid = deepcopy(self.grid)
        found_rows, found_columns = self._find_empty_lines()
        self._expand(found_rows, found_columns)
        self._fix_expanded_galaxy_coordinates_and_get_galaxies()

    def calculate_greatly_expanded_galaxy(self, dist: int | None = None):
        found_rows, found_columns = self._find_empty_lines()
        found_galaxies = self._find_all_galaxies()
        return self._greatly_expand_galaxies(
            found_rows,
            found_columns,
            found_galaxies,
            dist,
        )

    def _greatly_expand_galaxies(
        self,
        found_rows: list[int],
        found_columns: list[int],
        found_galaxies: list[tuple[int, int]],
        universe_age_dist: int,
    ):
        # find all empty rows and columns between galaxy A and galaxy B
        # for each of the found rows and columns add 1_000_000 to the distance between them...
        if universe_age_dist is None:
            universe_age_dist = 999_999
        galaxy_coordinates_pairs: list[tuple[tuple[int, int], tuple[int, int]]] = list(
            combinations(found_galaxies, 2),
        )
        galaxy_lengths_sum = 0
        for (ga_x, ga_y), (gb_x, gb_y) in galaxy_coordinates_pairs:
            extra_distance = 0
            for col in found_columns:
                if ga_x < col < gb_x or gb_x < col < ga_x:
                    extra_distance += universe_age_dist

            for row in found_rows:
                if ga_y < row < gb_y or gb_y < row < ga_y:
                    extra_distance += universe_age_dist

            galaxy_lengths_sum += abs(ga_x - gb_x) + abs(ga_y - gb_y) + extra_distance
        return galaxy_lengths_sum

    def _find_all_galaxies(self):
        small_galaxy_finder = []
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].type_ == SpaceType.GALAXY:
                    small_galaxy_finder.append((x, y))
        return small_galaxy_finder

    def calculate_distances_between_galaxies(self) -> int:
        galaxy_coordinates_pairs: list[tuple[tuple[int, int], tuple[int, int]]] = list(
            combinations(self.big_galaxy_finder, 2),
        )
        galaxy_lengths_sum = 0
        for galaxy_a, galaxy_b in galaxy_coordinates_pairs:
            galaxy_lengths_sum += abs(galaxy_a[0] - galaxy_b[0]) + abs(
                galaxy_a[1] - galaxy_b[1],
            )
        return galaxy_lengths_sum

    def _expand(self, found_rows: list[int], found_columns: list[int]):
        i = 0
        for row in found_rows:
            self.big_grid.insert(
                row + i,
                [Space(SpaceType.EMPTY, None, None) for _ in range(self.width)],
            )
            i += 1
        self.big_height = len(self.big_grid)

        j = 0
        for col in found_columns:
            for row in range(self.big_height):
                self.big_grid[row].insert(col + j, Space(SpaceType.EMPTY, None, None))
            j += 1
        self.big_width = len(self.big_grid[0])

    def _fix_expanded_galaxy_coordinates_and_get_galaxies(self):
        for y in range(self.big_height):
            for x in range(self.big_width):
                self.big_grid[y][x].set_coords(x, y)
                if self.big_grid[y][x].type_ == SpaceType.GALAXY:
                    self.big_galaxy_finder.append((x, y))

    def _find_empty_lines(self):
        found_rows, found_columns = [], []
        for y in range(self.height):
            if all(self.grid[y][x].type_ == SpaceType.EMPTY for x in range(self.width)):
                found_rows.append(y)
        logging.debug(f"Found rows are: {found_rows}")

        for x in range(self.width):
            if all(
                self.grid[y][x].type_ == SpaceType.EMPTY for y in range(self.height)
            ):
                found_columns.append(x)
        logging.debug(f"Found columns are: {found_columns}")
        return found_rows, found_columns


def p1(input_: str):
    g = Grid(input_)
    g.display()
    g.expand_galaxy()
    g.display(big=True)
    return g.calculate_distances_between_galaxies()


def p2(input_: str, dist: int):
    g = Grid(input_)
    return g.calculate_greatly_expanded_galaxy(dist)


def main():
    # P1
    ## Tests
    dist = p1(EXAMPLE_COSMOS)
    assert dist == EXAMPLE_COSMOS_DISTANCE, f"The distance is equal: {dist}"

    ## Puzzle
    # dist = p1(PUZZLE_INPUT)
    # logging.info(f"The puzzle distance is {dist}")

    # P2
    ## Tests
    dist = p2(EXAMPLE_COSMOS, 1)
    assert dist == EXAMPLE_COSMOS_DISTANCE, f"The distance is equal: {dist}"
    dist = p2(EXAMPLE_COSMOS, 9)
    assert dist == EXAMPLE_COSMIC_X10_DISTANCE, f"The distance is equal: {dist}"
    dist = p2(EXAMPLE_COSMOS, 99)
    assert dist == EXAMPLE_COSMIC_X100_DISTANCE, f"The distance is equal: {dist}"

    ## Puzzle
    # dist = p2(PUZZLE_INPUT, 999_999)
    # logging.info(f"The puzzle distance is {dist}")


if __name__ == "__main__":
    main()
