""" Write the pseudocode and code for a function that reverses the words in a sentence. Input: "This is awesome" Output: "awesome is This". Give the Big O notation. """
def reverse(sentence):
    """ split original sentence into a list, then append elements of the old list to the new list starting from last to first. then join the list back toghether. """
    original = sentence.split()

    reverse = []

    count = len(original) - 1

    while count >= 0:
        reverse.append(original[count])
        count = count - 1

    result = " ".join(reverse)

    return result

""" sentence <- input sentence
    result <- empty list
    split_sentence <- sentence split into array
    index <- length of split_sentence - 1
    while index >= 0
        result append split_sentence[index]
        index <- index - 1
    end while
    
    return result
    
    O(N)
"""
