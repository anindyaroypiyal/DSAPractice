class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node


# Don't change the code above.

def getNum(head):
    
    temp = head
    str1 = ''
    while head is not None:
        str1+=str(temp.data)
        temp = temp.next
    
    s = ''.join(reversed(str1))
    num = int(s)
    return num

def addTwoNumbers(head1: Node, head2: Node) -> Node:
    # Write your code here.
   a = getNum(head1)
   b = getNum(head2)

   ans = a + b
   return ans

   