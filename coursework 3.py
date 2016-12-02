""" Write the pseudocode for a function which returns the highest perfect square which is less or equal to its parameter (a positive integer). Implement this in a programming language of your choice. """
def power(number):
    x = 1

    """ check if every square number going up from 1 fits. """
    while x * x < number:
        x = x + 1
    """ when the square number goes over the limit roll back the result by 1. """    
    if x * x > number:
        x = x - 1

    return x

""" number to be checked <- input number
squared <- 1

while squared * squared < number to be checked
    squared <- squared + 1

if squared * squared > number to be checked
    squared <- squared - 1

output squared

O(N) complexity """
