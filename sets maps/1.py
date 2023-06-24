from os import *
from sys import *
from collections import *
from math import *



def minElementsToRemove(arr):
    
    # Write your Code here.
    new_arr = [*set(arr)]
    return (len(arr)- len(new_arr))
