""" Write a recursive function (pseudocode and code) to check if a number n is prime. """
import math

def prime_check(start, check):
    """ start always starts at 2 """
    if check == 1 or check == 0:
        return False
    """ check if its 1 or 0 """
    elif check % start == 0:
        return False
    """ check if its divisible by current counter """
    elif start >= math.sqrt(check):
        return True
    """ dont have to go over higher multiples """
    else:
        return prime_check(start + 1, check)
        """ make sure to return your values all the way up the chain of recursive function calls to actually get a value out of it """

""" counter <- 2
    if input == 1 or 0
        return false
        
    else if input mod counter == 0
        return false
        
    else if counter >= square root(input)
        return true
    
    else
        increment counter, run again
"""
