#
# Receive an string as parameter for the input.
#
# Exit the program with an error message if the returned value from the input is not numeric.
# Returns value casted to int if value was numeric.
#
def int_input(phrase):
    value = input(phrase)

    try:
        return int(value)
    except ValueError:
        print("The value is not an integer")
        exit()


#
# Receive an string as parameter for the input.
#
# Exit the program with an error message if the returned value from the input is numeric or decimal.
# Returns value if value was not numeric.
#
def string_input(phrase):
    value = input(phrase)

    if not value.isalpha() and not value.isalnum():
        print("The value is not string")
        exit()

    return value


#
# Receive an string as parameter for the input.
#
# Exit the program with an error message if the returned value from the input is not decimal.
# Returns value casted to int if value was numeric.
#
def float_input(phrase):
    value = input(phrase)

    try:
        return float(value)
    except ValueError:
        print("The value is not a floating point")
        exit()
