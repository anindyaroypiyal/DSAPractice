from sys import stdin

#Following is the Node class already written for the Linked List

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

# Stack Class 
class Stack :
    def __init__(self) :

        self.head = None
        self.size = 0    
    
    def getSize(self) :
        return self.size

    def isEmpty(self) :
        return self.size == 0

    def push(self, data) :
        if self.head == None:
            self.head = Node(data)
            self.size += 1
            return
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size += 1

    def pop(self) :
        if self.head == None:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1

    def top(self) :
        
        if self.head == None:
            return -1
        return self.head.data
#main

t = int(stdin.readline().rstrip())
head = Stack()

while t > 0 : 

    query = list(map(int,stdin.readline().strip().split(" ")))
    if query[0] == 1 :
        print(head.getSize()) 
    
    elif query[0] == 2 :

        if(head.isEmpty()) :
            print("true")
        
        else :
            print("false")
    
    elif query[0] == 3 :
        #head = head.push(query[1])
        head.push(query[1])

    elif query[0] == 4:
        #head = head.pop()
        head.pop()

    else :
        if(head == None) :
            print(-1)
        
        else :
            top = head.top()
            print(top)
    t -= 1