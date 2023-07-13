from os import *
from sys import *
from collections import *
from math import *


	# Linked List Node class for reference

class Node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

def insertionSortLL(head):
    dummynode=Node(0,head)
    prev=head
    curr=head.next
    while curr:
        if curr.data>=prev.data:
            prev=curr
            curr=curr.next
            continue
        temp=dummynode
        while curr.data>temp.next.data:
            temp=temp.next
        prev.next=curr.next
        curr.next=temp.next
        temp.next=curr
        curr=prev.next
    return dummynode.next