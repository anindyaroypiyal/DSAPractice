from math import *
from collections import *
from sys import *
from os import *

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
        

def cloneRandomList(head):
    # Your code goes here.
    deep_head = LinkedListNode(0)
    temp1 = head
    temp2 = deep_head


    while(temp1):
        temp2.next = LinkedListNode(temp1.data)

        temp2 = temp2.next
        temp1 = temp1.next

    temp1 = head
    temp2 = deep_head.next
    
    while(temp2):
        temp2.random = temp1.random

        temp2 = temp2.next
        temp1 = temp1.next
    
    return deep_head.next
