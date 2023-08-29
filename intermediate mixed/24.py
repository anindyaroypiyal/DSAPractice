
from sys import stdin

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None

class LRUCache:
	# Initialize the LRU Cache
	def __init__(self, capacity):
		# Your code goes here
		self.head = Node(0,0)
		self.tail = Node(0,0)
		self.hashMap = {}

		self.capacity = capacity
		self.head.next = self.tail
		self.tail.prev = self.head
	
	def get(self, key):
		# Your code goes here
		if key in self.hashMap:
			n = self.hashMap[key]
			self.remove(n)
			self.insert(n)
			return n.value
		else:
			return -1
	
	def put(self, key, value):
		# Your code goes here
		if key in self.hashMap:
			self.remove(self.hashMap.get(key))
		if len(self.hashMap) == self.capacity:
			self.remove(self.tail.prev)
		self.insert(Node(key, value))

	def remove(self,node):
		del self.hashMap[node.key]
		node.prev.next = node.next
		node.next.prev = node.prev

	def insert(self, node):
		self.hashMap[node.key] = node
		headNext = self.head.next
		self.head.next = node
		node.prev = self.head
		headNext.prev = node
		node.next = headNext


# main
capacity, q = map(int, stdin.readline().rstrip().split(" "))

cache = LRUCache(capacity)

while q != 0:
	query = list(map(int, stdin.readline().rstrip().split()))

	if query[0] == 0:
		key = query[1]
		print(cache.get(key))
	elif query[0] == 1:
		key = query[1]
		value = query[2]
		cache.put(key, value)
	
	q -= 1