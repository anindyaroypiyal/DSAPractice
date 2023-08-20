from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

#Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
            
            
def isPalindrome(head):
    
    # Write your code here.

    if head == None or head.next == None:
        return True

    temp = head
    Counter = 0
    while temp:
        Counter += 1
        temp = temp.next

    stk = []
    pointer = Counter // 2
    temp = head

    t = 0
    while t < pointer:
        stk.append(temp.data)
        temp = temp.next
        t+=1

    if Counter % 2 != 0:
        temp = temp.next

    while len(stk)!= 0:
        a = temp.data
        b = stk.pop()

        if a != b:
            return False
        else:
            temp = temp.next

    return True
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    
def takeinput():
    
    inputlist=[int(ele) for ele in input().split()]
    
    head=None
    tail=None
    
    for currentData in inputlist:
        
        if currentData == -1:
            break
        
        Newnode=Node(currentData)
        
        if head is None:
            head=Newnode
            tail=Newnode
        else:
            tail.next=Newnode
            tail=Newnode
            
    return head







#Main
t = int(stdin.readline().rstrip())

while t > 0:
    
    head = takeinput()
    
    if isPalindrome(head):
        print('true')
    else:
        print('false')
        
    t -= 1
