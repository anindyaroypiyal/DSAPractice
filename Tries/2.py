from os import *
from sys import *
from collections import *
from math import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count_pref = 0
        self.ends_with = 0

class Trie:
    def __init__(self):
        # Write your code here.
        self.root = TrieNode()

    def insert(self, word):
        # Write your code here.
        cur = self.root

        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
                cur = cur.children[i]
                cur.count_pref = 1
            else:
                cur= cur.children[i]
                cur.count_pref += 1
            
        cur.ends_with += 1


    def countWordsEqualTo(self, word):
        cur = self.root

        for i in word:
            if i not in cur.children:
                return 0
            else:
                cur = cur.children[i]
        return cur.ends_with


    def countWordsStartingWith(self, word):
        cur = self.root

        for i in word:
            if i not in cur.children:
                return 0
            else:
                cur = cur.children[i]
        return cur.count_pref

    def erase(self, word):
        # Write your code here.
        cur = self.root

        for i in word:
            cur.count_pref -= 1
            cur = cur.children[i]
        cur.count_pref -= 1
        cur.ends_with-=1
