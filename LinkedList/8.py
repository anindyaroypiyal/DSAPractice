from os import *
from sys import *
from collections import *
from math import *

# Following is the class structure of the Node class:   
class Node:
    def __init__(self, data, next = None):
       	self.data = data
        self.next = next

def addNodes(head, n, m):
    # Write your code here.

    skip = 0
    add = 0
    summ= 0
 
    temp = head
    while temp:
        if skip != m:
            skip += 1
            temp = temp.next
            continue
        
        if add != n:
            summ+=temp.data
            add+=1
    
            if add == n or temp.next == None:
        
                t = temp.next
                s = Node(summ,t)
                temp.next = s

                skip = 0
                add = 0
                summ = 0

                temp = s.next
                continue
            temp = temp.next
        
    return head

