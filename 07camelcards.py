import logging
from enum import IntEnum

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)

EXAMPLE_GAME = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

EXAMPLE_RESULT_P1 = 6440

EXAMPLE_RESULT_P2 = 5905

SYMBOL_STRENGTH_P1 = {
    symbol: strength for strength, symbol in enumerate("23456789TJQKA")
}
SYMBOL_STRENGTH_P2 = {
    symbol: strength for strength, symbol in enumerate("J23456789TQKA")
}


TWO_REPEATS = 2
THREE_REPEATS = 3
FOUR_REPEATS = 4
FIVE_REPEATS = 5


class HandType(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE = 3
    FULL_HOUSE = 4
    FOUR = 5
    FIVE = 6


class Hand:
    def __init__(self, value: str, bid: str, p2: bool = False):
        self.value = value
        self.bid = int(bid)
        self.p2 = p2
        self.strengths = SYMBOL_STRENGTH_P2 if p2 else SYMBOL_STRENGTH_P1

        hand_type, symbol_frequency = self.calculate_hand()
        self.type_ = hand_type
        self.symbol_frequency = symbol_frequency

    def calculate_hand(self) -> HandType:
        symbol_frequency = self._count_frequencies()

        hand_type = self._get_hand_type(symbol_frequency)

        return hand_type, symbol_frequency

    def _get_hand_type(self, symbol_frequency: dict):
        hand_type = HandType.HIGH_CARD  # Default hand type

        if any(sf == FIVE_REPEATS for sf in symbol_frequency.values()):
            hand_type = HandType.FIVE
        elif any(sf == FOUR_REPEATS for sf in symbol_frequency.values()):
            hand_type = HandType.FOUR
        elif any(sf == THREE_REPEATS for sf in symbol_frequency.values()) and any(
            sf == TWO_REPEATS for sf in symbol_frequency.values()
        ):
            hand_type = HandType.FULL_HOUSE
        elif any(sf == THREE_REPEATS for sf in symbol_frequency.values()):
            hand_type = HandType.THREE
        elif sum(sf == TWO_REPEATS for sf in symbol_frequency.values()) == TWO_REPEATS:
            hand_type = HandType.TWO_PAIRS
        elif any(sf == TWO_REPEATS for sf in symbol_frequency.values()):
            hand_type = HandType.ONE_PAIR

        return hand_type

    def _find_best_hand_solution(self, frequencies: dict):
        if frequencies.get("J", 0) == 0:
            return frequencies

        freq_copy = {key: val for key, val in frequencies.items()}
        logging.debug(f"Got solution frequencies {frequencies}")
        jokers = freq_copy.pop("J")

        for _ in range(jokers):
            highest_freq = max(freq_copy, key=freq_copy.get)
            freq_copy[highest_freq] += 1
        logging.debug(f"Best hand solution is {freq_copy}")

        return freq_copy

    def _count_frequencies(self):
        strength_frequencies = {s: 0 for s in self.strengths}
        for s in self.value:
            strength_frequencies[s] += 1

        if self.p2:
            strength_frequencies = self._find_best_hand_solution(strength_frequencies)

        return strength_frequencies

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        if self.type_ > other.type_:
            return True
        if self.type_ < other.type_:
            return False

        for vs, vo in zip(self.value, other.value, strict=True):
            if self.strengths[vs] > self.strengths[vo]:
                return True
            if self.strengths[vs] < self.strengths[vo]:
                return False

        return False

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        if self.type_ < other.type_:
            return True
        if self.type_ > other.type_:
            return False

        for vs, vo in zip(self.value, other.value, strict=True):
            if self.strengths[vs] < self.strengths[vo]:
                return True
            if self.strengths[vs] > self.strengths[vo]:
                return False

        return False

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__lt__(other)

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__gt__(other)

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__eq__(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return self.value == other.value

    def __str__(self) -> str:
        return f"Hand({self.value}, {self.bid}, {self.type_.name}) {self.p2}"


def calculate_total_winnings(hands: list[Hand]):
    winnings = 0
    for i, hand in enumerate(sorted(hands), 1):
        current_winnings = hand.bid * i
        logging.debug(
            f"The current winning for {hand.value} with bid {hand.bid} rank {i} is {current_winnings}",
        )
        winnings += current_winnings
    return winnings


def p1():
    hands = [Hand(*hand.split()) for hand in EXAMPLE_GAME.splitlines()]

    logging.debug("Unordered hands:")
    for hand in hands:
        logging.debug(hand)

    logging.debug("Ordered hands:")
    sorted_hands = sorted(hands)
    for hand in sorted_hands:
        logging.debug(hand)

    winnings = calculate_total_winnings(hands)
    logging.debug(f"The winnings are: {winnings}")
    assert (
        winnings == EXAMPLE_RESULT_P1
    ), f"Instead of {EXAMPLE_RESULT_P1} got winnings {winnings}"

    # hands = [Hand(*hand.split()) for hand in PUZZLE_INPUT.splitlines()]
    # puzzle_winnings = calculate_total_winnings(hands)
    # logging.info(f"Puzzle p1 winnings are: {puzzle_winnings}")


def p2():
    hands = [Hand(*hand.split(), p2=True) for hand in EXAMPLE_GAME.splitlines()]
    winnings = calculate_total_winnings(hands)
    logging.debug(f"The winnings are: {winnings}")
    assert (
        winnings == EXAMPLE_RESULT_P2
    ), f"Instead of {EXAMPLE_RESULT_P2} got winnings {winnings}"

    # hands = [Hand(*hand.split(), p2=True) for hand in PUZZLE_INPUT.splitlines()]
    # logging.debug("Ordered p2 hands:")
    # sorted_hands = sorted(hands)
    # for hand in sorted_hands:
    #     msg = f"{hand} -- JOKER" if "J" in hand.value else f"{hand}"
    #     logging.debug(msg)

    # puzzle_winnings = calculate_total_winnings(hands)
    # logging.info(f"Puzzle p2 winnings are: {puzzle_winnings}")


if __name__ == "__main__":
    p1()
    p2()
