import math
def p(n):
    """ Return True if "n" is prime, False otherwise """
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    md = math.floor(n**(1/2)) + 1

    for i in range(3, md, 2):
        if n%i == 0:
            return False

    return True
