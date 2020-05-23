class Node:
	def __init__(self, text):
		self.text = text
		self.next = None
		self.length = len(text)
		self.error = False #to tell for printing whether text is error or correct


class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, node, value): #add error suggestion to linked list. will NEVER be head
		current = self.head
		while current.next:
			current = current.next
		current.next = node
		if value == True: #value is set to true for correct text, false for our errors
			node.error = True

		

	def add_meta(self, node, total): #just to know how long the initial string is for later functions
		meta = Node("meta")
		meta.length = total
		self.head = meta







