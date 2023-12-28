from enum import Enum, auto
import logging

EXAMPLE_INPUT = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""


class TileType(Enum):
    EMPTY = "."
    VERTICAL = "|"
    LEFT_LEAN = "\\"
    RIGHT_LEAN = "/"
    HORIZONTAL = "-"


class Direction(Enum):
    NORTH = auto()
    WEST = auto()
    EAST = auto()
    SOUTH = auto()

    @staticmethod
    def from_next_post(x, y):
        if x == 0 and y == -1:
            return Direction.NORTH
        elif x == 0 and y == 1:
            return Direction.SOUTH
        elif x == -1 and y == 0:
            return Direction.WEST
        elif x == 1 and y == 0:
            return Direction.EAST

class Tile:
    def __init__(self, character: str) -> None:
        self.type = TileType(character)
        self.powered = False

    def split(self, direction: Direction):
        self.powered = True
        if self.type == TileType.EMPTY:
            return []
        elif self.type == TileType.VERTICAL:
            return [(0,-1),(0, 1)] if direction in [Direction.WEST, Direction.EAST] else []
        elif self.type == TileType.LEFT_LEAN:
            if direction == Direction.NORTH:
                return [(-1,0)]
            elif direction == Direction.WEST:
                return [(0,-1)]
            elif direction == Direction.EAST:
                return [(1, 0)]
            elif direction == Direction.SOUTH:
                return [(0, 1)]
        elif self.type == TileType.RIGHT_LEAN:
            if direction == Direction.NORTH:
                return [(1, 0)]
            elif direction == Direction.WEST:
                return [(0, 1)]
            elif direction == Direction.EAST:
                return [(0,-1)]
            elif direction == Direction.SOUTH:
                return [(-1,0)]
        elif self.type == TileType.HORIZONTAL:
            return [(-1,0),(1, 0)] if direction in [Direction.NORTH, Direction.SOUTH] else []
        raise ValueError("Unsupported direction or type!")

class Grid:
    def __init__(self, input_: str):
        self.grid: list[list[Tile]] = []
        for line in input_.splitlines():
            self.grid.append(
                [Tile(s) for s in line if s],
            )
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def display(self):
        for line in self.grid:
            space_line = ""
            for space in line:
                space_line += str(space)
            logging.debug(space_line)

    def do_reflections(self):
        queue: list[tuple[int, int]] = []
        current_pos: tuple[int, int] = None
        for i in range(self.width):
            self.grid[0][i].powered = True
            if self.grid[0][i].type != TileType.EMPTY:
                queue.append(self.grid[0][i].split(Direction.EAST))
                current_pos = (0, i)
                break
        else:
            return self.width
        
        while len(queue) > 0:
            current_lead = queue.pop()

    def is_in_boundary(self, x: int, y: int):
        if x > self.width or x < 0:
            return False
        if y > self.height or y < 0:
            return False
        return True
    
    def get_iterator(self, direction: Direction):
        pass


def p1(input_: str):
    g = Grid(input_)

def main():
    p1(EXAMPLE_INPUT)

if __name__ == "__main__":
    main()