

  # ---- Node class for reference-----
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def segregateOddEven(head):

    # Write your code here.
    new_list = Node(0)
    nh = new_list

    even = Node(0)
    eh = even

    temp = head
    while temp:
      if temp.data % 2 != 0:
        new_list.next = temp
        new_list = new_list.next
      else:
        even.next = temp
        even = even.next
      temp = temp.next

    even.next = None   #main culprit
    new_list.next = eh.next

    return nh.next
        