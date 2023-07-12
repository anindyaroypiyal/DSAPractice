class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.
def getNum(head):
    
    temp = head
    str1 = ''
    while temp != None:
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
   s = str(ans)
   ans_string = ''.join(reversed(s))

   head = Node(ans_string[0])

   temp = head
   for i in ans_string[1:len(s)]:
       temp.next = Node(i)
       temp = temp.next
   
   return (head)


    
