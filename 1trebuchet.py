FIRST_VALIDATION_STRING = \
"""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

SECOND_VALIDATION_STRING = \
"""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

TRANSLATION_DICTIONARY = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def are_there_numbers(line: str):
    occurences = get_first_occurrences(line)
    for position in occurences.values():
        if position != -1:
            return True
    else:
        return False

def get_first_occurrences(line: str):
    first_occurrence = {}
    for string in TRANSLATION_DICTIONARY.keys():
        pos = line.find(string)
        first_occurrence[string] = pos
    return first_occurrence

def translate_string_to_numbers(line: str):
    translated_line = line
    while are_there_numbers(translated_line):
        occurrences = get_first_occurrences(translated_line)
        first_occurrence = None
        for string, position in occurrences.items():
            if position == -1:
                continue
            if first_occurrence is None:
                first_occurrence = (string, position)
            else:
                if position < first_occurrence[1]:
                    first_occurrence = (string, position)
        translated_line = translated_line.replace(first_occurrence[0], TRANSLATION_DICTIONARY.get(first_occurrence[0]), 1)
    return translated_line

def calibrate_document_improved(input_string: str):
    calibration_value = 0
    for line in input_string.splitlines():
        if not line:
            continue
        first_digit, last_digit = None, None
        line = translate_string_to_numbers(line)
        for letter in line:
            if str.isdigit(letter):
                last_digit = letter
                if first_digit is None:
                    first_digit = letter
        partial_value = int(''.join([first_digit, last_digit]))
        calibration_value += partial_value
    return calibration_value

def calibrate_document(input_string: str):
    calibration_value = 0
    for line in input_string.splitlines():
        if not line:
            continue
        first_digit, last_digit = None, None
        for letter in line:
            if str.isdigit(letter):
                last_digit = letter
                if first_digit is None:
                    first_digit = letter
        calibration_value += int(''.join([first_digit, last_digit]))
    return calibration_value

if __name__ == "__main__":
    assert calibrate_document(FIRST_VALIDATION_STRING) == 142
    assert calibrate_document_improved(SECOND_VALIDATION_STRING) == 281