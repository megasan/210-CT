""" Given a sequence of n integer numbers, extract the sub-sequence of maximum length which is in ascending order. """
def consecutive(numbers):

    """
    takes input of a list of numbers and starts counting consecutively increasing numbers.
    the count resets after a number breaks the pattern.
    stores largest count to output.
    """
    pos = 0
    count = 1
    limit = len(numbers)

    while limit > 0:
        if pos + 1 >= len(numbers):
            break
        if numbers[pos] < numbers[pos + 1]:
            count = count + 1
        elif numbers[pos] > numbers[pos + 1]:
            count = 1

        pos = pos + 1
        limit = limit - 1
        
    return count
