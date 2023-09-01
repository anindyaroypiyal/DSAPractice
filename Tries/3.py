from os import *
from sys import *
from collections import *
from math import *

class TrieNode:
    def __init__(self):
        self.children = {}

def distinctSubstring(word):
    # Write your code here.
    counter = 0
    root = TrieNode()

    cur = root
    
    for i in range(len(word)):
        for j in range(i,len(word)):

            if word[j] not in cur.children:
                cur.children[word[j]] = TrieNode()
                counter += 1
                cur = cur.children[word[j]]
            
            else:
                cur = cur.children[word[j]]
        
        cur = root

    return counter
            


