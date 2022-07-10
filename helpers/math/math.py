#
#   Return a list with all the primes numbers between 2 to num
#
def sieve_of_eratosthenes(num):
    # Initialize the sieve
    primes = []
    composites = []

    # Range limits
    MIN = 2
    MAX = num + 1

    # Exit if the number is too small
    if num < MIN:
        return primes

    for i in range(MIN, MAX):
        # If number is not in the sieve, add it to the list of primes
        if i not in composites:
            primes.append(i)

            # Update the list of composite numbers
            for j in range(i * i, MAX, i):
                composites.append(j)

    return primes


# Finde the minimum number in an iterable object
def minimum(iterable):
    if len(iterable) == 0:
        return None

    if len(iterable) == 1:
        return iterable[0]

    # First number to compare
    MIN = iterable[0]

    # Keep updating the MIN variable with each number lower than MIN
    for value in iterable:
        if value < MIN:
            MIN = value

    return MIN


# Finde the maximum number in an iterable object
def maximum(iterable):
    if len(iterable) == 0:
        return None

    if len(iterable) == 1:
        return iterable[0]

    # First number to compare
    MAX = iterable[0]

    # Keep updating the MAX variable with each number greater than MAX
    for value in iterable:
        if value > MAX:
            MAX = value

    return MAX
