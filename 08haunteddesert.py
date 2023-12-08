import logging
from math import lcm

from tqdm import tqdm

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)

START_NODE = "AAA"

END_NODE = "ZZZ"

FIRST_DESERT = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""
FIRST_DESERT_STEPS = 2

SECOND_DESERT = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
SECOND_DESERT_STEPS = 6


START_NODE_SUFFIX = "A"
END_NODE_SUFFIX = "Z"
GHOST_DESERT = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
GHOST_DESERT_STEPS = 6


class DesertNode:
    def __init__(self, data: str, left: str, right: str) -> None:
        self.data = data
        self.left = left
        self.right = right
        self.left_node, self.right_node = None, None


class DesertMap:
    def __init__(
        self,
        nodes: list[DesertNode],
        chosen_path: str,
        max_path: int = 100_000_000_000,
    ) -> None:
        self.nodes = nodes
        self.node_map = {n.data: n for n in nodes}
        self.chosen_path = chosen_path
        self.max_path = max_path

    def find_node(self, key: str) -> DesertNode:
        return self.node_map[key]

    def traverse_desert(self):
        current_node = self.node_map[START_NODE]
        step_count = 0
        for step in tqdm(self.path_generator(), total=self.max_path):
            if current_node.data == END_NODE:
                break
            current_node = self.traverse_step(current_node, step)
            step_count += 1
        return step_count

    def traverse_step(self, node: DesertNode, step: str):
        return self.find_node(node.left) if step == "L" else self.find_node(node.right)

    def path_generator(self):
        i = 0
        while i < self.max_path:
            for step in self.chosen_path:
                yield step
                i += 1
        raise ValueError(f"Finished {self.max_path}, but still haven't found solution!")


class GhostDesertMap(DesertMap):
    def __init__(self, nodes: list[DesertNode], chosen_path: str) -> None:
        super().__init__(nodes, chosen_path)

    def multidimensional_traverse_desert(self):
        current_nodes = [
            node for node in self.nodes if node.data.endswith(START_NODE_SUFFIX)
        ]
        starting_nodes_length = len(current_nodes)
        logging.info(f"Desert has {starting_nodes_length} ghosts!")

        finishing_nodes = len(
            [node for node in self.nodes if node.data.endswith(END_NODE_SUFFIX)],
        )
        logging.info(f"Desert has {finishing_nodes} spots to finish!")

        starting_node_cycles = {
            node_index: None for node_index in range(starting_nodes_length)
        }
        step_count = 0
        for step in tqdm(self.path_generator(), total=self.max_path):
            if all(n.data.endswith(END_NODE_SUFFIX) for n in current_nodes):
                break
            for i in range(starting_nodes_length):
                if (
                    current_nodes[i].data.endswith(END_NODE_SUFFIX)
                    and starting_node_cycles[i] is None
                ):
                    starting_node_cycles[i] = step_count
            if all(n is not None for n in starting_node_cycles.values()):
                logging.info("Found all cycles!")
                return self.find_pattern(starting_node_cycles)
            current_nodes = [self.traverse_step(cn, step) for cn in current_nodes]
            step_count += 1
        return step_count

    def find_pattern(self, starting_node_cycles: dict):
        return lcm(*starting_node_cycles.values())


def p1(input_: str):
    example_desert = input_.splitlines()
    moves = example_desert.pop(0)
    unlinked_nodes = []
    for desert_node in example_desert:
        if not desert_node:
            continue
        data, left_right = desert_node.split("=")
        left, right = left_right.replace("(", "").replace(")", "").split(",")
        unlinked_nodes.append(DesertNode(*map(str.strip, [data, left, right])))
    desert_map = DesertMap(unlinked_nodes, moves)
    return desert_map.traverse_desert()


def p2(input_: str):
    example_desert = input_.splitlines()
    moves = example_desert.pop(0)
    unlinked_nodes = []
    for desert_node in example_desert:
        if not desert_node:
            continue
        data, left_right = desert_node.split("=")
        left, right = left_right.replace("(", "").replace(")", "").split(",")
        unlinked_nodes.append(DesertNode(*map(str.strip, [data, left, right])))
    ghost_desert_map = GhostDesertMap(unlinked_nodes, moves)
    return ghost_desert_map.multidimensional_traverse_desert()


def main():
    # Test cases
    actual_steps = p1(FIRST_DESERT)
    assert actual_steps == FIRST_DESERT_STEPS
    actual_steps = p1(SECOND_DESERT)
    assert actual_steps == SECOND_DESERT_STEPS

    # Result
    # actual_steps = p1(PUZZLE_INPUT)
    # logging.info(actual_steps)

    # Test cases
    actual_steps = p2(GHOST_DESERT)
    assert actual_steps == GHOST_DESERT_STEPS

    # Result
    # actual_steps = p2(PUZZLE_INPUT)
    # logging.info(actual_steps)


if __name__ == "__main__":
    main()
