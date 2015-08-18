#!/usr/bin/env python
# Exercise 3  
# (1) Write a function called most_frequent that takes a string and prints the
#     chars in decreasing order of frequency. (compare and print in lowercase)
# Ex. >>> most_frequent("aaAbcc")
#     a  
#     c
#     b
###############################################################################
# Imports

# Body

def most_frequent(s):
    """ This function takes in a sring, and converts all characters to lowercase
    where possible. A dictionary histogram{} is created, empty to start, with indeces 
    incremented when a letter scanned in string s is found in histogram{}. 

    A dictionary_by_frequency{} is created as the inverse of histogram{}, where values 
    are now keys. So, for a key, we have all letters found to appear at that frequency.

    We then sort the dictionary_by_frequency by keys in descending order, and pass into
    a list, sorted_dictionary.

    We then step through the length of this sorted_dictionary list, and for every step 
    we check to see if sorted_dictionary[i] is a key in dictionary_by_frequency{}.
    It will be. But in order to print the characters one after the other, we need to step
    through the values paired with that key.

    There MUST be a way to do this with list comprehension... ask Daniel. 

    """
    s = str.lower(s)
    histogram = {}
    for letter in s:
         histogram[letter] = histogram.get(letter, 0) + 1
    dictionary_by_frequency = inverse_dict(histogram)
    sorted_dictionary = sorted(dictionary_by_frequency.keys(), reverse = True)
    for i in range(len(sorted_dictionary)):
        if sorted_dictionary[i] in dictionary_by_frequency:
            for character in dictionary_by_frequency[sorted_dictionary[i]]:
                print character


def inverse_dict(d):
    """ An inverse dictionary is created in order to rank the above histogram 
    by frequency, because dictionaries cannot be sorted by values. What was 
    a value is now a key.

    Searches for a value in the passed in dictionary as a key in inverse{}. If 
    the value is not found as a key in inverse{}, then that value now becomes
    a key in inverse{} and is assigned the value paired with d[key].

    Return the inverse{} for completing above function.

    """
    inverse = {}
    for key, value in d.items():
        inverse[value] = inverse.get(value, []) + [key]
    return inverse



###############################################################################
def main():   # DO NOT CHANGE BELOW
    print("Example 1:")
    most_frequent("abcdefghijklmnopqrstuvwxyz")
    print("\nExample 2:")
    most_frequent("The quick brown fox jumps over the lazy dog")
    print("\nExample 3:")
    most_frequent("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna "
    "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
    "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
    "uis aute irure dolor in reprehenderit in voluptate velit "
    "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
    "occaecat cupidatat non proident, sunt in culpa qui officia "
    "deserunt mollit anim id est laborum.")
    print("\nExample 4:")
    most_frequent("Squdgy fez, blank jimp crwth vox!")

if __name__ == '__main__':
    main()
