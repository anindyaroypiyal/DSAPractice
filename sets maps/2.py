from os import *
from sys import *
from collections import *
from math import *
from collections import OrderedDict


def firstNonRepeatingCharacter(str):

    # Write your Code here.
    char_count = {}

    # Count the occurrences of each character
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first character with count 1
    for char in str:
        if char_count[char] == 1:
            return char
    