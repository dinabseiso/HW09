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
    s = str.lower(s)
    s_tuples = tuple(s)
    histogram = {}
    for letter in s_tuples:
         histogram[letter] = histogram.get(letter, 0) + 1
    dictionary_by_frequency = inverse_dict(histogram)
    sorted_dictionary = sorted(dictionary_by_frequency.keys(), reverse = True)
    for value in sorted_dictionary:
        print dictionary_by_frequency[value]
        if value == dictionary_by_frequency.keys():
            dictionary_by_frequency[value].replace("[","").replace("]", "").replace["'",""]
            # I have no idea how to split this list into a darn string so that each line is a string.
            # Been spending way too much time on this, oops.

def inverse_dict(d):
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
