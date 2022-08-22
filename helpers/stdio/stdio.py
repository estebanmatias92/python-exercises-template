import re

#
# Receive an string as parameter for the input.
#
# Exit the program with an error message if the returned value from the input is not numeric.
# Returns value casted to int if value was numeric.
#
def int_input(phrase):
    value = input(phrase)
    regex = "[-+]?\d+$"  # Expression to match integers
    match = re.match(regex, value)

    if match is None:
        raise ValueError("The value is not numeric only.")

    return int(value)


#
# Receive an string as parameter for the input.
#
# Exit the program with an error message if the returned value from the input is not decimal.
# Returns value casted to int if value was numeric.
#
def float_input(phrase):
    value = input(phrase)
    regex = "^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$"  # Expression to match floats
    match = re.match(regex, value)

    if match is None:
        raise ValueError("The value is not a floating point")

    return float(value)