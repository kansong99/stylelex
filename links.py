import spacy

nlp = spacy.load("en_core_web_sm")
text = ("He wants to buy red apples, green grapes, and yellow bananas. I like Jill, Jane, and Mary.")
doc = nlp(text)

perrors = {1: "oxford comma at position",  }

class Node:
	def __init__(self, leng):
		self.next = None
		self.error = False #to tell for printing whether text is error or correct
		self.start = 0 #initial string
		self.end = leng #last string


class LinkedList:
	def __init__(self, total): #meta info to know how long the initial string is for later functions
		top = self.head = Node("meta")
		top.length = total
		self.start = 0 #these last two fields are effectively pointers so you know where in string you are
		self.end = 0




	def insert(self, index, 1): #add error suggestion to linked list. will NEVER be head
		current = self.head
		while current.next:
			current = current.next
		current.next = node
		if value == True: #value is set to true for correct text, false for our errors
			node.error = True


llist = LinkedList(len(text))

llist.append(Node(text), True) #append text to linked-list

		

	#def add_meta(self, node, total): #just to know how long the initial string is for later functions
	#	meta = Node("meta")
	#	meta.length = total
	#	self.head = meta ###







