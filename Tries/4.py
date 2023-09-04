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
        else: return False

        
    def startWith(self, prefix) :
        
        # StartWith function goes here
        cur = self.root
        
        for i in prefix[0]:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
        
        return True

    def prefMatch(self, prefix) :
    
    # StartWith function goes here
        words = ''
        # l = 0
        cur = self.root
        
        for i in prefix:
            if i in cur.children:
                words+=i
                cur = cur.children[i]
            else:
                break
            
        return words
    
        


def spellChecker(dictionary, query):
    # Write your code here.
    dictio = Trie()

    for i in dictionary:
        dictio.insert(i)
    
    if dictio.search(query): 
        return ["CORRECT"]
    elif not dictio.startWith(query):
        s = set(dictionary)
        return sorted(s)
    else:
        w = []
        checker = dictio.prefMatch(query)
        for i in dictionary:
            if i.startswith(checker):
                w.append(i)
        return sorted(w)
        


    