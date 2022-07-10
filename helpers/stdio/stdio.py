#
# Receive an string as parameter for the input.
#
# Exit the program with an error message if the returned value from the input is not numeric.
# Returns value casted to int if value was numeric.
#
def int_input(phrase):
    value = input(phrase)

    if not value.isnumeric():
        print("The value is not numeric")
        exit()

    return int(value)


#
# Receive an string as parameter for the input.
#
# Exit the program with an error message if the returned value from the input is numeric.
# Returns value if value was not numeric.
#
def string_input(phrase):
    value = input(phrase)

    if value.isnumeric():
        print("The value is not string")
        exit()

    return value
