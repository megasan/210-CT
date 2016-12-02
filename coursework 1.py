""" Write a function that randomly shuffles an array of integers and explain the rationale behind its implementation. """
from random import randrange

def random_shuffle(original):

    result = []

    """ copy random element of input list into a second list, remove that element. until original list is empty. """
    while original:
        rand = randrange(0, len(original))
        temp = original[rand]
        result.append(temp)
        original.remove(temp)
        if not original:
            break

    return result

""" O(N) """
