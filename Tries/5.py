from typing import *

 

class TrieNode:

 

    def __init__(self):

        

        self.children={}

 

class Trie:

 

    def __init__(self):

        self.root=TrieNode()

 

    def insert(self,n):

        

        cur=self.root

        i=31

        while i>=0:

            bit=n>>i & 1

            if bit not in cur.children:

                cur.children[bit]=TrieNode()

            cur=cur.children[bit]

            i=i-1

 

    def maximum(self,value):

 

        cur=self.root

        i=31

        cur_ans=0

        while i>=0:

            bit=value>>i & 1

            if (1-bit) in cur.children:

                cur=cur.children[bit^1]  #(1-bit) == (bit ^ 1)

                cur_ans=cur_ans | (1<<i)

            else:

                cur=cur.children[bit]

            i=i-1

            

        return cur_ans

            

 

def maximumXor(arr: List[int]) -> int:

 

    root=Trie()

    root.insert(arr[0])

    max_ans=0

 

    for i in range(1,len(arr)):

        max_ans=max(max_ans,root.maximum(arr[i]))

        root.insert(arr[i])

        

    return max_ans