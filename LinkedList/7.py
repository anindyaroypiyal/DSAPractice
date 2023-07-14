from os import *
from sys import *
from collections import *
from math import *



    # Following is the class structure of the Node class:
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
            


def pairsSwap(head):

    # Write your code here. 
    dummy = Node(0,head)

    prev, curr = dummy, head

    while curr and curr.next:
        # save pointers
        nextPair = curr.next.next
        second =  curr.next

        # reverse pair
        second.next = curr
        curr.next = nextPair
        prev.next = second

        # update pointers
        prev = curr
        curr = nextPair
    return dummy.next
