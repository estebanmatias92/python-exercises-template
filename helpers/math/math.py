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


# Function with Try-Except
def dividir(dividendo, divisor):
    try:
        result = dividendo / divisor
    except ValueError:
        print("Error en el tipo de valor ingresado.")
    except ZeroDivisionError:
        print("No se puede dividir por cero!!")
    except IOError:
        print("No se puede abrir el archivo.")
    else:
        return result
    finally:  # Esto se ejecuta en caso que no hayan existido errores
        print("Fin de la operación.")


def sum_digits(num):
    """Sums every digit of a given number and returns it.
    Args:
        num (int): Integer to split in digits and sums each one
    Returns:
        int: Returns the sum of the digits of the argument
    """
    sum = 0

    for digit in str(num):
        sum += int(digit)

    return sum


def is_prime(num):
    """Test if an natural number is prime.
    Args:
        num (int): Integer value to test it's primality
    Returns:
        bool: Returns False if the numbers is not prime, else returns True
    """
    # Only natural numbers starting from 2 can be primes
    if num <= 1:
        return False

    # If num is divisible by any of it's predecessors, then num is not prime, return false
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False

    # If the num make it here, it means is probably prime, so return true
    return True


def int_count(num, match):
    """Return the number of appareances of a digit inside a number
    Args:
        num (int): Number to look for digit match
        match (int): Digit from 1 to 9
    Returns:
        int: Times the digit appears in the number
    """
    count = 0

    for i in str(num):
        if match == int(i):
            count += 1

    return count


def factorial(num):
    """Multiplies the number by itself - 1, until hit the number 1, and returns
        the total of those recursive operations at the end.
    Args:
        num (int): Value to find the factorial
    Raises:
        ValueError: This function won't accept cero or less tan cero, so it tells
            the user not to use them
    Returns:
        int: Returns the factorial calculation
    """

    # Check for incorrect values
    if num < 1:
        raise ValueError("Factorial is for Natural numbers above 0.")

    # Base case, if num is 1 or less there is no more operations to do, so return
    # the number
    if num == 1:
        return num

    return num * factorial(num - 1)
