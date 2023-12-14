import logging
from enum import Enum

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)

EXAMPLE_INPUT = """.....
.S-7.
.|.|.
.L-J.
.....
"""

FUZZY_INPUT = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

BIGGER_EXAMPLE_INPUT = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

BIGGER_FUZZY_INPUT = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

SMALL_RESULT = 4
BIG_RESULT = 8

EXAMPLE_NESTS = 4

ENCLOSING_INPUT = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
"""

# find main loop
# find starting position symbol


# connections N W E S
class PipeType(Enum):
    VERTICAL = (True, False, False, True)
    HORIZONTAL = (False, True, True, False)
    NW = (True, True, False, False)
    NE = (True, False, True, False)
    SW = (False, True, False, True)
    SE = (False, False, True, True)
    GROUND = (False, False, False, False)
    START = (True, True, True, True)

    @staticmethod
    def from_symbol(s: str):
        if s == "|":
            return PipeType.VERTICAL
        if s == "-":
            return PipeType.HORIZONTAL
        if s == "J":
            return PipeType.NW
        if s == "L":
            return PipeType.NE
        if s == "7":
            return PipeType.SW
        if s == "F":
            return PipeType.SE
        if s == "S":
            return PipeType.START
        if s == ".":
            return PipeType.GROUND
        if s == "O":
            raise ValueError("floodfill should create pipes")
        raise ValueError(f"Uknown symbol {s}")

    @staticmethod
    def expand_symbol(pt: object) -> tuple[str, str, str]:
        if not isinstance(pt, PipeType):
            raise ValueError("Incorrect object type")
        if pt == PipeType.VERTICAL:
            return (".|.", ".|.", ".|.")
        if pt == PipeType.HORIZONTAL:
            return ("...", "---", "...")
        if pt == PipeType.NW:
            return (".|.", "-J.", "...")
        if pt == PipeType.NE:
            return (".|.", ".L-", "...")
        if pt == PipeType.SW:
            return ("...", "-7.", ".|.")
        if pt == PipeType.SE:
            return ("...", ".F-", ".|.")
        if pt == PipeType.GROUND:
            return ("...", "...", "...")
        if pt == PipeType.START:
            return (".|.", "-S-", ".|.")
        raise ValueError(f"Unsupported pipe type {pt}")


class Pipe:
    def __init__(
        self,
        s: str,
        x: int,
        y: int,
        is_original: bool = True,
        dist: int | None = None,
    ):
        self.symbol = s
        self.x, self.y = x, y
        self.pt = PipeType.from_symbol(s)
        if dist is None:
            self.dist = None if self.pt != PipeType.START else 0
        else:
            self.dist = dist
        self.is_original = is_original

    def possible_connections(self):
        ptv = self.pt.value
        connections = []
        if ptv[0]:
            connections.append((self.x, self.y - 1))
        if ptv[1]:
            connections.append((self.x - 1, self.y))
        if ptv[2]:
            connections.append((self.x + 1, self.y))
        if ptv[3]:
            connections.append((self.x, self.y + 1))
        return connections

    def is_connected(self, other):
        if not isinstance(other, Pipe):
            raise ValueError("bad object")
        return any(
            cx == other.x and cy == other.y for cx, cy in self.possible_connections()
        )

    def expand(self):
        expanded_pipes: list[list[Pipe]] = []
        expanded_symbols = PipeType.expand_symbol(self.pt)
        new_x, new_y, new_dist = self.x * 3, self.y * 3, self.dist
        expanded_pipes = []
        for dy, row in enumerate(expanded_symbols):
            expanded_row = []
            for dx, symbol in enumerate(row):
                if dy == 1 and dx == 1:
                    expanded_row.append(self)
                    continue
                # Calculate the new coordinates
                coord_x, coord_y = new_x + dx - 1, new_y + dy - 1

                # Determine if the new pipe should inherit the distance
                inherit_dist = new_dist if symbol != "." else None

                expanded_row.append(
                    Pipe(
                        symbol,
                        coord_x,
                        coord_y,
                        is_original=False,
                        dist=inherit_dist,
                    ),
                )
            expanded_pipes.append(expanded_row)

        return expanded_pipes

    def __str__(self):
        if self.dist is None:
            return self.symbol
        if self.dist == 0:
            return "\x1b[6;30;47m" + self.symbol + "\x1b[0m"

        if self.is_original:
            return "\x1b[6;30;42m" + self.symbol + "\x1b[0m"

        return "\x1b[6;30;45m" + self.symbol + "\x1b[0m"


class Grid:
    def __init__(self, input_: str):
        self.grid: list[list[Pipe]] = []
        for y, line in enumerate(input_.splitlines()):
            self.grid.append([Pipe(s, x, y) for x, s in enumerate(line) if s])
            self.height = len(self.grid)
            self.width = len(self.grid[0])
        self.big_grid = None

    def display(self):
        for line in self.grid:
            pipe_line = ""
            for pipe in line:
                pipe_line += str(pipe)
            print(pipe_line)

    def zoomed_in_display(self):
        if self.big_grid is None:
            self.expand_grid()
        for line in self.big_grid:
            pipe_line = ""
            for pipe in line:
                pipe_line += str(pipe)
            print(pipe_line)

    def expand_grid(self):
        self.big_grid = []
        for line in self.grid:
            pipe_upper_line, pipe_middle_line, pipe_lower_line = [], [], []
            for pipe in line:
                pul, pml, pll = pipe.expand()
                pipe_upper_line.extend(pul)
                pipe_middle_line.extend(pml)
                pipe_lower_line.extend(pll)
            self.big_grid.append(pipe_upper_line)
            self.big_grid.append(pipe_middle_line)
            self.big_grid.append(pipe_lower_line)

    def connected_pipes(self, pipe: Pipe):
        # possible connections
        pcs = pipe.possible_connections()
        connections = []
        for pcx, pcy in pcs:
            if self.is_in_boundary(pcx, pcy):
                other = self.grid[pcy][pcx]
                if other.is_connected(pipe):
                    connections.append(other)
        return connections

    def find_starting_pipe(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].symbol == "S":
                    return self.grid[y][x]
        raise ValueError("Starting pipe is missing")

    def find_furthest_pipe(self):
        sp = self.find_starting_pipe()
        step = 1
        next_pipes = self.connected_pipes(sp)
        current_pipes = next_pipes
        while len(current_pipes) != 0:
            logging.debug(f"current pipes {[str(cp) for cp in current_pipes]}")
            next_pipes = []
            for cp in current_pipes:
                if cp.dist is None:
                    cp.dist = step

                    cps = self.connected_pipes(cp)
                    cps = list(filter(lambda p: p.dist is None, cps))
                    next_pipes.extend(cps)
            logging.debug(f"next pipes {next_pipes}")
            current_pipes = next_pipes
            step += 1
        return step - 1

    def flood_fill(self):
        flood_fill_counts = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].symbol == "O":
                    continue
                if y in (0, self.height - 1) or x in (0, self.width - 1):
                    flood_fill_counts += 1
                    self._flood_fill(x, y)
        logging.debug(
            f"Needed {flood_fill_counts} floods to fill all the missing pieces",
        )

    def _old_flood_fill(self, x, y, new: str | None = None):
        new = "O"

        if not self.is_in_big_boundary(x, y):
            return
        if self.big_grid[y][x].symbol == new:
            return
        if self.big_grid[y][x].dist is not None:
            return

        self.big_grid[y][x].symbol = new
        self._flood_fill(x + 1, y)
        self._flood_fill(x - 1, y)
        self._flood_fill(x, y + 1)
        self._flood_fill(x, y - 1)

    def _flood_fill(self, x: int, y: int):
        new = "O"
        stack = [(x, y)]

        while stack:
            x, y = stack.pop()

            if not self.is_in_big_boundary(x, y):
                continue
            if self.big_grid[y][x].symbol == new:
                continue
            if self.big_grid[y][x].dist is not None:
                continue

            self.big_grid[y][x].symbol = new
            # Check and add adjacent positions to stack
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

    def count_nests(self):
        nests = 0
        for pipe_line in self.grid:
            for pipe in pipe_line:
                if pipe.dist is None and pipe.symbol != "O":
                    nests += 1
        return nests

    def is_in_boundary(self, x, y):
        if x > self.width or x < 0:
            return False
        if y > self.height or y < 0:
            return False
        return True

    def is_in_big_boundary(self, x, y):
        if x >= self.width * 3 or x < 0:
            return False
        if y >= self.height * 3 or y < 0:
            return False
        return True


def p1(input_: str):
    g = Grid(input_)
    logging.debug("current grid")
    g.display()
    furthest_pipe = g.find_furthest_pipe()
    logging.debug("$$$$$")
    g.display()
    logging.debug("#####")
    return furthest_pipe


def p2(input_: str):
    p1(input_)
    g = Grid(input_)
    _ = g.find_furthest_pipe()
    print("$$$$$")
    g.zoomed_in_display()
    print("$$$$$")
    g.flood_fill()
    g.zoomed_in_display()
    print("$$$$$")
    g.display()
    print("$$$$$")
    nests_count = g.count_nests()
    print(f"We have {nests_count} nests")
    return nests_count


def main():
    fp = p1(EXAMPLE_INPUT)
    assert fp == SMALL_RESULT, f"Got {fp}"
    fp = p1(FUZZY_INPUT)
    assert fp == SMALL_RESULT, f"Got {fp}"
    fp = p1(BIGGER_EXAMPLE_INPUT)
    assert fp == BIG_RESULT, f"Got {fp}"
    fp = p1(BIGGER_FUZZY_INPUT)
    assert fp == BIG_RESULT, f"Got {fp}"

    # fp = p1(PUZZLE_INPUT)
    # logging.info(f"The biggest step is {fp}")

    nests = p2(ENCLOSING_INPUT)
    assert nests == EXAMPLE_NESTS, f"Got {nests}"
    # nests = p2(PUZZLE_INPUT)
    # logging.info(f"Number of nests is {nests}")


if __name__ == "__main__":
    logging.debug("starting")
    main()
    logging.debug("finishing")
