import logging
from collections.abc import Callable

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)

EXAMPLE_READINGS = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

P1_EXAMPLE_RESULT = 114
P2_EXAMPLE_RESULT = 2


def extrapolate(readings: list[int], predict: Callable):
    derivatives = [readings]

    # Calculate all derivatives in line
    while not all(d == 0 for d in derivatives[-1]):
        current_readings = derivatives[-1]
        if len(current_readings) <= 1:
            raise ValueError(
                f"The current readings shouldnt be this short! {derivatives}",
            )
        current_derivatives = [
            current_readings[i + 1] - current_readings[i]
            for i in range(len(current_readings) - 1)
        ]
        derivatives.append(current_derivatives)

    return predict(derivatives)


def predict_last(derivatives: list[list[int]]):
    reversed_derivatives: list[list[int]] = list(reversed(derivatives))
    for i in range(len(reversed_derivatives)):
        if i == 0:
            reversed_derivatives[i].append(0)
            continue
        d1 = reversed_derivatives[i - 1][-1]
        d2 = reversed_derivatives[i][-1]
        pred = d2 + d1
        reversed_derivatives[i].append(pred)
    return reversed_derivatives[-1][-1]


def predict_first(derivatives: list[list[int]]):
    reversed_derivatives: list[list[int]] = list(reversed(derivatives))
    for i in range(len(reversed_derivatives)):
        if i == 0:
            reversed_derivatives[i] = [0, *reversed_derivatives[i]]
            continue
        d1 = reversed_derivatives[i - 1][0]
        d2 = reversed_derivatives[i][0]
        pred = d2 - d1
        reversed_derivatives[i] = [pred, *reversed_derivatives[i]]
    return reversed_derivatives[-1][0]


def p1(input_: str):
    all_readings = input_.splitlines()
    predicted_readings_sum = 0
    for readings in all_readings:
        readings = list(map(int, readings.split()))
        predicted_readings_sum += extrapolate(readings, predict_last)
    return predicted_readings_sum


def p2(input_: str):
    all_readings = input_.splitlines()
    predicted_readings_sum = 0
    for readings in all_readings:
        readings = list(map(int, readings.split()))
        predicted_readings_sum += extrapolate(readings, predict_first)
    return predicted_readings_sum


def main():
    predicted_sum = p1(EXAMPLE_READINGS)
    assert predicted_sum == P1_EXAMPLE_RESULT, f"Got {predicted_sum}"
    # predicted_sum = p1(PUZZLE_INPUT)
    logging.info(f"Got predicted last readings: {predicted_sum}")

    predicted_sum = p2(EXAMPLE_READINGS)
    assert predicted_sum == P2_EXAMPLE_RESULT, f"Got {predicted_sum}"
    # predicted_sum = p2(PUZZLE_INPUT)
    logging.info(f"Got predicted first readings: {predicted_sum}")


if __name__ == "__main__":
    main()
