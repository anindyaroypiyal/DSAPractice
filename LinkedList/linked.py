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
    
    def print(self):
        if self.head == None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
    
    def delete(self, data):
        if self.head == None:
            print("Linked List is Empty")
        else:
            temp = self.head
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
            while temp != None:
                if temp.data == data:
                    break
                prev = temp
                temp = temp.next
            if temp == None:
                print("Not found")
                return
            prev.next = temp.next
            temp = None
