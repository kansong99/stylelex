import spacy

nlp = spacy.load("en_core_web_sm")
text = ("He wants to buy red apples, green grapes, and yellow bananas. I like Jill, Jane, and Mary.")
doc = nlp(text)



class Node:
	def __init__(self, text):
		self.text = text
		self.next = None
		self.length = len(text)
		self.error = False #to tell for printing whether text is error or correct


class LinkedList:
	def __init__(self, total): #meta info to know how long the initial string is for later functions
		top = self.head = Node("meta")
		top.length = total
		self.start = 0 #these last two fields are effectively pointers so you know where in string you are
		self.end = 0




	def insert(self, node, value): #add error suggestion to linked list. will NEVER be head
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







