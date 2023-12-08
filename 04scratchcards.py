import logging

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.DEBUG)


EXAMPLE_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
PUZZLE_INPUT = None
EXAMPLE_RESULT_1 = 13
EXAMPLE_RESULT_2 = 30


def transform_card(card: str) -> tuple[list[int], list[int]]:
    _, numbers = card.split(":")
    winning_numbers, numbers_got = numbers.split("|")
    winning_numbers, numbers_got = winning_numbers.split(), numbers_got.split()
    return [int(n) for n in winning_numbers], [int(n) for n in numbers_got]


def calculate_card_points(card: str):
    winning_numbers, numbers_got = transform_card(card)
    points = 0
    for n in numbers_got:
        if n in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points


def calculate_repeats(cards: list[tuple[list[int], list[int]]], index: int):
    current_card_winning_numbers, current_card_numbers_got = cards[index]
    matches = 0
    for number_got in current_card_numbers_got:
        if number_got in current_card_winning_numbers:
            matches += 1
    number_of_cards = 0
    for i in range(1, matches + 1):
        number_of_cards += calculate_repeats(cards, index + i)
    return 1 + number_of_cards


def calculate_card_repeats(cards: str):
    number_of_cards = 0
    transformed_cards = [transform_card(c) for c in cards.splitlines()]
    for i in range(len(transformed_cards)):
        number_of_cards += calculate_repeats(transformed_cards, i)
    return number_of_cards


def calculate_all_points(cards: str):
    points = 0
    for card in cards.splitlines():
        points += calculate_card_points(card)
    return points


if __name__ == "__main__":
    points = calculate_all_points(EXAMPLE_INPUT)
    assert points == EXAMPLE_RESULT_1
    puzzle_points = calculate_all_points(PUZZLE_INPUT)
    logging.info(f"Calculated points are : {puzzle_points}")

    number_of_cards = calculate_card_repeats(EXAMPLE_INPUT)
    assert number_of_cards == EXAMPLE_RESULT_2
    puzzle_number_of_cards = calculate_card_repeats(PUZZLE_INPUT)
    logging.info(f"Number of cards is: {puzzle_number_of_cards}")
