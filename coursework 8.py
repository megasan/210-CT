""" Write a recursive function (pseudocode and code)that removes all vowels from a given string. Input: "beautiful" Output: "btfl"."""
def remove_vowel(pos, word):
    """ serves as a base case """
    if pos == len(word):
        return word
    """ check for vowels """
    if word[pos] == "a" or word[pos] == "e" or word[pos] == "i" or word[pos] == "o" or word[pos] == "u":
        """ special handling for words starting with a vowel """
        if pos == 0:
            return remove_vowel(pos + 1, word[1:])
        """ normal vowel found handling """
        else:
            new = word[:pos] + word[pos + 1:]
            return remove_vowel(pos, new)
        """ skip """
    else:
        return remove_vowel(pos + 1, word)
    
""" word <- take input
    counter <- 0
    if counter == length of word
        return word
    
    if word[counter] is a vowel
        remove word[counter]
        increment counter
        run again
    else
        increment counter
        run again
"""
