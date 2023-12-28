import logging
from enum import Enum

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)


class GroundType(Enum):
    ASH = "."
    ROCKS = "#"

EXAMPLE_GROUND = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

PUZZLE_INPUT = """##..#.#..##
###...#....
##.##.##...
....###..##
####..###..
##.####....
...####.###
###...##...
##...#..###
##...#.....
.##..##.###

##.#...##...#
.#.#####.#.##
.#...........
####.#.###.#.
....###.#.#..
....###.#.#..
####.#.###.#.
.#...........
.#.#####.#.##
##.#...##...#
##.#.#.##...#
.#.#####.#.##
.#...........

##......##.
..##..#....
##....#####
##.#.#..##.
..#.###....
....#..#..#
####..#####
####..#....
#...###....

...#.####.#
####......#
#.###.##.##
#.##.#..#..
#.####..###
.....#..#..
###..####..
.....####..
..##..##..#
#..#......#
##..#....#.
##..#....#.
#..#......#

#.##.#..###.##.
##..###.####...
##..###.####...
#.##.#..###.##.
.#..#..##.#.#..
..##..##.####.#
##...##...#..#.
..##.......##.#
.#..#..#...##..
######........#
##..####.#..#..
#.##.#.#.#.###.
######.#.###.#.
#....#.###.####
##..##.####.#.#

###...###..
###...###..
#.#.#.#...#
...#..##.#.
...#..#....
.###.#.###.
#..##.###..
..#..#.#.##
..#..#.#.##
#..##.###..
.###.#.###.
...#..#....
...#..##.#.
#.#.#.#.#.#
###...###..

###........##..
...#..#.##.#...
...#..#..#.#...
###........##..
......#....#.##
...#.##.#..#.#.
#.###....#.#..#
.##.#..#..###..
.#.......###.#.
...###.#####...
..#..#####...#.
.#.#.#.#.#..###
.#.#.#.####..##
.#.#.#.####..##
.#.#.#.#.#..###

#.#..#..#
#....#..#
..##..#..
##...##..
.##..#..#
..#...##.
#..##.#..
#..##.#..
..#...##.

.#.##..#.#.#..#.#
.#.##..#.#.#..#.#
#..#.###.##....##
#.##.###.#......#
#.##...#.#.####.#
.#..#.##.###..###
#.....###...###..
..#.########..###
..#.###.#........
#..#####.########
.....##..########

...#....#....
#...####...##
#....##....##
.#..####..#..
#..#....#..##
..###..###...
#..##..##..##
..#.#..#.....
#.#.#..#.#.##
#####..######
##.##..##.###
#####..######
#.##.##.##.##

.#....##.#.#..##.
..#.##..###..#...
##...#...#..#....
##...#...#..#....
..#.##..###..#...
.#....##.#.#..##.
###...#..###..##.
##.#..##..##..#.#
.#.#..##..##..#.#

.#.####..##
..##.#.##.#
.#.##.#..#.
.....#....#
##....#..#.
....#......
...##......
##....#..#.
.....#....#

#.#..#.##.#
##....####.
###..######
.#....#..#.
.##..##..##
.##..##...#
.######..##
.#....#..#.
##.##.####.

....#.#
#....#.
#....#.
....#.#
..#.##.
.#.#...
####...
..#.##.
#......
#.#..#.
##.##..
##.##..
#.##.#.
#......
..#.##.

########.#..#.#
...##...#.##.#.
#.####.#......#
#.#..#.#.####.#
.#.##.#.######.
##.##.#########
.##..##..#..#..
#.####.#......#
.##..##.#....#.
..#..#...####..
##....##......#
..####...#..#..
.##..##.#.##.#.
.#..#.#.######.
..#..#..##..##.
.#....#........
..#..#..##..##.

..#.#.#..##..
.#.#...######
##.##....##..
...#####....#
###.####.##.#
.##..##.####.
..###.##....#
.##.#.#......
..#.##..#..#.
#...#.#......
.##.#.#######
.##.#.#######
#...#.#......
..#.##..#..#.
.####.#......

###.#...##.#.##
....#.###.##.##
.....####.#.###
##.###...#...#.
###.#..#####.#.
.....#.####....
..#.####..####.
###.####.###.#.
...####..###..#
###.#..#.#...#.
...#.##.#..####
..#..##.##....#
......#########
######...#..###
#######..#..###
......#########
..#..##.##....#

########...#.
.#...#.......
##.##.#...##.
####.#.##.##.
..#..##...#.#
##.##.#.#.#..
#.####....###
#.##.#..#####
#.##.#..#####
#.####....###
##.##.#.#.#.#
##.##.#.#.#.#
#.####....###
#.##.#..#####
#.##.#..#####
#.####....###
##.##.#.#.#..

..#.#...#####
##..##.#..#..
.##.....##.##
....######...
######.#..#.#
######.#..#.#
....######...
.##.....##.##
##..##.#..#..
..#.#....####
..#.#....####

####.#.#.#.####
.##.####.###.#.
.##...#..#..###
#..##..###.....
####..####.#.#.
.##..###......#
#####..###....#
.....#..#..#.#.
.....#..#..#.#.
#####..###....#
.##..###.....##
####..####.#.#.
#..##..###.....

#..##..#..#.###
.##..##..##.###
##########.....
..#..#...#.#.##
.........######
###..###.......
###..###.#.#...
...##......####
.##..##.##...##
..#..#.........
#......#..#.#..
#.####.####.###
#..##..###.#.##
##....###.#....
##.##.####.....
...##....###.##
##.##.#.####...

##..###...###
##..######.##
.###.....#.##
..#..#.#.#...
..#..#.#.##..
.###.....#.##
##..######.##
##..###...###
...........##
....##.#.#.##
#..####...###

####...#.###.....
.##.##.#.#..#....
.##.##.####.#.##.
#..##..##....####
.....###...#.#..#
#..#.##.#####.##.
#..#..#.#...#....
#######.#.....##.
.##...#####.#..#.
#####..##.#..#..#
#####...#.###....
####..#.#..#.####
####..#.##..#....
#..###.#..#.#.##.
####..#..##.#....

####.#..#
####.#..#
#.####.#.
.#..#.#..
.......##
##.#.##..
##.#.##..
.....#.##
.#..#.#..
#.####.#.
####.#..#

......#....
##..####...
.####...##.
#....#.####
.......#...
..##...#.#.
##..####..#
.#..#...###
.#..#.##.#.
.#.....#.#.
##..###..##
..##..#...#
......##.#.
#....##..##
#....##..##

#....####.#
##..##.#.##
##..##..#..
######...##
.#..#..##.#
#.##.#...##
######.####
######..###
#.##.#...##
.#..#..##.#
######...##

#.####.#.##
..####..###
...##......
.........##
...##...###
......#.###
..#..#..###
...##...#..
.######....
.#....#.#..
.#.##.#..##

..###....#.#..#
###.#..#.#..#.#
..###.##..#....
#...#..#..#....
#..##..#..#....
..###.##..#....
###.#..#.#..#.#
..###....#.#..#
.###....###.#.#
.##..#####..##.
.##..#####..##.
.###....###.#.#
..###....#.#..#
###.#..#.#..#.#
..###.##..#....

..##..#.#
######.#.
.####.##.
......#.#
##..##.##
..##...##
########.
..##.....
......##.

#.####..#.#
#..##...##.
.#.##.##...
.#.##.##...
#..##...##.
#.####..#.#
....#.#..#.
.#...#..#..
##.....##..
..#..##.###
..#..##.###
##.....#...
.#...#..#..
....#.#..#.
#.####..#.#
#..##...##.
.#.##.##...

..###.#..#.##
...#........#
..###......##
##....####...
....#......#.
##...######..
...##.####.##
###.#.####.#.
...##.####.##
..#.#.#..#.#.
##.###....###
......####...
...#.#....#.#
##.###.##.###
...#.#.##...#

#.###.#.###..
#..#.#.#####.
...#.##...#.#
.#####..##..#
##.#.....##.#
###..#...##.#
###..#...##.#
##.#.....##.#
.###.#..##..#
.###.#..##..#
##.#.....##.#
###..#...##.#
###..#...##.#
##.#.....##.#
.#####..##..#

..#####..#####.
..#.#.#..#.###.
###.#.#..#.#.##
..#.#......#.#.
...###.##.###..
..##..#..#..##.
##.###....###.#

.#..##....##..#
##.###.##.###.#
##.....##.....#
##.....##.....#
##.###.##.###.#
.#..##....##..#
.######..######
..#.#.#..#.#.#.
##.##.##.#.##.#
.....######....
###...####...##

#####..#######.
#..#.###....###
....#..######..
.##...#..##..#.
#..##..######..
.##.#.#..##..#.
.....##.####.##
....###.#..#.##
....#..##..##..

..........#......
###...#####......
..##..##...##..##
#.######.#.#.##..
...####....#...##
...#..#....##....
.###..###..######
.#..##..#..##....
#..####..#.#.#...
#.##..##.#.#.....
#........#.#.#...
...#..#...##.####
#.######.#####...
#.##..##.##..#.##
##.#..#.##.#...##

#....####..####..
#..##.#.#........
.##.###.#########
.##.##.#.#.####.#
.##.#...#...##..#
.##.#...#...##..#
.##.##.#.#.####.#
.##.###.#########
#..##.#.#........

..........#..
...##....####
..#..#...#.#.
.#....#..#..#
#......##.#.#
.#....#...#..
.#....#...#..
#......##.#.#
.#....#.....#

###..#....##.#..#
...##...###.###..
...##...###.###..
###..#....##.#..#
##...####.#.#..##
.#.##.####..#####
#.#.#.#..#.##..##
.#.#.####.#....##
#.#....##...#..#.
###.#..#.#.##.##.
.##....#.#.###..#
#...#.###....####
#.......#..#...#.
.######.##.#####.
..#####.##.#####.

##...#.##.#...#
#.###......###.
....#.####.#...
#.###..##...##.
...#..####..#..
##.####..####.#
#.#.########.#.
##.##.####.##.#
######....#####
#..##.####.##..
#..#...##...#..
#..#........#..
#..#........#..
#..#...##...#..
#..##.####.##..

....#.#..
.###...##
##.#..#..
..###.###
#..#.#...
.##.#.###
.##.#.###
#..#.#...
...##.###
##.#..#..
.###...##
....#.#..
####..#..

#...#.##.#.....
#..#..#.....#.#
.######.#..####
.######.#..####
#..#..#.....#.#
#...#.##.#.....
#.#.....##...#.
.#....##..##...
...####.#.#..##
.###..#.#..##..
.##..###.#.#..#
.##..###.#.#..#
.###....#..##..

######.#..#..##.#
..#.#..#.#.#.#..#
.##..##..###.####
.###..###........
...#.##.#.#...##.
.##.#..##..######
.##.#..##..######
...#.##.#.#...##.
.###..###........

##.#.###..##.
#.#.#.#.#..#.
..##.#.######
..##.#.######
#.#.#.#.#..#.
##.#.###..##.
.##...##.##.#
#.#.#.#.##.##
##.#.####..#.
##.#.####..#.
..#.#.#.##.##
.##...##.##.#
##.#.###..##.
#.#.#.#.#..#.
..##.#.######

.##.###.###..##
.##.#..#.#....#
.##..#.####..##
#..#..#..#.##.#
####.##..#....#
...##..#.......
#..#.###.#....#
#..#.#...#.##.#
......##..#..#.
.##....#.#....#
.##.##.#..####.
####..#.###..##
.##.#..##.#..#.
#..######.#..#.
.##.###.##....#

....####.###.#.##
##.#....##..###.#
##.#.#.#....####.
.....####..#..###
..#..#...#..#####
....##...####..#.
###..##.........#
############....#
##..#.#.#.######.
.##..##.#.##.#..#
...#..#####......
###...#.######...
###...#.######...

..#.##....#
..##.#.##.#
####.......
###........
.#..#######
..#.#.#..#.
..#...##.#.
..###......
#####......
.###.#.##.#
#..#..####.
.#..##.##.#
......#..#.
.##.#######
##..#......
##..#......
.##.#######

##.##.###
..####...
.#.####..
#..##..##
.##..##..
###..####
#..##..##
#......##
..#..#...
###..####
#.####.##
#.#..#.##
#......##
##....###
..####...

####.#...##..
.##.##.#####.
.##.#.#######
......######.
####.##...#..
#..##.#.##..#
#..##.#.###.#
####.##...#..
......######.

.#.##..##
#.#.#..#.
...#.##.#
....####.
....####.
...#.##.#
#.#.#..#.
.#.##..##
#.##....#
#####.###
#....##..
...##..##
#..######

.....####..#...##
#..#...#.#.#.##.#
####....#####.###
#..#.........#.#.
.......#..#.###..
#..#.###...#..#..
####...#....###.#
....#..#.########
....#..#.###.####

##.#...#...
##.#..####.
##.#..#####
##.#...#...
..##.#.###.
##.#.##....
####.#.###.
###..#.####
.....##.#.#
....#....#.
..##.#.###.

.#####...#.
##.#.#...#.
####.#...#.
##...#.###.
#.####.####
#....##.###
....#....##
...#..##..#
...#..##..#
....#....##
#....##.###
#.####.####
##...#.###.
####.#...#.
##.#.#...#.

.##.#.#.#
....#...#
##.#..###
....##.#.
.##.##.##
.##.#..#.
.##..#.##
.##..#.##
.##.#..#.
.##.##.##
....##.#.

..###..##..
#..##......
..#...####.
#......##..
#.##..#..#.
#.#.##.##.#
.#....#..#.
###..######
.##.#..##..
.#.#..####.
#..#..####.
#.#........
#.##.......
#..#..####.
.#.#..####.

#.##.#...
..##..###
......###
.####....
######...
.#..#.###
..##...##
##..#####
.##.#.###
#.##.####
.####....

...#...#....#...#
..##.#........#.#
..#..##.#..#.#...
##.####.#..#.####
...##..#....#..##
##.#.###....###.#
#####..#.##.#..##
####...#.##.#...#
###.####....####.
###....##..##....
..#.#...####...#.

.######.#..
..#..#..###
....#...#..
##....####.
########.##
#.#..#.#...
.#.##.#..##
.#....#.##.
#..##..#...
#..##..#...
.#....#.##.
.#.##.#..##
#.#..#.#...

######..#
..##...##
#.##.####
########.
#.##.#..#
.####.#..
######...
##..###.#
########.
#....#.##
#....#.##
########.
##..###.#
######...
.####.##.
#.##.#..#
########.

.##.#...#.###
#..#.#.##.#..
........###..
........###..
#..#.#.##.#..
.##.#...#.###
######.#.#.##
#..#..#..#...
.#....#....##
....#....#..#
#..#.####....
........###.#
#####.#.#...#
#..#..###..##
#..#.#.###...

.##.#..###..#..
.##.#..#..#....
.##...#.##.##..
.##...#.##.##..
.##.#..#..#....
.##.#..###..#..
#..#####.......
.....#####..##.
#####....#....#
..#......###..#
####...#......#
#..##.##.###.##
######.#...##.#

####.#.
#..##.#
#..##..
####.#.
####.#.
####...
.....#.
#####..
#####..
.##...#
.##.#.#
.##..##
.....##

......#.#..##.#
......#.#..##.#
#....###..##.#.
.####...#.#.###
.#..#...###.#..
######....#..##
.#..#.#.#.#.#..
......#....##.#
#.#..#####..#..
......##..####.
..##..##.###...
#.##.#..#....#.
.####.##.....#.

.##.##.##...#..#.
.##....##.##..###
..........#.##.#.
###########...#..
####..#######..##
#..#..#..##..##.#
#..####..#.#..#..
####..####..#####
##########..###..
.##.##.##.###.#..
#..#..#..#...#...
####..#####.#...#
###########.#.###
###.##.###.#..###
####..#####.#.#..
#..#..#..##...#.#
.##.##.##.#.#####

..##.#.
###.##.
###..#.
..##.#.
##..###
..###..
##.#..#

###..#.#..#.##.
#.#.#.#.#.#....
.#...#...##....
##...#...#..##.
..#####..##....
...#######.....
#...#.#..#.####
.##.###...#.##.
##.#.#.#.##.##.
.##.#..##.#....
..#.###........
#..#.#.#.#.#..#
#....#.#.#.#..#

..#.#.###..#.
..#.#.###..#.
.###....##..#
.##..#####.#.
##.#..###....
.#..##...##.#
#.#.##.###.##
#.#.######.##
.#..##...##.#
##.#..###....
.##..#####.#.

.##########..
.#.######.###
.#...##...#..
#..#....#..##
.##########..
#..######..##
##.#.##.#.###
..###..###...
.####..####..
.####..####..
..##....##...

##....##.....
##....##..#..
.#.#..#.#.###
####..##.#.##
#.###.##.#.##
....#....#...
..##.##.#.#..
...###.###...
..##.....####
.###.#.####..
.####.#......

.#.....##....
##.#..#..#..#
.#.#..#..#..#
.#..##.##.##.
.......##....
....##.##.##.
#............
.#.##########
##.....##....
..###########
#....#.##.#..

.##...##...
##.........
.#..#.##.#.
.##########
..##.#..#.#
#.###....##
..###....##
##.########
..##......#
####.####.#
..##.####.#
###.#.#..#.
....######.
....######.
......##...
......##...
....######.

###.#...#..###...
######.##.#..#...
###...###....###.
####..#..##....##
...###.#..##...##
.#...###.####...#
.#...###.####...#
...##..#..##...##
####..#..##....##
###...###....###.
######.##.#..#...
###.#...#..###...
###.#...#..###...

#.#.#.##.#..#.#
#...#.##.#..#.#
...###..#.##.#.
#.#.#.#.######.
##...#...####..
...####..#..#..
#.#.#.#########
.#...##..#..#..
##.#..###....##
###....#.#..#.#
##.##...#....#.
#.#...#.##..##.
.###.#.#.#..#.#
#..#.#..#.##.#.
..#.#.####..###

.#..#....#.
##..##..##.
...########
..#........
##.##.##.##
##.#..##..#
##.#......#
###.######.
.....#..#..
...##.##.##
####......#

..#..#..##...
..#..#..##...
#####...###.#
...###....#.#
#..##...#.#..
#...#..#...##
.#..##..#####
.##....##...#
#..##.#.#.#.#
###.....###.#
#...##.##.##.
#.#.###..##..
.#.#....#####
.#.#....#####
#.#.###..##..
#...#..##.##.
###.....###.#

#...###
.####.#
..##...
#......
#.#..#.
##.#.##
##.#.##
#.#..#.
#...#..
..##...
.####.#
#...###
#.##..#
.#.#...
.#.#...

..####.
##....#
...#...
##.##.#
##.##.#
##.##.#
##....#

###.##.#..#
#..###.#...
#####.#.###
.##.##.####
####..####.
.##..####..
#..#..#.##.
#..###.##.#
####.#.#...
#####.##.#.
.....#.####
.##.....#..
.....####..
.##..###..#
.##..###..#
.....####..
.##.....#..

#..###.#.#..#
.##.#.#..##..
####.#...##..
#..###.######
.##.#.###..##
####..##....#
....##.######
....##.......
.........##..
#..###.######
.....###.##.#
#..##.##.##.#
....###......
.##..#.######
####..##....#
.##.##..#..#.
#####.###..##

..##..#.###.#
..##..###.###
.####.....#.#
#....#.#.####
........#.#.#
......#....#.
#.##.##.##...
#....##..#..#
#....##..###.
#....#..###..
#..#.##.###..
#.##.#....###
.#..#..#....#
..##..##..###
.......#.....
#########...#
#########...#

....##..####.
#..#....#.###
#..#....#.###
....##..####.
##..##.##.#.#
#......##..##
.#######...##
#.#.....###.#
#.#.....###.#
.#######...##
#......##..##
##..##.##.#.#
..#.##..####.

#..##..#.......
#..#...#.##....
.##.#.##..#####
#..######.#####
.##.#..#..##..#
.##....##......
####.#....#.##.
.....#.#####..#
.##.....#......
.##.#..#.#.....
...##.###.#.##.

###.#...#....
....##.###...
....##.###...
#####...#....
##...#......#
...######....
...###..#.##.
##...#.#..#..
##.#.####.###

.#..###.#
#.#.#.###
#.#.#.###
.#..###.#
##.###..#
.#.#..#..
##..#.#.#
.##......
#..#...#.
##..#.##.
####.###.
.#..#.#..
###.#....
#.#....##
..#.#.#..
..#.#.#..
#.##...##

.######.#..##..
...#####.######
##..####..####.
###..#..#.#..#.
##.#.######..##
######..#..#...
##.#.####.####.
####..##.#.##.#
####..##.#.##.#
##.#.####.####.
######..#..#...

.#.#...####
....###.##.
###....#..#
.....#.#..#
######.....
.#.##.##..#
#.#.#..####
#.#.#..####
.#.##.##..#
#.####.....
.....#.#..#

.#.####.#...#.#
.#.####.#...###
###.##.###..#..
.########..##.#
...#..#....##.#
#........##..##
#.##..##.##.#..
..######....###
.###..###..##.#
.##....##.##.##
..##..##...#..#
#.##..##.###.##
#.#....#.#.##.#
#........###..#
...#..#...##.##

...##.###
##.#.....
##.##....
..#.###.#
.#....#..
####..###
##.#.##.#
##.#.##.#
####..###

.#.##.##.##
##.##.##.##
..###...###
#...#..###.
###.....##.
.###.#..#..
#.#....####
#.#....####
.###.#..#..
###.....##.
#...#..###.
..###...###
##.##.##.##
.#.##.##.##
###...#..#.

#.##.#.#.
#....#.##
#....#.##
#.##.#.#.
##..##...
######..#
#.##.##.#
######.#.
#.##.#..#
.####.#.#
.#..#.#.#
.#..#.#.#
..#...###
..##...##
#######..

#.##...####..##
##.#..##...#...
#....#.##.#.##.
####.#.#.###.#.
#######.##.##..
#######.##.##..
####.#.#.###.#.
#....#.##.#.##.
##.#..##...#...
#.##...####..##
.#...#..###.#.#
#.##..#.######.
..####.........
..####.........
#.##..#.######.
.#...#..###.#.#
#.##..#####..##

###.###.###
#..#.##..#.
#..###.#.#.
#######....
.##.#.#.##.
....##....#
####.#..###
.##..##.#..
.##..##.#..
####.#..###
....##....#
.##.#.#.##.
#######....

....#...##.
#..#.#...#.
.##..#.....
####.#..###
.##.#...##.
.##...##..#
....#..#...
.....#....#
####.#..##.
#..##.##..#
####.##.#.#
#..#.#.####
#..#.#.####
####.##.###
#..##.##..#
####.#..##.
.....#....#

..##..#..####
#.#..###.#..#
#.#.....#....
.#..####.####
..##.##.#.##.
...###..#.##.
##.######.##.
..####...#..#
.#..##.......
.#####..#####
.#####..#####
.#..#........
..####...#..#

....##..##...
...##.##.##..
#.#.##..##.#.
###..#..#..##
#.....##.....
...#.#..#.#..
.##.######.##
#.#...##...#.
#..#.#..#.#..
##.########.#
##.#.#..#.#.#
###.#.####.##
###..####..##
.#.#..##..#.#
.#.#..##..#.#

..#..#..###..
.###.#####...
.#..##..#.#..
##....#.##...
####..##..###
..##..#..##..
#.#.#...#####
..#.###.#####
###..####....
#.#..#.###...
####.########
......#..#...
#....#..#..##
.#..#....#.##
#####.#...#..
###.#.#...#..
.#..#....#.##

....#..##
.##.#.#.#
.##..##..
####..#.#
####..#.#
.##...#..
.##.#.#.#
....#..##
#..#....#

..#.##....##.#..#
....#.####.#....#
..#.###..###.#..#
.#.#...##...#.#.#
.###..#####.###..
####.#....#.####.
##..#.####.#..###
##..#.####.#..###
####.#....#.####.

###.##.###...####
.#.####.#..##..#.
##..##..########.
##......########.
.##.##.##..##..##
..##..##...##...#
##......###..###.

###......########
###...#..########
..#...###########
.##.#..#.#.#..#.#
###..##..#.####.#
#......#....##...
#.#.#...#........
##..#####...##...
#...#...#........
#.#.#..##.#....#.
#..###.##...##...
"""

class Grid:
    def __init__(self, input_: str):
        self.grid: list[list[GroundType]] = []
        for line in input_.splitlines():
            self.grid.append(
                [GroundType(s) for s in line if s],
            )
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def display(self):
        for line in self.grid:
            space_line = ""
            for space in line:
                space_line += str(space)
            logging.debug(space_line)

    def find_reflexion(self):
        found = False
        for row in range(1, self.height):
            found = self._find_row_reflexion(row)
            if found:
                return row * 100

        for column in range(1, self.width):
            found = self._find_column_reflexion(column)
            if found:
                return column
        raise ValueError("Not found any reflexion...")

    def _find_row_reflexion(self, row: int):
        comparison = 0
        for i in range(0, self.height):
            upper_row_idx = row - i - 1
            lower_row_idx = row + i
            if upper_row_idx >= 0 and lower_row_idx < self.height:
                comparison += 1
                logging.debug(f"Comparing row {self._row_display(upper_row_idx)} to {self._row_display(lower_row_idx)}, comparisons: {comparison}")
                if self.grid[upper_row_idx] != self.grid[lower_row_idx]:
                    return False
        logging.debug(f"Found row reflexion at row: {row}")
        return True
    
    def _find_column_reflexion(self, col: int):
        comparison = 0
        for i in range(0, self.width):
            left_col_idx = col - i - 1
            right_col_idx = col + i
            if left_col_idx >= 0 and right_col_idx < self.width:
                comparison += 1
                left_col = self._column_display(left_col_idx)
                right_col = self._column_display(right_col_idx)
                logging.debug(f"Comparing column {left_col} to {right_col}, comparisons: {comparison}")
                if left_col != right_col:
                    return False
        logging.debug(f"Found column reflexion at column: {col}")
        return True

    def _row_display(self, row: int) -> str:
        return "".join([g.value for g in self.grid[row]])
    
    def _column_display(self, col: int) -> str:
        return "".join([self.grid[i][col].value for i in range(self.height)])



def extract_grids(input_: str):
    current_grid = ""
    grids = []
    for line in input_.splitlines():
        if not line:
            grids.append(current_grid)
            current_grid = ""
            continue
        current_grid += line + "\n"
    grids.append(current_grid)
    return grids


def p1(input_: str):
    grids = extract_grids(input_)
    grid_reflexion_value = 0
    for grid_input in grids:
        g = Grid(grid_input)
        grid_reflexion_value += g.find_reflexion()
    logging.debug(f"Sum of the reflexions is: {grid_reflexion_value}")
    return grid_reflexion_value

def main():
    x = p1(EXAMPLE_GROUND)
    assert x == 405
    x = p1(PUZZLE_INPUT)
    logging.info(f"The puzzle output is {x}")

if __name__ == "__main__":
    main()