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
    # Input the string here
    document = ""
    calibration_value = calibrate_document(document)
    print(calibration_value)