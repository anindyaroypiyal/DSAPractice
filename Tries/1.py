from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOf = False

class Trie :

    def __init__(self) :

        # constructor for the Trie
        self.root = TrieNode()
    
    def insert(self, string) :

        # Insert function goes here
        cur = self.root
        
        for i in string:
            if i in cur.children:
                cur = cur.children[i]
            else:
                cur.children[i] = TrieNode()
                cur = cur.children[i]
        cur.endOf = True

    
    def search(self, word) :
        
        # Search function goes here
        cur = self.root
        
        for i in word:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
        if cur.endOf == True:
            return True

        
    def startWith(self, prefix) :
        
        # StartWith function goes here
        cur = self.root
        
        for i in prefix:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
        
        return True



# main
t = int(input().strip())
root = Trie()
for i in range(t) :

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1) :
        root.insert(str1)
    
    elif (q == 2) :
        if(root.search(str1)) :
            print("true") 

        else :
            print("false")
        
    else :
        if(root.startWith(str1)) :
            print("true")

        else :
            print("false")

