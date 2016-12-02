""" Count the number of trailing 0s in a factorial number. """
import math

def factorial(number):

    i = 1
    result = 0

    """ use maths to work out the number of trailing 0s. """
    while i:
        current = math.floor(number / (5**i))
        if current == 0:
            break
        result = result + current
        i = i + 1

    return result

""" O(N) """
