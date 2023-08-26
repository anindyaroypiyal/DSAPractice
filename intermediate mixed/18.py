class myHashMap :

    def __init__(self) :
        # Implement the init method(s).
        self.hm = {}

    def get(self, key) :
        # Implement the get(k) function.
        if key in self.hm:
            return (self.hm[key])
        else:
            return -1
    
    def insert(self, key, value) :
        # Implement the insert(k, v) function.
        self.hm[key] = value

    def remove(self, key) :
        # Implement the remove(k) function. 
        if key in self.hm:   
            del self.hm[key]     
                
    def search(self, key) :
        # Implement the search(k) function.
        if key in self.hm:
            return True
        else: return False

    def getSize(self) :
        # Implement the getSize() function. 
        return len(self.hm)   
    
    def isEmpty(self) :
        # Implement the isEmpty(k) function.
        if len(self.hm) == 0:
            return True
        else: return False
        
# main
myMap = myHashMap()

n = int(input().strip())

for i in range(n) :

    li = input().strip().split(" ")
    typ = int(li[0])
 
    if (typ == 1):
        key = li[1]
        value = int(li[2])
        myMap.insert(key, value)
        
    elif (typ == 2):
        key = li[1]
        myMap.remove(key)
        
    elif (typ == 3):
        key = li[1]
        if (myMap.search(key)):
            print('true')
        else :
            print('false')
              
    elif (typ == 4):
        key = li[1]
        print(myMap.get(key))
    
    elif (typ == 5):
        print(myMap.getSize())
    
    else :
        if(myMap.isEmpty()) :
            print("true")
        else :
            print("false")
    