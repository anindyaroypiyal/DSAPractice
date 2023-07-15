from collections import deque

class Queue :
    def __init__(self):
        self.d=deque()




    '''----------------- Public Functions of Queue -----------------'''

   
    def isEmpty(self) :
        return len(self.d)==0



    def enqueue(self, data) :
        self.d.append(data)



    def dequeue(self) :
        if self.isEmpty():
            return -1
        x=self.d.popleft()
        return x



    def front(self) :
        if self.isEmpty():
            return -1
        return self.d[0]