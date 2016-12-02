""" Adapt  the  binary  search  algorithm  so  that  instead  of  outputting  whether  a  specific  value was  found,  it  outputs  whether  a  value  within an  interval  (specified  by  you)  was  found. Write the pseudocode and code and give the time complexity of the algorithm using the Big O notation."""
def binarySearch(lower, upper, alist):
    """
    take in a lower bound, upper bound, and a list as input.
    then you have the range of numbers to search for.
    binary search after but the search element is a range of numbers.
    """
    
    bounds = range(lower, upper + 1)
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] in bounds:
            found = True
        else:
            if bounds[0] > alist[midpoint]:
                first = midpoint + 1 
            else:
                last = midpoint - 1
    return found


"""
take lower bound, upper bound and list as inputs
set search start point, end point

while the list is not empty and element is not found
    set a new midpoint using the start point and end point
    if the midpoint is in bounds
        element is found
    else
        if the smallest element is greater than the midpoint
            set lower bound to the current midpoint
        else
            set upper bound to the current midpoint
return whether or not an element matching was found

O(N)
"""
