from os import *
from sys import *
from collections import *
from math import *

from typing import List

def insertionSort(n: int, arr: List[int]) -> None:
    # Write your code here.
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
    return arr
    