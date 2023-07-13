
# Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        


def removeKthNode(head, k):
    # Write your code here.
    dummy = Node(0,head)
    count = 0
    temp = head
    
    while temp:
        count+=1
        temp= temp.next

    removeItem = count - k

    temp = head

    if removeItem == 0:
        return dummy.next.next

    if k == 1:
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        return dummy.next

    c = 0
    while c != removeItem-1:
        temp = temp.next
        c+=1
    temp.next = temp.next.next
    return dummy.next
    
