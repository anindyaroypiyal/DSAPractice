def findMiddle(head):

    # Write your code here

    # head denoted head of linked list

    if head!= None:

        curr = head

        c = 0

        while curr!= None:

            c = c+1

            curr = curr.next

        temp = head

        mid = c // 2

        i=0

        while i<mid:

            temp = temp.next

            i = i + 1

        return temp