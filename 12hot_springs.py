import logging
from copy import deepcopy
from enum import Enum
from itertools import product
from tqdm import tqdm

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)


EXAMPLE_SPRING_HISTORY = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

EXAMPLE_RESULT = 21

PUZZLE_INPUT = """.##????.?.#.????? 4,1,1,3,1
???#??.?#??.? 2,2
???#??#?#?#???#???#? 8,9
???#?##??..?#??#? 9,2,2
???##????????#?? 7,4
..?????.???? 1,1,1,2
?#?.???????.#. 2,1,3,1
?????#.??#. 2,1,1
?##???.???#?...?? 4,3
#??????.#??? 4,1,1,1
??.??.??????#?? 1,3,4
.?.#?.????#.?#???# 1,1,1,1,6
.#?#?????.?..#??##? 5,2,2
??????????????## 3,4,3
?#???##?????? 3,2,1
..??.????#?.? 1,2
???????##? 1,5
??#???????#..??????. 11,4
????##????#??#?? 10,3
..???????. 3,1
?#??#?#???.#??#?#?? 9,1,5
?#?????#?#???#?# 1,3,1,1,3
??????#???? 1,1,6
??#?#??#??#?#?? 3,10
??#?#????#??# 2,1,3,1
?#???????? 1,3,1
.????.??#??? 3,3
????.?#??..#? 1,2,1,1
##?.????.?.?. 3,1,1,1
.?.??..#??? 1,1
#??????.??.#??.?? 1,4,2,3
?..??#.????? 1,3,1
???###.?#?? 3,3
?#????..??.???#?? 5,1,1,3
??????.???? 1,1
?#?#??#????.#?? 4,1,1,1
.?#??#????? 5,2,1
??#?#???#. 3,2
??.??????.? 1,1,1
.????#??#?????#??#?. 1,16
??##.??#??#?#?? 3,8
.??##?.????? 1,3,3
#????##?#?? 4,4
??????#?#???. 3,6,1
???.???##??#?? 2,1,3,1
.??##???..??##.? 4,4,1
.??#?#???.?#??#?? 7,1,1,1
?????#.?.??# 4,2
#??.?#????#?. 3,7
??????.?????#?##?#? 3,2,1,5
???????..??#??.???. 1,4,5,2
?.?#????????? 5,2,1
?????.#?????#?#? 1,2,1,1,3
.?.?.??###???????#?? 7,1
.??##.#??##??#?? 4,10
?..??#??#????#.??##? 11,2
.????#????##???#?? 2,12
??.???#?##? 1,1,5
.#??###????.???? 10,3
?##????.?.#??.#??? 5,1,3,1,1
??????????#???? 1,1,1,8
#??#???#?##?..#???#? 5,6,1,1,1
?????#??#? 1,3,1
???#????.???#?#?.##? 6,1,1,1,3
.#??.?????##?.# 3,3,3,1
??.?#?.?#?? 1,4
##?#..?????##? 4,1,2
?????#???? 2,1,1
???#...????# 1,1,1,1
??#?#??#?.##?? 8,2,1
#???..#.?.?#?..?..# 3,1,1,2,1,1
?????.???#???.? 1,1,2,3,1
??#?#?.?????????? 4,6
.?.#????????? 1,1
??????.#???#?? 4,1,2,3
????????#?#?? 6,3
##???###?#??.??# 2,8,1,1
??#??..????????? 1,2,4,1,1
#.##?#?#.?????. 1,6,4
??##??#???..?? 2,2,1,1
..??#...?#??#?##?? 2,7
??..?????#??.? 2,7
?.?##??.???#??? 1,3,3
?.?#?????##?#??. 1,6
#???##???. 1,3
??#??.?.????#?#?.?? 2,1,1,5,2
???##?????.?#?? 1,7,1
.#.?.???.??? 1,1,1,1
.????.##?? 1,2,2
??#?????.#??##?# 6,1,1,2,1
.???#?.#?...#?# 2,2,3
?#????#???## 3,2,1,2
?#??#.#.?.????? 2,1,1,1,4
.#?????????#? 2,2,2
.?#?#?????#??##??. 7,1,3
?.?#..??###? 2,4
?#??#???.??#?.#?##? 5,1,2,4
##.??.#?????##.???? 2,1,8,1
.?#?##?.???? 5,1,1
##??????.??? 4,1,2
.????.#?#???????? 2,3,2,3
?#?????#??.?????? 2,4,1,2,1
#???#??#???##?.? 1,11
.???????????? 1,1,1,2
#??##?.?#.???..?##. 6,2,2,2
??.??.?.#?##??.???? 1,1,1,6,1,1
#??.?#??????#?????.? 1,3,6,2
????????????##??. 5,7
##.????...??#?? 2,3,3
?.#.??.???# 1,1,2
?.??.##?.#??? 3,2
??#?##.?.??##. 4,4
?.??#.??#.?#??## 1,2,3,6
.?##??????????? 9,2
?????#????.?#??????? 2,1,2,3,1,1
?????.???##?? 5,4
?##???....?.? 4,1
?.?#?????#?.?.?.? 9,1
??#?.???????? 2,4,1,1
.??.??.??.??##. 1,1,1,1,2
.#???..????????. 1,1,1,3,1
.??.??###?##????#?? 1,11
???.##?##.?##?? 3,5,2,1
????.?.??.???.? 2,1,1,3
.?????##??##.?..??# 1,1,6,1,2
???.##???? 1,5
.???.??????. 1,3
#???????#.?? 5,1
?#?#????#? 4,4
?..#?#.?????#.?? 3,4
.?#?#?#?.???. 5,1,1
?.?#..?.???????.? 1,1,1,7,1
?.?????????#??????#? 1,1,9,1,1
???.???????.?. 1,5,1
?.?????#.??..?????. 6,2,3
?#????##??# 2,6
?.????????##??##?? 1,5,3,2,1
.?????????????. 1,1
..?#?.??????.? 2,4
?..##?.#???.???? 1,2,2,1,3
?#???#?????###????? 1,1,2,7
?#.#????#??#??# 1,1,1,1,5
??.?#??#????.. 1,1
???????##?.???##???? 7,6,2
????#..??.?????? 1,2,1,1,1
.????#?.???? 5,1
.?????.#?.... 2,2
??#??.?.?.???? 1,2,1,4
.????#?????????# 9,5
??????#??#.?? 1,6
??##?.???????.#?. 3,3,1
#?#??#???.???##?? 8,4
.??.??#???. 2,3
??#..????.??? 1,1,1,2
???????#??.?. 3,2,1
#?##??????##.??#??.? 12,3,1
#??#?##?.??###???? 1,5,8
#????.???#??. 1,2,3
?????#.??.??.?? 2,1,1,1,1
..#?????????...?#?#? 10,4
?#??????#?#?? 3,1,5
??????????.##????.? 5,1,1,6
???.????#????#????#? 3,4,5,1
????.?##?????? 2,2,1,1
.???.#?.?? 1,1,1
?????..?##??? 1,1,3
???.#??????? 3,1,1,1
???#??#??#?#???##? 4,11
??#???.#???.?#.?? 5,2,1,1
???.#?.?????. 2,2,2,1
?.#??#??#????#? 1,4,4,2
???.??#.?##????##??. 1,1,1,1,10
#?????##?#????#?? 1,1,8,1,1
#????#????.??##. 4,1,1,1,2
.???#.??????? 1,1,3,1
#??#???##????.?? 12,1
?.??###...?##???.??? 3,5
???.#?.???#???????#? 1,1,2,12
###??##?#??#????#? 3,13
??#.????#??#?????? 1,1,11,1
##?###?.??????? 7,1,3
???.????##?#?? 1,1,6
???.??#???#? 2,1,1,2
.#?#??#?##?#?.?#?.?? 11,2
.???.????#.????#?.?? 2,1,2,6,1
??..#??.#?????. 1,2,3,2
?????????#?#??? 1,1,5
?###?????#.##? 6,2,3
??#?.?#?.?.?#????#. 4,3,1,2,1,1
?????..???#?? 3,3
????.???##???? 1,7
?.????.????#??? 1,2,1,1,3
?????#?#??? 1,7
?????.??##?#??.? 2,8
??????###????# 3,7,1
#?#?#?..#??#?????##? 6,2,8
??#???????????#?? 3,3,4
#?.????#????#????? 1,12
???#?##?#.#??.?. 7,1,3
?#????????????? 1,3,1,1,3
????.????#???.##??. 1,1,1,4,4
...???##??.. 3,1
??????.?#? 4,1
?#???#?.?#????## 5,1,3
???.????#?.#.?.???.. 2,6,1,3
#.??.#??#??#???? 1,1,9,1
???.#?.?###?. 2,1,4
#.??#?????#????.#? 1,1,1,1,6,1
#???#???????#?? 2,7,1
???.????.?.??????.? 1,1
.????#??.?#?#?????? 6,5
.??#??..??. 4,1
.??#????##??#??.?? 4,3,2,1
??????.?#??? 3,2
??#??#????? 3,2,3
?#?#??.?.???.??### 2,2,1,1,4
??##???.??.. 1,2,1,1
#?#???#???#????#? 9,1,1,2
?.??##????#??#?##.. 3,10
.????????###??????? 1,1,1,10
?#..#?.??#? 1,1,2
?##.?.??##????#.# 3,1,2,1,1
?.?????#?#?.??? 1,6,1
?????#?.????#??#? 5,7
?#.#?#??.? 1,3,1
..???????.??? 5,2
???.?#????????? 1,1,2,1,3
??#?.??###??? 3,4
.#..??????#??##?##? 1,8,2,3
..?????#??.? 4,1
??..?.#.#?#???? 1,1,1,7
?.???????.?#?...??#. 1,4,3,3
#..?#??????.?# 1,4,1
?.?????????##?????.? 1,2,1,5,1,1
???##?#???#????.#?#? 4,7,1,4
???.??????? 1,1,1
????##.?#????????? 5,1,1,1,1,1
??#??#??????? 3,7
#?#???????..?.??.# 1,4,2,2,1
?#??#????? 6,1
?.?#????????#. 2,5
??#..#?.?#??#?? 2,1,1,1,1
???????.?. 5,1
.?#?#????. 1,4
?##?..??#? 2,1
.#???.??.? 2,1
.??#.??.??#?? 3,1,4
???????.???? 5,1,1,1
.?????.???#?.????? 5,1,1,1,1
???#?#?????#??????# 1,1,3,9
??????#.???..??? 4,1,1,1,1
#.?.#??#.?#?? 1,1,1,2
##?.??????# 3,1,4
?#?..?????##????#?? 2,14
?#?.?#???????????? 2,13
??#???????#? 3,1,1
.??????.?? 2,1
?????#????#???#??.# 7,1,1,2,1
?.??.#.?#??? 2,1,2
??..##????#???? 4,2
...???##?##???????? 12,1
????????.????#?#?. 1,5,1,4
?#??##??????#?? 9,2
???..???#???#?# 1,1,4,1,3
???###?#??# 1,6,1
?.??..?#?#? 2,4
?.???????#???###???? 1,15
.?..????#?#???? 1,8,1
?.?#?????.?????????. 7,5,3
??????#??.#?? 3,4,3
???.??#????##.? 1,1,4,2,1
?.??#??#.??# 1,2,2,1
??#??#??.?.?# 7,1,1
?#..???#??? 1,4
.#?#?#.#????.??#?? 3,1,1,1,2,1
??#?????#### 1,7
#..????#.?.???#??##? 1,1,1,1,8
#???#???.#??? 1,3,3
#?????.???#.??? 1,1,2,1,1
.??????..??#?? 1,4,4
.???????#??#? 2,3,2
?...???#?????????#? 1,9,1,1
??????#???. 6,1
.#??#?.??#?.?.?.#?. 5,2,1,2
??.????#.?.??#?### 2,4,1,1,3
?#???#???.?#???##??? 5,1,3,5
#??????#??? 1,1,3
??#?##????##??#.??? 12,1,1
.#????#???#?????.?? 1,6,3
.#??##?.?#? 1,2,1
??????#??????#????. 1,13
.??.?#.????. 2,2,3
?????.?.## 4,2
?.?#??#????#??#?? 4,5
??????#???????.??? 1,7,2,1,1
##?#????#?.#??? 5,1,1,1,2
??#?#?##.##??? 7,4
??#???.?#?? 3,2
???#??.?#??. 4,2
?#???????.#??????? 5,1,1,5,1
?..?#????#?? 1,2,1,4
?.??.##???##???#? 8,2
??.?#???#???? 2,1,7
?????#.??#??#? 3,5
.????#??.#??? 2,4
???####.????. 6,1,1
..?##?????.?? 4,1
?#.??#????? 1,3,1
...??..???##? 2,5
??..???#?#?????#?? 6,1
###????.?.#??#### 3,2,1,7
#??.??#???.?###?#? 2,1,1,1,7
??#??.#??#.# 3,2,1,1
??#?..?##?#. 3,4
??.???????#???#..? 4,6
??#???.?????.#? 6,1,1,2
#??#??##?##?.????? 12,2
#??????#?##???#??.. 2,1,8,1,1
???.??#??? 3,5
???.#????#?#??#?..#. 1,3,1,4,1
???.???#?#??#???.? 2,1,6,1
????????????#??.??? 1,3,1,3,2
.?..?#??#. 1,5
?#.##.??##??? 2,2,5
#.?????#???##?? 1,1,3,6
?????????? 2,3
##?#?????????? 6,6
#?????#??..##?#? 3,4,4
.??.?.?#?##?? 1,5,1
..??#?#??..##?# 1,5,4
?.????#??? 1,2,1
???#????#???# 4,2,1
???#..???#??.? 3,5
..??.??##??.??? 2,5
.????#??..#? 2,2,2
????????##??#?? 7,2,3
?????.???????.?##??? 2,1,1,1,1,6
.?#?????.???##??? 2,1,6
???#?#?????? 7,1
????.???#????????#. 1,1,1,4,2,1
??.?.??#??????????.# 1,1,8,1,1
????.??.??.?. 1,2
.#????#???? 1,2,1
#?#?#?#..?????.??. 7,3,1
???.#??????.#?#. 2,1,3
?????#???#??? 6,1,1
?.?????..#????? 5,3
.????.#?????.? 1,6
??.???##.??#???? 2,1,2,3,2
??#????????????#??# 15,2
##??????.????. 4,1,1,1
????#?#??..? 1,6
??#????????.? 3,4,1,1
?#..??#????????? 2,2,4,1,1
?????#?#???.????? 3,3,2,1
##?###?#??#???.? 11,1
?#????.???#????. 5,5
?.#??.?.???# 3,3
?#?????##??#.?? 4,3,2,1
.??.?..??#???#.?.#? 1,1,7,2
#??????.#? 1,4,1
????#???##??? 1,1,4
#.?#?#???#? 1,4,1
???.#??#?###?#?#??? 1,1,1,5,1,2
???#????????..#??.?# 7,1,1,2,2
#????????##??#? 1,1,3,6
?????##?#?..? 1,7
#?????##????#??## 8,3,2
.?#????.#??.??# 5,1,1,1
?#??.???####??..???? 3,6,4
?#???.??#???? 2,6
.?.??.##???##. 1,1,3,3
??#??????#?????#?#? 1,1,1,1,1,8
#?####????#??? 7,2,1
??.??????? 1,1
.?#??...?##????#??. 4,9
??????#?.???# 1,4,2,1
?????.?#??.?? 2,1,2,1
#?.?##?##?#?.??#?#?? 1,9,3,1
.#??##..???.#?? 5,1,1
??##?.##???. 3,2,2
#???????????.? 4,3
.?.?#?#??# 1,4,1
.##??#??###???.? 5,3,1
?.??##??#??#?#??.#. 1,2,1,2,2,1
?#???###.#?.### 2,4,2,3
???#???????.?#.##??? 8,1,2,2
.#?#??#.?.??? 1,4,1
???#???????#?????#? 1,1,2,5,5
?#?????????.??#?#??# 1,1,3,6,1
?#??#???.?.?. 4,1,1
#?#???????? 5,1,2
?#??#?.?????##??? 5,1,3
#.#?#?.?##??? 1,4,5
????##??????..#?## 7,4,1,2
??..????.#.?#????? 1,3,1,1,3
.?#?#?.#??#???????.? 3,4,1,2
?###.?#??????? 4,2,2,1
??##?????????##.# 9,2,1
?.???????#???#? 1,4,2
#?????????# 1,5,2
?????????#??.????# 1,2,5,5
???#??###.?.??? 1,2,3,1
?#??#???#????? 8,2
#??.##????.??.?.#?. 2,4,1,1,1,1
#?.#?#??##?..???#?? 1,8,4
????.??#..?# 2,3,1
.??.????.?? 2,3
??????#??????????#?? 1,5,1,1,1,3
??.???#??## 1,7
?...???#.?..???.?? 3,1
???#?#??#???.#.#. 11,1,1
?????????????.?.??? 9,1
?????????#????#.? 1,7,3,1
????#????.?.?#?? 4,1,1,3
.??##??????? 4,2
?##?#???#.?? 7,1,1
????#?????#?#??.???? 1,2,1,4,1,1
?????????#??? 1,2,3
?.###?.????.???#?? 1,4,2,4
???#???###?#?.#?.??. 2,8,1,1
.#?????????? 5,2
?#?.#???.#??#? 1,3,1,1
#?#????##? 3,1,2
.#.?...#??? 1,1,2
?????.?#??.#?? 1,1,4,2
?#?##..??????.??# 4,1,1,1,1
..???#??..# 2,2,1
.#????.???#? 1,2,1,1
#???.#..???#?????? 1,1,1,1,5,1
???.?..???#?? 2,1,1,3
?.?#.?#??#?...#? 1,2,5,1
????.???#?#?? 2,6
????#.#??#?? 1,1,2,1
.????##???.? 2,6
???..???#?#???## 1,1,4,3
..?.??#???##?. 1,1,1,5
..??????###? 2,5
..??#?##?#??????? 9,1
?##?#.???#????.??? 2,1,1,1,3,1
.#.#????#?##?#???? 1,2,10,1
#???##??#???? 2,3,1,1
??#???#?#????? 1,1,1,2
.??#?.??.??.? 2,1
?#????????#.?.# 2,1,4,1,1
???.??????????# 1,2,2,5
??????????????? 2,1,5,1
??????????#???#? 1,4,8
##?..???#?#?? 3,2,3,1
#????#??.? 1,5
??????#???#???#?. 10,3
.?#?.???.?? 1,2,1
????????????? 1,4,1
???????????? 4,1,2
??.#??????.?? 1,1,1
?#..??????? 2,1,4
?#??.??#??? 1,1,6
???#?#.?????????? 3,1,3,1,1
???#?#????#???##? 1,4,8
????#??.?##?.??? 1,2,3,1
???##?..???.. 5,2
.#???##??#??????. 1,9,1
???#????#???.?.??. 3,1,1,1,1,1
??..###???#..?#. 1,7,1
???.#?????.#????#?## 1,1,1,4,1,4
????.???#.#?? 3,3,3
???#???##.???? 4,2,1,1
?#?##.???? 4,2
????????#??.?????? 1,5,1,1,1,1
.##???#??? 2,3
#????.?#????.?. 1,1,6
?.??.??#?##?#.???..? 1,1,7,1,1
????#??#??##.#??. 1,2,1,3,2
??????#???.##?.??? 5,4,3,2
.?????#??#?????##. 1,4,4,3
????.??.#?.??#.###? 4,2,1,3,4
??.??#??????????.?? 1,3,1,2,1,2
????#???.???#. 6,1,1
#.?..#?.??????#????? 1,2,10
.??#?#?#??#.??#? 9,2
??????????. 2,1,1
.?.????#?????? 6,1
??#?..????? 4,1,2
?...???#?#? 1,4
???????#??#. 1,3,1,1
#?#???#??? 1,6
??????????.?##? 2,6,4
.???????.#?#.??.?# 1,2,1,3,1,2
?#.?..#????? 1,1,2,2
.?.??#????. 1,1,2
.??#?#????????????? 1,3,1,1,4,1
.#??#???#?? 4,1
???#..???#.?? 2,4
?.??.?.?#?? 1,1,3
.?.?.#???.??#.??.? 1,2,1,2,1,1
#??##?.?.????? 6,1,1
????#??#.????.#?# 1,4,3,3
??##?##?????#?#???# 14,2
?#?.?#.##?#?##??#?# 1,1,10,1
#?.?#????????.?# 1,5,1,2,1
??.??##???##?# 1,9
#?.??#?#??????.????. 1,7,1,1,1
??????#??.##?.? 1,1,1,2,1
????#????##?.? 8,1
????#?.?#?.? 2,1,1,1
.??#?.#????????.. 3,2,4
.??#??????. 2,4
????.#???? 2,1
??.#?.??##???#????#? 1,1,1,9,1
??.?#?????# 1,5,2
???????????# 1,1,4,1
??##.?????#???####? 1,2,13
#.???#??#????? 1,7,1
???????.#???#?? 1,1,2,1,4
??.?????#?.?#?#?? 1,1,1,2,4
#???#??.??. 7,1
??.?.??.???? 1,1,1,3
.?#????#??#??## 2,2,1,5
#??#??#??##??##???#. 1,13,2
?.??#????##???.?#?.? 12,2
..?#.???.? 2,1,1
?????????.?.. 6,1
???????.??? 7,2
.???#?##???#??.? 2,5,1,1
??#????#.?? 2,2,1
###????#??#?????#? 8,3,2
??.#??.??#?#?#. 2,1,1,3,3
.#.?#.?#?.?.??? 1,1,1,1,2
.#??#?##.?.. 2,4
????#????#????? 1,1,6
??#?#?.?#????? 3,2
?#..???.???#??#. 2,1,1,3,1
?????????.?## 2,3,1,2
?.?#??###???#???#?.? 1,11,3,1
.?#?.???.?????#?#? 2,2,8
?.?.#???????## 1,1,1,7
???????##???. 1,7,1
?????????#??#??# 2,1,3,2,1
.??.#?##???#???.#?? 1,11,1,1
?..?##??#?# 1,6,1
??.?.?.#??#?#. 1,6
?.#?#.???#?##? 3,6
??????????#?????#.? 2,4,1,5,1
?.?#???.?##?. 1,2,1,3
??#???.?#?? 1,3,1
?.???#???#????.? 1,9
.???????.#???. 6,3
??##?????#?#??#?.? 3,1,5,1
?#????.?????? 3,2,3,1
?.???#??#.????#?? 5,2
??#?#???.?.?#?? 5,1,1,1,1
????#?#?#???#.. 5,5,1
#????????. 1,4
?#.#?????#?? 1,2,1,3
?.??.???????#??..? 3,4
?.#???#???.#??? 6,1,1
.#?.#.??#????#???# 2,1,3,3,1,1
?????#??###???##?. 7,3
.???#????#????##???? 1,1,4,6
#.#?????.?????#?.# 1,2,1,4,1,1
?.?#?????? 1,3,3
?????.##?.?.?#.?#? 2,2,1,2,2
?.??#??..?#?##???. 5,5
??#.#.#.?####.###?? 1,1,1,1,4,5
.?????????#. 2,1,1,1
???????#.##???##.?? 1,1,1,7,1
??.????.?. 1,3
???##??.??????????? 4,1,3,1,1,1
??#??.?##??.??? 2,5,1
.?.###.?#????? 1,3,6
.?????..??.?? 4,1,1
#????.??#??????#???? 4,6,3,2
?..?#?.#????##???? 3,3,5
??#?#??##???#???#??. 1,14
???#???#.? 3,1
?.???#??#?????????? 1,11,2,1
??##????#?????.#?? 6,1,1,2,3
??##.??#??#?.?? 4,1,2,2
???##??#?#???##?. 9,3
?.??#???#????? 1,5,1
?.?.??.?#.? 1,1
?????##???. 1,6
.#??#??#???#???#??? 12,4
???.#???????? 2,1,6
??#???##???#?##??? 3,3,7
???.##???.??#?#. 2,3,1,2,1
.?.?#???????. 1,2,2,2
?#?#?#?.#.?????.# 6,1,1,2,1
#??#..???##????.?.?? 2,1,6,1,1,1
????#???????.? 1,1,1,3
?????#.#???##????.# 4,3,6,1
?#.??..??? 1,2,1
.???#.?.?? 1,1,1
.?????#??.??#???# 6,6
?.#????????#?.?? 2,5
??????#?.#?#?#????? 6,5,3
?#.???.??#?????#.?? 1,1,1,7,1,1
..?##?.?????. 2,4
????????.???#???#? 5,6
?.#?????#??#??????#? 1,8,6
???#???????##.??. 7,2,1
?..???#?#? 1,4,1
?##?#?###??????.? 11,1,1
#..???#?#?????????.? 1,13
??#???.??#? 1,2,2
#?#?#????????#?????# 1,1,1,1,2,7
?#.????#???#?#?.? 1,3,1,6,1
??..?.?#... 1,1,2
?.?.??.????.? 2,2
?.#????????? 2,3
????.???##?? 3,3
????.#????##??## 2,2,8
??.##??#?????#???? 5,5,1
.????????..?.?.???? 3,2,1,1,2
??#?#?????#?.##?. 1,5,4,3
??.?.?##??#???. 1,8
?#?????.## 6,2
.????#?#??#??# 1,8,1
?#??????#??#???????# 1,1,13
.??#.?#?...?????#?? 3,2,1,1,1,1
#.?.???#?####?#?? 1,1,12
??##?????##??... 3,6
#??#?#?..????#?##? 1,3,1,5
????.#???#? 1,1,2
??..??.????????? 1,1,2,2
????.??????? 2,1,1
??????.##.?? 2,2,1
?##??#????##? 6,2
.#???.?.#.???. 4,1,1
???.?????????? 1,2,4
????##.???? 2,2,1
???#...???##?. 1,1,6
..#???##?#????.?# 2,7,1
?.#??????????.#?.?? 1,2,5,1,1,2
###???#???#?????? 12,1,1
???.?#?#?.?.? 1,4
.????.##???#????? 2,1,10
.??????#?#? 1,4
???.???#??? 1,1,2
?#??.??????#?? 3,1,4
????.?????? 4,2
?.??#????#?????#? 1,3,1,2,2
?????#.????# 1,3,2,1
##?.??.#.?? 2,1,1
#??.?.???#???? 1,1,3
??#??.#?.? 1,2,1
?#?.?##??#?.?.#. 2,2,1,1,1
??#.?#.#?????.?.??? 1,1,1,6,2
?#?##???????#? 2,3,6
?????#?.?#?.? 1,1,2,1
?###??????????????. 3,5,4
...?????????. 3,2
.?.#?.#???????.? 1,3,1,1,1
??#.??????.??? 3,6,1
???????#?? 1,2,3
??????.??#?.??#..? 4,4,2,1
?.???#?##...?.?#??. 5,2
?????..##?? 2,4
?#????.?#????? 2,2,1,1
?#??##??##???.#?.# 1,7,2,2,1
#???#???????#?.? 2,6,2
???#??????##?#.#?# 3,1,2,4,1,1
?..#..????? 1,1,3
???????.?#???.?? 1,1,2,5
##?????###.?????#? 2,2,4,6
?###?#?????##? 4,1,6
?????..??????#?# 1,2,2,3
?#?#?.#???? 2,1,5
?.?#?#??#??.??#. 6,1
?##.?.?.????#.? 3,1,3,1,1
??????##?????#?? 1,6,2
???????.#.??# 4,1,1,1
.??????#..??#.? 6,3
?#?#?????.###????# 1,1,1,1,6,1
.?????###??.?#????#. 7,7
????##????#??. 6,1,3
??##????????????.?.? 5,4,3
##..###????.??? 2,3,2,2
??##.?.?.#???.?#??#? 4,1,4,6
???#???????#?? 1,2,6,1
???#??##?#.#?#? 8,1,1,1
.???##?#??#???#? 8,5
?.???????#.??#? 1,2,2,1,2
??#?????#. 2,4
????????????##?.?.?? 1,9,1,1
?##?.??.#.??#?#.? 4,1,1,4,1
?.????#.???#????? 1,1,1,6
?.???????. 2,2
.?#?###??##??????? 1,7,2,1
#?##??????????#???#? 1,2,1,4,1,1
.??.??.???.#?.?.? 1,2
???????.???#??#?.? 1,2,2,6
????.?????? 2,4
??#.#?#?????? 1,1,2,1
?????????#.?## 1,8,2
?.?????.???? 1,2
??????##??##?????? 1,11
.?#??#??.?.? 2,1,1,1
??????.??? 1,1,1
#?#??#??.??????? 6,5
??#?#???#.#??? 6,1,4
????.??###?? 1,5
?#????????? 1,1,2
???#????.??..?. 3,2,2,1
??#????????#??????# 5,1,3,1,1
???.#?#???????..?. 4,4
?????.???##?.? 3,5
???..???#?#???? 1,8
?##?.????.. 3,3
???#??..?#???### 3,2,4
??##???#???#?#??? 1,7,1,1,1
???.?????????#?.???? 1,1,8,2,1,1
?????????..?. 3,2,1
??.?.?????#??. 2,1,4
????#?#?.##?#???#?#? 6,11
?#????.??..??????? 1,1,1,1,2,2
??##?????#??#??.? 4,1,6
.???#????.# 7,1
?##.?.??#?? 3,3
??##?????##??.#?? 1,9,2
?#??.?????.?? 3,5
???.???#?## 2,7
?.#?.???##?.? 2,5
??#??#####??#??? 3,6,2,1
#??#?#.?#.??#?#??# 2,3,1,3,1
????????#?#? 1,9
?#.???#??? 1,1
??#???##??? 2,6
.?#?#?#??#???.? 3,2,1
?.???.???#? 1,1,4
???????????.# 1,3,1,1
?#??????#??#??.?#??. 5,6,3
?????.?#.. 2,1
???.???#???#??#???.? 1,1,3,8,1
?.???#??...?##???#. 5,7
?.???#?#??? 1,5
#??.??.#??##????? 1,1,1,5,2
???????#?.? 1,1
?.??#?#????????#?? 1,1,1,1,1,6
??????#?#?#??# 1,1,8
????.??#??#. 1,6
#?????#???#? 4,2,2
??#?????.#?????? 2,2,7
?#???##?#?##?#???? 14,1
##??????????#?#? 8,3,1
?#.#.??###??#???#??? 2,1,9,1,1
.????##???.????? 4,1
???##??#??#?#?. 6,4
?#?.???.?#???? 2,1,3,1
?.????.??##??? 1,3,3
????###?#??????#???? 12,1,1,1
.?#?.??????? 3,3
??#?#?#.?#.??#.???? 5,1,2,2,1,1
.#.?.?????#..??#?.?# 1,1,6,1,1,1
?#?###.#..? 5,1,1
#??#????..????#?##?? 6,1,1,8
??#?###?????#??? 13,1
##?.?.?#??? 3,5
??.?#?##???# 1,8
.??.??.#?#?#?# 2,1,7
???#???#?#????.??? 12,1,1
?.#.##??..???? 1,3,4
.??#???##??????# 7,5
?.?????#????? 1,10
#?.????#?#.?##?# 1,1,5,5
???????????.?##??. 10,2
.#?.#??#???.# 1,5,1,1
.?##??.??.?? 3,1
??.??????#? 1,5
??###????#?#???????? 6,1,3,1,1
???.?.#???#??????##? 1,7,5
?####?#?????.### 8,2,3
??#??#?#?..#???. 2,4,1,2
?..??.?##...?? 2,2
#.?.?#?#??????#???? 1,1,4,1,3,1
...?.???###??#??.. 1,6,4
?????..???????.??#?. 4,5,3
????????????#??? 1,7
.#??#????#??#?#? 1,11
??#.??##.?? 2,2
????.??#?? 2,2
?#??##?#?#.?#???? 9,1,2
.#?????.???.???.#?? 2,1,2,2,2
???#?.???????? 4,2,2
.?#?.?#.?? 2,2,1
.?###?????#???? 7,2,1
???##???????????#??? 1,2,9,1
##????????? 3,2,3
#.??.?##??#.??# 1,1,3,1,1
.#??????#??##?#????? 1,2,2,7,2
.????#??.???#?#?..?# 6,1,3,2
??#.?#?????#.??.?# 1,1,2,5,1,2
?.#.?##???#?.? 1,7
#???#??##??????.? 1,6,2,1
#???##?#?.?#?#??? 9,1,2
??????#?#???? 1,2,1,2
???#?.#?##.? 3,4,1
#???..???????####?? 3,3,6
#???#..##??.#. 2,1,3,1
#.#??.?????#??#?#??# 1,1,1,9,1,1
.??.???#????? 1,4,2
.?##????.??? 7,1
.??#??.?####???#? 3,9
#?????#??? 2,6
?????.??#??#?? 1,1,3,2
????#??#????##?. 4,3,3
.#????.?#?. 1,2,2
??#??#?#?#???#??? 12,1
???#.#?.??????###?.? 1,2,2,9,1
?##???#???##?.?? 3,1,1,2,1
??.????.??#?????# 2,1,1,1,7
#.?#?#?...?? 1,5,2
?????##??##? 1,1,7
?#?.?.??.?#? 2,1,2,3
???#?..???.? 1,2,3,1
??##????.?#..#????? 1,5,2,1,1
#????????.?#?? 9,1
#????#??#..#?#???? 1,5,1,1,3,1
?#???#??#?.??#? 3,5,3
.??.?????? 1,1
#??????#??.??#?#? 8,1,5
??#..?????###?? 1,1,1,1,3
#.???.??.??? 1,2,1,3
?.???.??.???# 1,2,3
??.???.??.?#?.?.??? 2,2
?????.?#?.??#??#? 4,1,3,2
?##???????##?#?## 2,2,8
?#??????#?? 1,3,2
?????.???#?#?## 1,1,1,1,4
#?#??.?????.#.?? 5,1,1,1,2
????#?.?.? 1,2,1
.??.???.?? 1,1,1
.???###.????#.????? 1,3,1,1,4
??#????###.? 1,1,4
.?..?##????? 1,6
.#??#?.???? 4,1
#.#??#????????. 1,5,1,1,1
.#.??#??##?.??#???? 1,8,3,1
#???#????.??? 2,5,1
.?.???.??..# 1,2,1,1
????.?##??#?#????..? 3,11,1
.????#.#??. 1,1,2
?????#????.?????#?? 9,4
?#??????.??????#??# 1,4,1,2,1,1
??#.##.???? 1,2,1
????.????##??.???? 2,2,2,4
???#??#??????#. 6,1,2
??#??????.###?? 1,2,1,2,4
?#?#?#.?#.??. 5,1,1
#?##.?????.??#? 1,2,2,1,3
?#?#.?????##. 3,2,3
#????##??.#. 3,3,1
#??????.?#??##????? 1,1,1,6,4
?.?..?#??##???????# 1,1,7,1,1,1
???#???##??? 6,1
.??#??????? 4,1,2
?.???#???.#??. 7,1,1
????#????.???????. 7,3
???#.????#???? 1,2,6
??##????#.#???.?? 1,2,1,3,1
?###?.#?????#. 4,3,1,1
???..??.#? 2,1,1
??.?????????. 1,7
##?.?#?#?#?#???????# 2,11,1,1
?????#??.????#? 6,1,1
??.??????##?? 1,1,4
.?##?.?.??????#? 3,1,1,1,3
??.##?????? 1,3,2
??????#?#?##??????#. 2,1,4,6,2
??.????????#?#.? 2,10
?#????#?.?????##? 6,4,2
??##??#???????.#? 4,2,1,2,1
.#?.???#??#??..?##? 1,5,1,3
#??#??????? 4,2,1
.?????????#????? 1,11
#???#??##???????? 1,2,7
..?.????#?.?.?##?#?? 1,2,1,1,7
..#?.?..#. 1,1,1
.#????#???#??.????. 11,2
?????.????#????.?? 5,2,1,3,2
??#????#?#??? 2,1,2,3
???.???#.?? 1,2
#???#??##???#??# 3,1,2,5
????????#??????? 2,1,1,2,5
?.?#???.#? 1,3,1
..?.#??.#??#?????? 1,1,1,1,3,2
???#???.??.?? 6,1,1
?#?#.#????? 4,3
???#?.???.???..?..?. 4,3,1,1,1,1
???#?#?.???#?? 1,4,3
?#?????.????#???? 2,2,6
.??#????....???#?.? 6,4
???.?##??????#? 4,5
??.??.#???# 2,1,5
.??#??#?#???????##? 8,8
???.????.???.###??? 1,3,3,3,1
????#.?#?? 1,1,2
?????????#.? 1,1,1,1
???.?.???.? 2,3
..?.??.?#???.??.?? 5,2
???#??????????#? 3,7
?????.???.#??. 2,1,1,2
?##??????? 3,1
?##?#..???#?##.? 4,1,5
?#?#????##??? 4,6
?.????...?.. 1,1
??#?????.?? 4,2
?#????.????? 6,1,1
??##??????????# 4,1,1,1,2
##..?#????.??#?#..? 2,2,1,4,1
##??#????#?.???.??? 2,7,2,1
???.???##?? 2,1,4
.?#.#????#?#??.?#??? 2,9,1,1
?#????##?? 4,3
.#?.?##?.????# 2,4,1,1
.???#??????.????#? 6,1,4
?????#???.. 1,6
?.?#?????? 2,3
??.???.??#.?# 1,3,1,1
?.?..??#??.?? 1,4
???#??????##?.???.? 6,4,3
?????##.???..#? 3,2,1,1
????.??.???. 3,1,2
.??.?##?.? 2,2
#?????#???#??#?.?#? 1,1,11,2
????##??#.#?? 1,2,1,1
?###?.#???.#???#? 3,4,2,2
?????.#?..#????.#?.? 2,1,1,4,1,1
??.?????.#? 1,1,1
..??.??.?????.?? 1,4
#???###.???.?. 7,1
?#?.???###. 2,5
??#?????.???? 6,2
.????#?.#? 1,1,2
.#?##????#.???????. 5,2,3,2
#?#????#??? 5,1,2
?#..???##?.???#???? 1,1,3,1,2,1
.?.???.???????# 1,1,2,1,3
#?.????#???#.??#??#? 2,1,4,1,6
?#????.?#.????? 2,1,2,1,2
??.?#??#####???# 1,2,8,1
?????????.??##?#. 1,1,2,5
????..???.?##?.. 1,3
??#???????????????? 4,1,4,1,2,1
?#.??#.?#?.??.?????# 1,1,2,1,1,4
?#????#????#??#????. 1,6,5,2
?#.?.???????? 1,1,1,4
?????#??#.??..? 1,1,4,1
.???????##?#? 2,1,6
.??????#??????#?? 6,7
????.#???? 1,3
???#..?#?. 4,3
???.?#???????#. 1,6,3
.???#?#???#?#?#.??.. 12,1,1
.??.????##?????.???? 1,7,1,1,2
?..#?.???? 1,1
#???????#?. 1,1,5
?????.?..????..??.? 1,3
?.#?#?#??????? 10,1
???#????..?#???? 5,5
?.?.?????..??.#??#?? 1,1,1,1,1,5
??..#?..#???.?? 1,1,1,1,1
#??.????#???##??#.?? 1,1,1,7,1,1
#?.??#???#??? 1,2,3,1
##?###?.??? 2,3,1
?.???#??.????.?. 2,3,1
???????#?.???.? 7,3
????.#?????. 4,1,3
#????.?#??????#? 5,3,1,2
?????##?.??????????? 8,1,1,3,1
?##?.#??????? 3,4,1
????.?.?????#?#????? 1,8
.???#.??#.??? 4,1,1,1
?#????????#???.???? 2,1,2,2,1,2
.???.???.#? 3,2
????#?..????. 3,2
.???.?.???##? 1,3
???.????????.?????? 1,7,1,1,1
.???.?#??#? 2,5
##?..#???#? 3,2,2
???.??????##??##?# 1,12,1
???????.###?? 1,1,1,3
.???????????#.???? 1,1,2,4,1
..?????????.?.?.???? 1,1,1
??#???#???#.# 3,4,1,1
?#??##?###????#??.#? 10,5,2
?#?.#??????##?????#? 2,1,1,2,2,5
??????.?#?.??.?#?#?? 1,2,3,1,5
??.#??.???????????# 1,3,2,2,1,2
??#??..#?#?? 4,1,1,1
.??##????.???? 6,1,1
???###??#??#??#?#? 1,6,1,3
??##?????#? 6,1
?.???...?? 1,1,1
???#???#..#????. 1,1,3,3
??#?????.???#?#???? 4,2,1,4,3
.??#####?#?..??? 7,1,1
.#.?.?.?##??#??#??#? 1,1,1,7,5
.???#???..???. 2,3,3
..??#?.???????#.#??? 4,1,1,1,1,3
"""

EXAMPLE_EXPANDED_RESULT = 525152


class SpringHistoryRecord(Enum):
    OPERATIONAL = "."
    DAMAGED = "#"
    UKNOWN = "?"

    @staticmethod
    def known():
        return [SpringHistoryRecord.OPERATIONAL, SpringHistoryRecord.DAMAGED]

    @staticmethod
    def display(records: list[object]) -> str:
        if not all(isinstance(r, SpringHistoryRecord) for r in records):
            raise ValueError("Incorrect record type!")
        return "records - " + "".join(r.value for r in records)


def history_meets_conditions(
    test_history: list[SpringHistoryRecord],
    contiguous_failure_groups: list[int],
) -> bool:
    current_damaged_count = 0
    damaged_counts = []

    logging.debug(f"Checking {SpringHistoryRecord.display(test_history)}")
    for r in test_history:
        if r == SpringHistoryRecord.DAMAGED:
            current_damaged_count += 1
        elif current_damaged_count > 0:
            damaged_counts.append(current_damaged_count)
            current_damaged_count = 0

    if current_damaged_count > 0:
        damaged_counts.append(current_damaged_count)

    logging.debug(f"Got {damaged_counts}, expected {contiguous_failure_groups}")
    return damaged_counts == contiguous_failure_groups


def bruteforce_fix_history(
    damaged_spring_history: list[SpringHistoryRecord],
    contiguous_failure_groups: list[int],
) -> tuple[int, list[tuple[SpringHistoryRecord]]]:
    count_unknown = damaged_spring_history.count(SpringHistoryRecord.UKNOWN)
    possible_fix_combinations = list(
        product(SpringHistoryRecord.known(), repeat=count_unknown),
    )
    true_combinations = 0
    logging.info(
        f"Trying to fix {SpringHistoryRecord.display(damaged_spring_history)} with {len(possible_fix_combinations)} possibilities"
    )
    good_fixes = []
    for possible_fix in possible_fix_combinations:
        fixed_spring_history = deepcopy(damaged_spring_history)
        i = 0
        for j, r in enumerate(fixed_spring_history):
            if r == SpringHistoryRecord.UKNOWN:
                fixed_spring_history[j] = possible_fix[i]
                i += 1
        if history_meets_conditions(fixed_spring_history, contiguous_failure_groups):
            good_fixes.append(possible_fix)
            true_combinations += 1
    return true_combinations, good_fixes


def pruned_bruteforce_fix_history(
    damaged_spring_history: list[SpringHistoryRecord],
    contiguous_failure_groups: list[int],
) -> int:
    possible_fix_combinations = get_pruned_possibilities(
        damaged_spring_history, contiguous_failure_groups
    )
    true_combinations = 0
    logging.info(
        f"Trying to fix {SpringHistoryRecord.display(damaged_spring_history)} with {len(possible_fix_combinations)} possibilities"
    )
    for possible_fix in possible_fix_combinations:
        fixed_spring_history = deepcopy(damaged_spring_history)
        i = 0
        for j, r in enumerate(fixed_spring_history):
            if r == SpringHistoryRecord.UKNOWN:
                fixed_spring_history[j] = possible_fix[i]
                i += 1
        if history_meets_conditions(fixed_spring_history, contiguous_failure_groups):
            true_combinations += 1
    return true_combinations


def get_pruned_possibilities(
    expanded_damaged_spring_history: list[SpringHistoryRecord],
    good_combinations: list[tuple[SpringHistoryRecord]],
    contiguous_failure_groups: list[int],
):
    count_unknown = expanded_damaged_spring_history.count(SpringHistoryRecord.UKNOWN)
    count_known = expanded_damaged_spring_history.count(SpringHistoryRecord.DAMAGED)
    count_needed = sum(contiguous_failure_groups)
    missing = count_needed - count_known
    possible_fix_combinations = [
        p
        for p in product(SpringHistoryRecord.known(), repeat=count_unknown)
        if p.count(SpringHistoryRecord.DAMAGED) == missing
    ]
    return possible_fix_combinations

def get_lower_subset_of_good_possibilities(good_combinations: list[tuple[SpringHistoryRecord]]):
    pass

def extract_input(line: str) -> tuple[list[SpringHistoryRecord], list[int]]:
    damaged_spring_history, contiguous_failure_groups = line.split()
    damaged_spring_history = [SpringHistoryRecord(r) for r in damaged_spring_history]
    contiguous_failure_groups = [int(g) for g in contiguous_failure_groups.split(",")]
    return damaged_spring_history, contiguous_failure_groups


def bruteforce_solve(line: str) -> int:
    damaged_spring_history, contiguous_failure_groups = extract_input(line)
    true_combinations, _ = bruteforce_fix_history(
        damaged_spring_history, contiguous_failure_groups
    )
    if true_combinations == 0:
        logging.error(f"For line {line} there was no possible fixes!")
        raise ValueError("There needs to be at least one possible fix combination!")
    logging.debug(
        f"On the line {line} there are {true_combinations} possible solutions",
    )
    return true_combinations


def extract_and_expand_input(
    line: str, folds: int | None = None
) -> tuple[list[SpringHistoryRecord], list[int]]:
    if folds is None:
        folds = 5
    damaged_spring_history, contiguous_failure_groups = extract_input(line)
    expanded_spring_history = []
    for _ in range(folds):
        expanded_spring_history.extend(
            damaged_spring_history + [SpringHistoryRecord.UKNOWN]
        )
    expanded_failure_groups = contiguous_failure_groups * 5
    return expanded_spring_history, expanded_failure_groups


def pruned_fix_history(
    expanded_damaged_spring_history: list[SpringHistoryRecord],
    expanded_contiguous_failure_groups: list[int],
    good_combinations: list[tuple[SpringHistoryRecord]],
):
    possible_fix_combinations = get_pruned_possibilities(
        expanded_damaged_spring_history, good_combinations, expanded_contiguous_failure_groups
    )
    true_combinations = 0
    logging.info(
        f"Trying to fix {SpringHistoryRecord.display(expanded_damaged_spring_history)} with {len(possible_fix_combinations)} possibilities"
    )


def pruned_solve(line: str):
    damaged_spring_history, contiguous_failure_groups = extract_input(line)
    (
        expanded_damaged_spring_history,
        expanded_contiguous_failure_groups,
    ) = extract_and_expand_input(line)
    _, good_combinations = bruteforce_fix_history(
        damaged_spring_history, contiguous_failure_groups
    )
    pruned_fix_history(
        expanded_damaged_spring_history,
        expanded_contiguous_failure_groups,
        good_combinations,
    )


def p1(input_: str):
    all_possible_fixes = 0
    for line in tqdm(input_.splitlines()):
        all_possible_fixes += bruteforce_solve(line)
    return all_possible_fixes


def p2(input_: str):
    all_possible_fixes = 0
    for line in tqdm(input_.splitlines()):
        all_possible_fixes += pruned_solve(line)
    return all_possible_fixes


def main():
    # P1
    ## Example
    # result = p1(EXAMPLE_SPRING_HISTORY)
    # assert result == EXAMPLE_RESULT

    ## Puzzle
    # result = p1(PUZZLE_INPUT)
    # logging.info(f"Got possible fixes: {result}")

    # P2
    ## Example
    result = p2(EXAMPLE_SPRING_HISTORY)
    assert result == EXAMPLE_EXPANDED_RESULT


if __name__ == "__main__":
    main()
